import socket
import time

host = '127.0.0.1'
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print(f"Server is listening on {host}, {port}")

conn, addr = s.accept()
print(f'Connected with {str(addr)}')

data = conn.recv(1024).decode('utf-8')
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Received from the client: {data}")
print(f"time: {current_time}")

response = f"The message is received"
conn.send(response.encode('utf-8'))
conn.close()
s.close()
