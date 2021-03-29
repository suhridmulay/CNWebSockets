# CN Assignment 2  
Web server and client application in python

## Requisites  
- **server1.py** : Your server program "server1.py " will be a single process server that can handle only one client at a time. If a second client tries to chat with the server while some other client's session is already in progress, the second client's socket operations should see an error. After the first client closes the connection, the server should then accept connections from the other client.
- **server2.py** : Your server program "server2.py " will be a multi-threaded server that will create a new thread for every new client request it receives. Multiple clients should be able to simultaneously chat with the server.
- **server3.py** : Your server program "server3.py " will be a single process server that uses the "select" method to handle multiple clients concurrently.
- **server4.py** : Your server program "server4.py" will be an echo server (that replies the same message to the client that was received from the same client); it will be a single process server that uses the "select" method to handle multiple clients concurrently.

## Usage
start desired server with ````python3 serverX.py```` where X is the number of server file (1 to 4) these start at the localhost, you can specify a port at the prompt or leave it blank as it defaults to 10000.  

Next up, start ````python3 continous_client.exe```` This is the client. It defaults to localhost:10000 (same as the server) but you can change the host and port if you wish to. The client displays a prompt, enter a message and begin communicating with the server.

for servers 1 to 3, you can try sending basic arithmetic expressions which will be evaluated by the server and returned to you. server4 is an echo server which repeats whatever it hears from the client. 

## Notes
If you are running on MacOS, you might need to run ````server1_u.py```` instead of ````server1.py```` due to some undocumented OS Specific behavious by sockets API on MacOS

This repository can be found on github at http://www.github.com/suhridmulay/CNWebSockets

## Done
    - [x] client.py
    - [x] server1.py
    - [x] server2.py  
    - [x] server3.py
    - [x] server4.py
    - [ ] video
    - [ ] screenshots
