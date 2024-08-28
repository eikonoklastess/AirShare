from androidstorage4kivy.sharedstorage import Environment
import kivy
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

from androidstorage4kivy import SharedStorage, Chooser, sharesheet
from android_permissions import AndroidPermissions


Environment = autoclass("android.os.Environment")
Port = 22


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

    hostname = ""
    username = ""
    password = ""

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
        except Exception as e:
            print(e)
            self.ids["connexion_err"].text = ConnectionStatus.FAILED.value
        finally:
            self.ssh.close()

    def chooser_start(self):
        self.file_chooser_text = ""
        self.chooser = Chooser(self.chooser_callback)
        self.chooser.choose_content("*/*")

    def chooser_callback(self, uri_list):
        try:
            ss = SharedStorage()
            for uri in uri_list:
                self.file_chooser_text += get_file_name_from_uri(str(uri))
                ss.copy_from_shared(uri)
        except Exception as e:
            Logger.warning("SharedStorageExample.chooser_callback():")
            Logger.warning(str(e))

    def transfer(self):
        self.ids["send_btn"].text = TransferStatus.TRANSFERING.value
        try:
            # Connect to the server
            self.ssh.connect(
                hostname=self.hostname,
                port=Port,
                username=self.username,
                password=self.password,
            )
            # Create an SFTP session from the SSH connection
            sftp = self.ssh.open_sftp()
            remote_file_path = "~/test"

            print("=================================================================\n")
            context = mActivity.getApplicationContext()
            result = context.getExternalCacheDir()
            if result:
                for root, dirs, files in os.walk(result.getPath()):
                    for file in files:
                        file_path = os.path.join(root, file)
                        print(f"file path: {file_path}\n")
                        print(f"/Users/walidoutaleb/test/{os.path.split(file_path)[1]}")
                        sftp.put(
                            file_path,
                            f"/Users/walidoutaleb/test/{os.path.split(file_path)[1]}",
                        )
            else:
                raise ValueError("cool")
            print("=================================================================\n")
            # cache_dir = os.path.join(app_storage_path(), "cache")
            # print(f"chache_dir: {cache_dir}\n")
            # for root, dirs, files in os.walk(cache_dir):
            #     for file in files:
            #         file_path = os.path.join(root, file)
            #         print(f"found file: {file_path}\n")
            # sftp.put(local_file_path, remote_file_path)

            self.ids["send_btn"].text = TransferStatus.FINISHED.value
        except Exception as e:
            self.ids["send_btn"].text = TransferStatus.FAILED.value
            print(e)
        finally:
            # Close the SFTP session and SSH connection
            sftp.close()
            self.ssh.close()
            temp = SharedStorage().get_cache_dir()
            if temp and os.path.exists(temp):
                rmtree(temp)

        # def permissions_external_storage(self):
        #     if platform == "android":
        #         PythonActivity = autoclass("org.kivy.android.PythonActivity")
        #         Environment = autoclass("android.os.Environment")
        #         Intent = autoclass("android.content.Intent")
        #         Settings = autoclass("android.provider.Settings")
        #         Uri = autoclass("android.net.Uri")
        #         if api_version > 29:
        #             # If you have access to the external storage, do whatever you need
        #             if Environment.isExternalStorageManager():
        #                 # If you don't have access, launch a new activity to show the user the system's dialog
        #                 # to allow access to the external storage
        #                 pass
        #             else:
        #                 try:
        #                     activity = mActivity.getApplicationContext()
        #                     uri = Uri.parse("package:" + activity.getPackageName())
        #                     intent = Intent(
        #                         Settings.ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION, uri
        #                     )
        #                     currentActivity = cast(
        #                         "android.app.Activity", PythonActivity.mActivity
        #                     )
        #                     currentActivity.startActivityForResult(intent, 101)
        #                 except:
        #                     intent = Intent()
        #                     intent.setAction(
        #                         Settings.ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION
        #                     )
        #                     currentActivity = cast(
        #                         "android.app.Activity", PythonActivity.mActivity
        #                     )
        #                     currentActivity.startActivityForResult(intent, 101)
        #                     activity.startActivityForResult(intent, 1)


class MyApp(App):
    def build(self):
        return MyLayout()

    def on_start(self):
        self.dont_gc = AndroidPermissions()
        temp = SharedStorage().get_cache_dir()
        if temp and os.path.exists(temp):
            rmtree(temp)

    def quit_app(self, window, key, *args):
        if key == 27:
            mActivity.finishAndRemoveTask()
            return True
        else:
            return False


def get_file_name_from_uri(uri_string):
    # Import the necessary Java classes
    Uri = autoclass("android.net.Uri")
    Context = autoclass("android.content.Context")
    ContentResolver = autoclass("android.content.ContentResolver")

    # Get the application context
    context = autoclass(
        "org.kivy.android.PythonActivity"
    ).mActivity.getApplicationContext()

    # Convert the string URI to a Uri object
    uri = Uri.parse(uri_string)

    # Get the content resolver
    content_resolver = context.getContentResolver()

    # Define the projection (the columns you want to retrieve)
    projection = ["_display_name"]

    # Query the content resolver
    cursor = content_resolver.query(uri, projection, None, None, None)

    # Extract the file name from the cursor
    file_name = ""
    if cursor and cursor.moveToFirst():
        name_index = cursor.getColumnIndexOrThrow("_display_name")
        file_name = cursor.getString(name_index)
        cursor.close()

    return file_name


if __name__ == "__main__":
    MyApp().run()
