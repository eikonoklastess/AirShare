import kivy
import paramiko
from kivy.app import App, ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file("my.kv")


class MyLayout(Widget):
    status = StringProperty(defaultvalue="notconnected")
    hostname = StringProperty(defaultvalue="host@name - IP")
    port = 22  # Default SSH port
    username = StringProperty(defaultvalue="your_username")
    password = StringProperty(defaultvalue="your_password")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.hostname = self.ids["hostname"].text
        self.username = self.ids["username"].text
        self.password = self.ids["password"].text

        try:
            self.ssh.connect(
                hostname=self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
            )
            self.status = "success"
            # print("connection successful")

        except Exception as e:
            self.status = f"failed = {e}"
            # print(e)
        finally:
            self.ssh.close()


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
