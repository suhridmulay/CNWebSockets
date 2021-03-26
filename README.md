# CN Assignment 2  
Web server and client application in python

## Requisites  
- **server1.py** : Your server program "server1.py " will be a single process server that can handle only one client at a time. If a second client tries to chat with the server while some other client's session is already in progress, the second client's socket operations should see an error. After the first client closes the connection, the server should then accept connections from the other client.
- **server2.py** : Your server program "server2.py " will be a multi-threaded server that will create a new thread for every new client request it receives. Multiple clients should be able to simultaneously chat with the server.
- **server3.py** : Your server program "server3.py " will be a single process server that uses the "select" method to handle multiple clients concurrently.
- **server4.py** : Your server program "server4.py" will be an echo server (that replies the same message to the client that was received from the same client); it will be a single process server that uses the "select" method to handle multiple clients concurrently.

## Done
    - [x] client.py
    - [x] server1.py
    - [x] server2.py  
    - [x] server3.py
    - [x] server4.py
    - [ ] video
    - [ ] screenshots