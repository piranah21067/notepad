
print("------welcome to notepad-------")

while True:
	print(" ")
	print("1-Write note")
	print("2-Read previous notes")
	print("3-Delete previous notes")
	print("4-Exit the program")
	option=input("Enter your option here:")
	if option == "1":
		note=input("Enter your note here:")
		save=input("Would you like to save the note?:")
		if save=="yes" or "Yes":
			file=open("notes.txt","a")
			file.write(f"\n {note}")
			file.close()
			print("Your note has been saved")
		else:
			print("Your note was not saved")
	elif option=="2":
		file=open("notes.txt","r")
		prevNotes=file.read()
		file.close()
		print(prevNotes)
	elif option=="3":
		file=open("notes.txt","w")
		file.write("")
		file.close()
		print("All notes have been deleted")
	elif option=="4":
		break
	else:
		print("Your input was invalid")

print("Thank you for using the programme")