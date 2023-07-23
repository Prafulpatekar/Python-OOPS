import socket

host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((ip_addr,55555))
msg = sock.recv(1024)
sock.send("Kya bolte".encode())

print("Message", msg.decode())
