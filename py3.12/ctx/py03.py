import socket
class ManagedSocket:
    def __init__(self,address,port):
        self.address = address
        self.port = port

    def __enter__(self):
        self.sock = socket.socket()
        self.sock.connect((self.address,self.port))
        return self.sock

    def __exit__(self,*exc):
        self.sock.close()

with ManagedSocket('localhost', 8384) as s:
    s.send(b'GET /HTTP/1.1\r\nHost:localhost\r\n\r\n')
