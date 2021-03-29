import socket
import sys

talker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '127.0.0.1'
port = 10000

# Get server from command line args or take input from user
print(sys.argv, len(sys.argv))
if len(sys.argv) > 2 and sys.argv[1]:
    server = sys.argv[1]
else:
    print('Invalid arguments, enter server manually')
    server = input('Enter address of server to connect to (default 127.0.0.1): ')

# Get port from command line
if len(sys.argv) > 2 and sys.argv[2]:
    port = int(sys.argv[2])
else:
    print('Invalid arguments, enter port manually')
    port = input('Enter server port to connect to (default 10000): ')

talking = True

talker_socket.connect((server, port))

while talking:
    dialog = input('Enter  your message to server: ')
    if dialog == "bye":
        print('Terminating connection')
        talker_socket.sendall('bye'.encode('utf-8'))
        break
    talker_socket.sendall(dialog.encode('utf-8'))
    response = talker_socket.recv(1024).decode().strip('')
    if response == '':
        print('Blank response from server. Is server dead?')
    if response == 'busy':
        print('Server is busy, try again later')
        print('Closing connection')
        break;
    print('Server said: {}'.format(response))

talker_socket.close()