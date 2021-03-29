import socket, threading, sys

# Create the server socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Create the address tuple
HOST_NAME: str = 'localhost'
PORT_NO = 10000
if sys.argv[1]:
    PORT_NO = sys.argv[1]
else:
    print('No port specified in arguments')
    PORT_NO = input('Enter port number to host server on (default 10000): ')
PORT_NO = int(PORT_NO)
PORT_NO = int(PORT_NO)
address_tuple = (HOST_NAME, PORT_NO)

# Bind the server to the said address and star listening for connections
server_sock.bind(address_tuple)
server_sock.listen(10)
print('Server listening on localhost:{}'.format(PORT_NO))

# Initialise current active thread to none
# This represents the thread handling connections to and from the client
active_thread: threading.Thread = None


# Define a handler function for the connection
def handler(conn : socket.socket, addr: tuple):
    print('Handling connection from {}'.format(addr))
    query = conn.recv(1024).decode('utf-8')
    while query != 'bye':
        print('Client said: {}'.format(query))
        resp = ''
        try:
            result = eval(query)
            resp: str = 'Query evaluates to: {}'.format(result)
        except Exception:
            resp: str = 'Bad query, please enter a valid expression'
        conn.sendall(resp.encode('utf-8'))
        query = conn.recv(1024).decode('utf-8')
    print('Terminating connection, client said bye')
    active_thread = None
    return

# Set the current server state to running
server_state = 'RUNNING'

# Server loop
while server_state == 'RUNNING':
    # Accept a client
    conn, addr = server_sock.accept()
    print('Incoming connection from {}'.format(addr))
    # Check if any other client is being serviced
    if active_thread and active_thread.is_alive():
        # If yes, notify the client that the server is busy and will communicate later
        # Terminate connection
        print('Server busy, notifying client and closing connection')
        conn.sendall('busy'.encode('utf-8'))
        conn.close()
    else:
        # If server is free, set active thread to server this client
        active_thread = threading.Thread(target=handler, args=(conn, addr))
        active_thread.daemon = True
        active_thread.start()

