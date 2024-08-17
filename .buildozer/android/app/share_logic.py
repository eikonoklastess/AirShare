"""
!!! need to create a dir "~/AirShare"
AirShare
    |
    +--------> current
    |
    +--------> History
                  |
                  +---------> h1
                  +---------> h2
                  +---------> etc

The local file path depend on the user choice. logic in the app ui

ssh commands with paramiko:
command = 'ls -la /path/to/directory'
stdin, stdout, stderr = ssh.exec_command(command)
"""

import paramiko

# Define the server and login details
hostname = "your.server.ip"
port = 22  # Default SSH port
username = "your_username"
password = "your_password"  # Or use a private key file

# Create a new SSH client
ssh = paramiko.SSHClient()

# Automatically add the server's SSH key
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the server
    ssh.connect(hostname, port, username, password)

    # Create an SFTP session from the SSH connection
    sftp = ssh.open_sftp()

    # Define local and remote file paths
    local_file_path = "path/to/local/file"
    remote_file_path = "/remote/directory/filename"

    # Upload the file

    sftp.put(local_file_path, remote_file_path)

    # Alternatively, download a file
    # sftp.get(remote_file_path, local_file_path)

    print(f"File transferred successfully to {remote_file_path}")
except Exception as e:
    print(e)
finally:
    # Close the SFTP session and SSH connection
    sftp.close()
    ssh.close()
