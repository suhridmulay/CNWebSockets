# Socket for networking
# Threads for multithreading support
import socket, threading, sys

MAX_CLIENTS = 10

# Initialise the server socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set up the address tuple
HOST_NAME: str = 'localhost'
PORT_NO = 10000
if sys.argv[1]:
    PORT_NO = sys.argv[1]
else:
    print('No port specified in arguments')
    PORT_NO = input('Enter port number to host server on (default 10000): ')
PORT_NO = int(PORT_NO)
address = (HOST_NAME, PORT_NO)

# Bind the socket to said address
server_sock.bind(address)

# Listen for connections
# Put out address on stdout
server_sock.listen(MAX_CLIENTS)
print('Server listening on {}:{}'.format(HOST_NAME, PORT_NO))

# Create a list to store threads
threads = []

# Handler function for connection
def handle(conn: socket.socket, addr: tuple):
    """
    Handler is the method that handles individual connections. 
    It takes in the client socket, and the client address as input and
    Handles the connection to and fro from the server to the client
    """
    thread_id = threading.get_ident()
    print('Thread {} recieved connection from {}'.format(thread_id, addr))
    while True:
        # Read the query
        request = conn.recv(1024).decode('utf-8').strip('')
        print('Client said: {}'.format(request))
        # If request asks to terminate break out of loop
        if request in ('', 'bye', 'exit'):
            break   
        # Prepare response
        response = ''
        try:
            query_soln = eval(request)
            response = '[Thread {}] says: {}'.format(thread_id, query_soln)
        except Exception:
            response = '[Thread {}] says: {}'.format(thread_id, 'Bad query in request, please enter a valid expression')      
        # Send response
        conn.sendall(response.encode('utf-8'))
        print('Responding with: {}'.format(response))
    
    conn.sendall('bye'.encode('utf-8'))
    conn.close()
    return


SERVER_STATE = 'running'


while SERVER_STATE == 'running':
   # Accept a client and store its details
   connection, address = server_sock.accept()
   # Assign a worker thread to the client
   new_t = threading.Thread(target=handle, args=(connection, address, ))
   # Set the new thread up to be a Daemon
   # Thus newly created threads won't block main from exiting
   new_t.daemon = True
   # Append to a list of threads
   threads.append(new_t)
   # Start the thread
   new_t.start()

# Catch any stray threads (although there should be none)
for thread in threads:
    thread.join()

# Close socket
server_sock.close()
