import os
# Подключение функционала в языке Питон
import psutil
import sys

print("It`s possible to be winner for long live in Russia")
print("hellow")
name = input("Your name: ")
print(name, ", welcome!")

answer = input("Do u wont get stat? (Y/N)")

if answer == "Y":
	print("Good job MAN!")
	print("First! I can tolk with u about any theme!")
	print("Second! I can teaching u for same new lang!")
	print("And Third! I can just listining to u!")
	print("Dirictory file 4")
	print("windows version 5")
	print("Process list 6")
	print(" 7")
	print("of what kind of filesystemcoding ur file? 8")
	print("Where ur file now? 9")
	print("ur OS is? 10")

	kind = int(input("print the number"))

	if kind == 1:
		print("Maby we r doing somthing more?")
	elif kind == 2:
		print("I know more then 100 leng")
	elif kind == 3:
		print("U r boring!")
	elif kind == 4:
		print(os.listdir())
		#os.listdir() показывает файлы внутри дериктории, где сейчас ведете работу
	elif kind == 5:
		print(sys.getwindowsversion())
		#sys.getwindowsversion() выводит версию windows
	elif kind == 6:
		print(psutil.pids())
		#psutil.pids выводит список процессов
	elif kind == 7:
		print(sys.stdout())
	elif kind == 8:
		print(sys.getfilesystemencoding())
		#coding in file system
	elif kind == 9:
		print(os.getcwd())
		#way of dirictory listing file
	elif kind == 10:
		print(sys.platform())
	else:
		pass
	


elif answer == "N":
	print(name, "fuck u")
else:
	print(name, ",fuck u")