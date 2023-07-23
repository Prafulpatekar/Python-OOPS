import socket

host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind((ip_addr,55555))
sock.listen()

while True:
    client, ip_address = sock.accept()
    print("Connected to IP Address...",ip_address)
    print("Client...",client)
    client.send("You are connected!".encode())
    print(client.recv(1024))
    client.close()