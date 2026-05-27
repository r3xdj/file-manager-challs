#!/usr/bin/env python3
import os, hashlib, time, sys, subprocess

def init():
	sys.stdout.reconfigure(line_buffering=True)
	sys.stderr.reconfigure(line_buffering=True)
	os.system("stty -echo")

def new_welcome():
	print("Welcome to the file manager 3!")
	print("I can't believe it... my file manager got pwned TWICE already.\nSeriously, how did you guys even do that?\n")
	print("Anyway, I've fixed everything this time.\nThere's now a proper permission authentication system, and deleted flag.txt at very start,\nso you definitely can't access files you shouldn't. :)\n")
	print("Also, great news!\nThe backup restore feature is finally here (beta version)!")
	print("Enjoy the new version!\n")

	print("Hint 1: Is there any difference in 'check_filename' function?")
	print("Hint 2: You may want to see the 'Dockerfile' first\n")

def banner():
	print("="*30)
	print("Welcome to the file manager!")
	print("="*30)

check_filename = lambda fn, files: any(c in fn for c in " /\\:*?\"<>|") or len(fn) > 255 or os.path.basename(fn) in files
file_exists = lambda fn: os.path.exists(fn)

ROOT_UID = 0
ROOT_GID = 0
CTF_UID = 1000
CTF_GID = 1000

is_root = False

def drop_priv():
    global is_root
    os.setresgid(CTF_GID, CTF_GID, ROOT_GID)
    os.setresuid(CTF_UID, CTF_UID, ROOT_UID)
    is_root = False

def restore_priv():
    global is_root
    os.setresuid(ROOT_UID, ROOT_UID, CTF_UID)
    os.setresgid(ROOT_GID, ROOT_GID, CTF_GID)
    is_root = True

def readfile(fn):
	if check_filename(fn, [""]): print("Please enter a valid filename without spaces or special characters, and less than 255 characters"); return 1
	if check_filename(fn, ["backup.tar"]):
		print("Backup file is not a text file and cannot be read!"); return 1
	print(f"[*] Auditing access to {fn}...")
	time.sleep(0.1)
	if not file_exists(fn):
		print("File does not exist!")
		return 1
	else:
		with open(fn, "r") as f:
			print("Here is the content of the file:")
			print(f.read())
		
def get_hash(filename):
	sha256 = hashlib.sha256
	file = open(filename, "rb").read()
	return sha256(file)
		
def calhash(fn):
	if not file_exists(fn):
		print("File does not exist!")
		return 1
	else:
		print("Calculating hash...")
		print("The hash of the file is: " + str(get_hash(fn).hexdigest()))

def create_file_banner():
	print("You will be asked for line (<=10), text and filename. The text will be written into the file for the number of lines you specified.")
	print("For example, if you enter 3 for line, and 'hello' for text, and 'text.txt' for filename, the file 'text.txt' will contain:")
	print("hello")
	print("hello")
	print("hello")
	print("And remember, the filename should not contain any spaces or special characters such as '/', '\\', ':', '*', '?', '\"', '<', '>', '|'.")
	print("And the filename should not be too long (less than 255 characters).")
	print("Also, it can't be 'main.py' or 'flag.txt' to avoid breaking the program.")
	print("Caution: If you create a file with the same name as an existing file, it will overwrite the existing file!")

def createfile():
	create_file_banner()
	line = input("line: ")
	if not line.isdigit() or int(line) <= 0:
		print("Please enter a valid positive integer for line.")
		print("File creation failed!")
		return 1
	elif int(line) > 10:
		print("Please enter a smaller number for line (less than 10).")
		print("File creation failed!")
		return 1
	else:
		line = int(line)
	text = ""
	for i in range(line):
		text += input(f"line {i+1}: ") + "\n"
	while True:
		filename = input("filename: ")
		if check_filename(filename, ["main.py", "flag.txt"]):
			print("Please enter a valid filename without spaces or special characters, and less than 255 characters, and not 'main.py' or 'flag.txt'.")
		else:
			break
	with open(filename, "w") as f:
		f.write(text)
		print("File created successfully!")

def backup():
	print("Creating backup...")
	if file_exists("backup.tar"):
		print("Backup file already exists, it will be overwritten!")
		os.remove("backup.tar")
	try:
		subprocess.run(["tar", "-cf", "backup.tar", "--exclude=flag.txt", "--exclude=main.py", "--", "."])
		print("Backup created successfully!")
	except Exception as e:
		print(f"An error occurred while creating backup: {e}")

def restore():
	ch = input("Are you sure? this might replace existed files? type \"yes\" to continue: ")
	if not ch.lower() == "yes": return 1
	print("Restoring backup...")
	if not file_exists("backup.tar"):
		print("Backup file does not exist!")
		return 1
	try:
		subprocess.run(["tar", "-xf", "backup.tar"])
		print("Backup restored successfully!")
	except Exception as e:
		print(f"An error occurred while restoring backup: {e}")

def run():
	global is_root
	auth = open("flag.txt", "r")
	os.remove("flag.txt")
	drop_priv()
	while True:
		banner()
		print("1. read file")
		print("2. calculate hash")
		print("3. create file")
		print("4. backup (Won't backup flag.txt, main.py)")
		print("5. restore backup (beta)")
		print("6. Get root" if is_root == False else "6. Drop priv.")
		print("999. exit")
		ch = input(">> ")
		if ch == "1":
			fn = input("filename: ")
			readfile(fn)
		elif ch == "2":
			fn = input("filename: ")
			calhash(fn)
		elif ch == "3":
			createfile()
		elif ch == "4":
			backup()
		elif ch == "5":
			restore()
		elif ch == "6":
			if is_root == False:
				auth_key = input("Enter the whole flag as the auth key >> ")
				auth.seek(0)
				if auth_key == auth.read(): restore_priv(); print("You're now root!")
				else: print("auth key error.")
			else:
				drop_priv()
		elif ch == "999":
			print("Thank you for using the file manager!")
			break


if __name__ == "__main__":
	init()
	new_welcome()
	run()

# Bonus question: What unexpected solution would occur if auth.seek(0) were not used?