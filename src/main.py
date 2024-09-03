from sys import stderr
from androidstorage4kivy.sharedstorage import Environment
import kivy
import socket
from kivy.uix.label import Label
import paramiko
from kivy.app import App, ObjectProperty, StringProperty
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.utils import platform
from android import mActivity, autoclass, api_version
from android.storage import app_storage_path
from enum import Enum
import os
from shutil import rmtree
from cryptography.fernet import Fernet

from androidstorage4kivy import SharedStorage, Chooser
from android_permissions import AndroidPermissions

key = Fernet.generate_key()
cipher_suite = Fernet(key)
encrypted_password = ""
Environment = autoclass("android.os.Environment")
Port = 22
PythonActivity = autoclass("org.kivy.android.PythonActivity")
AirShareDir = "~/airshare"
Context = autoclass("android.content.Context")
current_activity = autoclass("org.kivy.android.PythonActivity").mActivity
private_storage_path = current_activity.getFilesDir().getAbsolutePath()


class ConnectionStatus(Enum):
    NOT_CONNECTED = "connect"
    CONNECTED = "connected"
    FAILED = "invalid"


class TransferStatus(Enum):
    NOT_TRANSFERING = "send"
    FINISHED = "finished"
    TRANSFERING = "sending"
    FAILED = "failed"


class MyLayout(BoxLayout):
    path = ""

    connexion_error = StringProperty("")
    file_chooser_text = StringProperty("choose file")

    hostname = StringProperty("")
    username = StringProperty("")
    password = StringProperty("")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.hostname = self.ids["hostname"].text
        self.username = self.ids["username"].text
        self.password = self.ids["password"].text

        try:
            self.ssh.connect(
                hostname=self.hostname,
                port=Port,
                username=self.username,
                password=self.password,
            )
            self.ids["connexion_err"].text = ConnectionStatus.CONNECTED.value
            self.ids["connexion_err"].color = (76 / 255, 175 / 255, 80 / 255, 1)
            print("======================")
            print("in connect")
            save_server(self.hostname, self.username, self.password)
            print("======================")
        except Exception as e:
            print(e)
            self.ids["connexion_err"].text = ConnectionStatus.FAILED.value
            self.ids["connexion_err"].color = (1, 0, 0, 1)
        finally:
            self.ssh.close()

    def chooser_start(self):
        if self.file_chooser_text == "choose file":
            self.file_chooser_text = ""
        self.chooser = Chooser(self.chooser_callback)
        self.chooser.choose_content("*/*")

    def chooser_callback(self, uri_list):
        try:
            ss = SharedStorage()
            for uri in uri_list:
                self.file_chooser_text = (
                    self.file_chooser_text + "\n" + str(get_file_name(uri))
                )
                print("============================\n")
                print(str(get_file_name(uri)))
                print("\n============================\n")
                ss.copy_from_shared(uri)
        except Exception as e:
            Logger.warning("SharedStorageExample.chooser_callback():")
            Logger.warning(str(e))

    def transfer(self):
        self.ids["send_btn"].text = TransferStatus.TRANSFERING.value
        try:
            self.ssh.connect(
                hostname=self.hostname,
                port=Port,
                username=self.username,
                password=self.password,
            )
            stdin, stdout, stderr = self.ssh.exec_command("ver")
            stdout.channel.recv_exit_status()
            err = stderr.read().decode()
            if err:
                mkdir_command = f"mkdir {AirShareDir}"
                finder_command = f"open {AirShareDir}"
            else:
                mkdir_command = "mkdir %USERPROFILE%\\airshare"
                finder_command = "explorer %USERPROFILE%\\airshare"

            stdin, stdout, stderr = self.ssh.exec_command(mkdir_command)
            stdout.channel.recv_exit_status()
            err = stderr.read().decode()
            if err:
                print(f"Error: {err}")
            stdin, stdout, stderr = self.ssh.exec_command(finder_command)
            stdout.channel.recv_exit_status()
            err = stderr.read().decode()
            if err:
                print(f"Error: {err}")

            sftp = self.ssh.open_sftp()

            context = mActivity.getApplicationContext()
            result = context.getExternalCacheDir()
            if result:
                for root, dirs, files in os.walk(result.getPath()):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if mkdir_command == f"mkdir {AirShareDir}":
                            sftp.put(
                                file_path,
                                f"/Users/{self.username}/airshare/{os.path.split(file_path)[1]}",
                            )
                        else:
                            stdin, stdout, stderr = self.ssh.exec_command(
                                "echo %USERPROFILE%"
                            )
                            userprofile = stdout.read().decode().strip()
                            if stderr.read():
                                print(
                                    f"Error retrieving USERPROFILE: {stderr.read().decode().strip()}"
                                )
                            sftp.put(
                                file_path,
                                f"{userprofile}\\airshare\\{os.path.split(file_path)[1]}",
                            )

            self.ids["send_btn"].text = TransferStatus.FINISHED.value
            self.ids["send_btn"].color = (76 / 255, 175 / 255, 80 / 255, 1)

        except Exception as e:
            self.ids["send_btn"].text = TransferStatus.FAILED.value
            self.ids["send_btn"].color = (1, 0, 0, 1)
            print(f"Exception: {e}")
        finally:
            # Close the SFTP session and SSH connection
            sftp.close()
            self.ssh.close()
            temp = SharedStorage().get_cache_dir()
            if temp and os.path.exists(temp):
                rmtree(temp)

    def switch_to_help(self):
        # Switch to the help layout
        self.ids.screen_manager.current = "help_screen"

    def switch_to_main(self):
        # Switch back to the main layout
        self.ids.screen_manager.current = "main_screen"


def get_file_name(uri):
    content_resolver = PythonActivity.mActivity.getContentResolver()
    cursor = content_resolver.query(uri, None, None, None, None)
    if cursor is not None:
        try:
            if cursor.moveToFirst():
                name_index = cursor.getColumnIndexOrThrow("_display_name")
                return cursor.getString(name_index)
        finally:
            cursor.close()
    # Fallback to getting the file name from the path if necessary
    path = uri.getPath()
    return path.split("/")[-1] if path else "Unknown"


def save_server(ip, username, password):
    file_name = "server_info.txt"
    info = f"{ip} {username} {password}"
    file_path = os.path.join(private_storage_path, file_name)
    print("=======================")
    print(f"saving info at {file_path}")
    with open(file_path, "w") as file:
        file.write(info)
    print("saved")
    print("=======================")


def load_server():
    file_name = "server_info.txt"
    file_path = os.path.join(private_storage_path, file_name)
    content = ""
    try:
        with open(file_path, "r") as file:
            content = file.read()
        print("=======================")
        print("loaded from mem:")
        print(content)
        print("=======================")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        return content


class MyApp(App):
    def build(self):
        self.layout = MyLayout()
        return self.layout

    def on_start(self):
        self.dont_gc = AndroidPermissions()
        temp = SharedStorage().get_cache_dir()
        if temp and os.path.exists(temp):
            rmtree(temp)
        print("======================")
        print("on_start:")
        content = load_server()
        print("======================")
        if content != "":
            info = content.split(" ")
            self.layout.hostname = info[0]
            print(self.layout.hostname)
            self.layout.username = info[1]
            self.layout.password = info[2]
            self.layout.ids.hostname.text = self.layout.hostname
            self.layout.ids.username.text = self.layout.username
            self.layout.ids.password.text = self.layout.password

    def quit_app(self, window, key, *args):
        if key == 27:
            mActivity.finishAndRemoveTask()
            return True
        else:
            return False


if __name__ == "__main__":
    MyApp().run()
