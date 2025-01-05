import socket
class MySocket:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host,self.port))
        return self.sock

    def __exit__(self,exc_type, exc_val,exc_tb):
        self.sock.close()

with MySocket('localhost', 8384) as s:
    s.send('Hello World! 8384')
