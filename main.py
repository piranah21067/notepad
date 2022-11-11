
print("------welcome to notepad-------")

while True:
	print(" ")
	print("1-write note")
	print("2-read previous notes")
	print("3-delete previous notes")
	print("4-exit the program")
	option=input("enter your option here:")
	if option == "1":
		note=input("enter your note here:")
		save=input("would you like to save the note?:")
		if save=="yes" or "Yes":
			file=open("notes.txt","a")
			file.write(f"\n {note}")
			file.close()
			print("your note has been saved")
		else:
			print("your note was not saved")
	elif option=="2":
		file=open("notes.txt","r")
		prevNotes=file.read()
		file.close()
		print(prevNotes)
	elif option=="3":
		file=open("notes.txt","w")
		file.write("")
		file.close()
		print("all notes have been deleted")
	elif option=="4":
		break
	else:
		print("your input was invalid")