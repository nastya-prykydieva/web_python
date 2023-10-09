import socket

host = '127.0.0.1'
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

message = input("Enter text to send to the server: ")
s.send(message.encode('utf-8'))

response = s.recv(1024).decode('utf-8')
print(f"Response from the server: \n{response}")
s.close()
