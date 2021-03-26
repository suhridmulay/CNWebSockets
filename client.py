import socket

# Create the client socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Get the name of the server from user
server = input('Enter server to connect to: ')
if server == '':
    server = 'localhost'

# Get the port from user
port = input('Enter port to connect to (default 80): ')
# If port not specified use default 80
if (port == ''):
    port = 80

# connect to said server
sock.connect((server, 80))

# Generate request string
request_string = input('Enter request string (default HTTP GET for /): ')
if request_string == '':
    request_string = 'GET / HTTP/1.1\r\n'
    request_string += 'Connection: close\r\n'
request_string += '\r\n'
# Forward request string to server
sock.sendall(request_string.encode('utf-8'))

data = sock.recv(1024)
while data:
    data = data.decode('utf-8', errors='ignore')
    print(data, end='')
    data = sock.recv(1024)
print()
sock.close()