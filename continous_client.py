import socket

talker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = input('Enter address of server to connect to (default 127.0.0.1): ')
if server == '':
    server = '127.0.0.1'

port = input('Enter server port to connect to (default 10000): ')
if port == '':
    port = 10000

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
    print('Server said: {}'.format(response))
talker_socket.close()