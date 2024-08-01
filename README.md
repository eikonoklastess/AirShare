# AirShare
AirShare is a replacement for AirDrop that works with Android and macOS 

### TODO
## transfert data between machines on same network
## phone -> pc
?:
- choose data to transfert phone: android app python
    - choose receiver?
    - open file viewer
    - choose either file or dir
    - tap send
- listen on a port on pc ?
- start transfert protocol ??? bluetooth better?
- send data to that port ??
- connect to pc (?ssh) 
- create new directory mv data
- open finder in that dir
- open document ex: pdf

### concrete todo
- android app:
    - choose file and send button
    - ssh to pc 1. begin FTP server
    - connect to server
    - send data
    - ssh to pc 1. mkdir AirShare AirShare-History 2. finder at AirShare 3. if applicable open document
- setup FTP server and client on phone pc
    - pc is the FTP server

### other feature
- android->windows
- pc->phone

### TODO3
- android app:
    1.	Flet?? Kivy or BeeWare: For building the Android app’s GUI and handling Android-specific features.
	2.	Paramiko: For SSH functionality, allowing you to connect to and control your Mac.
	3.	ftplib: For FTP client operations, enabling file transfers. 
	4.	Pyjnius: To access Android Java APIs, like the file picker. !!!
- macos cli:
    1. pyftpdlib: simple ftp server operations
