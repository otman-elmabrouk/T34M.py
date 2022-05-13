#!/usr/bin/python3
HOST='192.168.1.101'
PORT=4455
from os import mkdir, path, system
i=1
dir_exist = path.isdir("./monitor_transfers")
if dir_exist == False:
	mkdir("monitor_transfers")
print("[!] Transfers will be found in ./monitor_transfers directory")
print("[!] To stop serving run: killall monitor_server.py nc")
while True:
	command = "nc -lvp"+ str(PORT) +" > ./monitor_transfers/docs" +str(i)
	system(command)
	i += 1
