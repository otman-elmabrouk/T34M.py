#!/usr/bin/python3

import os
i=1
dir_exist = os.path.isdir("./transfers")
if dir_exist == False:
        os.mkdir("./transfers") 
while True:
        command = "nc -lvp 4444 > ./transfers/docs" +str(i)
        os.system(command)
        i += 1
