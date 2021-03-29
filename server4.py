import socket, select
import sys

# Create and internet socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set the server to not block 
server_sock.setblocking(False)

# Set up address tuple
HOST_ADDR = 'localhost'
PORT_NO = 10000
if sys.argv[1]:
    PORT_NO = sys.argv[1]
else:
    print('No port specified in arguments')
    PORT_NO = input('Enter port number to host server on (default 10000): ')
PORT_NO = int(PORT_NO)
address = (HOST_ADDR, PORT_NO)

# Bind socket to address
server_sock.bind(address)
server_sock.listen(10)

print("Server listening at {}:{}".format(HOST_ADDR, PORT_NO))

# Initialise list of inputs and outputs
inputs = [server_sock]
outputs = []

# Program loop
while True:
    # Select ready files using select
    read_ready, write_ready, errored = select.select(inputs, outputs, inputs)

    for file in read_ready:
        # If server is ready for reading
        if file == server_sock:
            # Get connection details from it
            conn, addr = server_sock.accept()
            print('Incoming connection from {}'.format(addr))
            inputs.append(conn)

        # If the input stream is stdin
        elif file == sys.stdin:
            cmd = sys.stdin.readline().strip('')
            if cmd in ('exit', 'quit'):
                print('Terminating server')
                exit()

        # Otherwise the file is a socket
        elif file:
            data = file.recv(1024).decode('utf-8').strip('')
            if data:
                # Facility to gracefully terminate connection
                if data == 'bye':
                    print('terminating connection on client request')
                    inputs.remove(file)
                # Log all incoming requests
                print("Recieved: {}".format(data))
                file.sendall(data.encode('utf-8'))
            else:
                file.close()
                inputs.remove(file)