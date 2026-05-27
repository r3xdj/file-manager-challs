#!/usr/bin/env python3
import os, sys

def init():
	sys.stdout.reconfigure(line_buffering=True)
	sys.stderr.reconfigure(line_buffering=True)
	os.system("stty -echo")

def Welcome():
	print("Welcome to the file manager!")
	print("You can read files, calculate their hash, and create new files.")
	print("Please be careful when creating files, as it may overwrite existing files.")
	print("Enjoy!")

def banner():
	print("="*30)
	print("Welcome to the file manager!")
	print("="*30)

check_filename = lambda fn, files: any(c in fn for c in " /\\:*?\"<>|") or len(fn) > 255 or os.path.basename(os.path.realpath(fn)) in files
file_exists = lambda fn: os.path.exists(fn)

def readfile(fn):
	if check_filename(fn, ["flag.txt"]):
		print("Please enter a valid filename without spaces or special characters, and less than 255 characters, and not 'flag.txt'.")
		return 1
	if not file_exists(fn):
		print("File does not exist!")
		return 1
	else:
		with open(fn, "r") as f:
			print("Here is the content of the file:")
			print(f.read())
		
def get_hash(filename):
	import hashlib
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

def run():
	while True:
		banner()
		print("1. read file")
		print("2. calculate hash")
		print("3. create file")
		print("4. exit")
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
			print("Thank you for using the file manager!")
			break
		print()


if __name__ == "__main__":
	init()
	Welcome()
	run()