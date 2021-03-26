import socket, threading

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up the address tuple
HOST_NAME: str = 'localhost'
PORT_NO = input('Enter port number to host server on (default 10000): ')
if PORT_NO == '':
    PORT_NO = 10000
PORT_NO = int(PORT_NO)
address = (HOST_NAME, PORT_NO)

server_sock.bind(address)

server_sock.listen(10)
print('Server listening on {}:{}'.format(HOST_NAME, PORT_NO))

threads = []

def handle(conn: socket.socket, addr: tuple):
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
            response = '[Thread {}] says: {}'.format(thread_id, 'Bad query in request')      
        # Send response
        conn.sendall(response.encode('utf-8'))
    
    conn.sendall('bye'.encode('utf-8'))
    conn.close()
    threading.current_thread().join()


SERVER_STATE = 'running'

while SERVER_STATE == 'running':
    connection, address = server_sock.accept()
    new_t = threading.Thread(target=handle, args=(connection, address, ))
    threads.append(new_t)
    new_t.start()

for thread in threads:
    thread.join()

server_sock.close()
