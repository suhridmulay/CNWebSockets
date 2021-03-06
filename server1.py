import socket

# Input port to run on
PORT = input('Enter port number (default 10000): ')
if PORT == '':
    PORT = 10000

# Set host address to localhost
HOST = 'localhost'

# Create socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Address tuple
address = (HOST, PORT)

# Bind socket to address
server_sock.bind(address)
# Listen for incoming connections
server_sock.listen(1)

# Notify user socket is listening
print('server listening on {}:{}'.format(HOST, PORT))

# Set socket state to running
STATE = 'running'

# Server loop
while STATE == 'running':
    # Accept connections
    server_sock.listen()
    conn, addr = server_sock.accept()
    print('Accepted connection from: {}'.format(addr))
    # Shutdown the socket so that new connections are no longer entertained
    server_sock.shutdown(0)

    # Start communication
    req = conn.recv(1024).decode('utf-8').strip()

    # Continue until server recieves a bye
    while req != 'bye':
        # Log out client's response
        print('Client said: {}'.format(req))
        # Prepare a response
        response = ''
        try:
            query_res = eval(req)
            response = 'Query evaluates to: {}'.format(query_res)
        except Exception:
            response = 'An exception occured'
        # Send the response
        conn.sendall(response.encode('utf-8'))
        # Fetch next query
        req = conn.recv(1024).decode('utf-8').strip()

    print('[ACTION] Terminating connection with {}'.format(addr))
    print('[REASON] Client said \'bye\'')
    
    # Send bye to client
    conn.sendall('bye'.encode('utf-8'))
    conn.close()
socket.close()
