import socket

host = "127.0.0.1" 
port = 42069  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b"Hello, world")
    data = s.recv(24069)

print(f"Received {data!r}")