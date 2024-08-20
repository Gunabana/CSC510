arr = []
print("Hey, I heard you want to download a virus!")
inp = input("Do you want a virus? (Y/n)\n>")
if (inp == ("Y" or "y")):
    arr[-1]	# error here
elif (inp == ("N" or "n")):
    print("Okay, that is smart. Shutting down.")
    exit()
else:
    print("Invalid input. Shutting down.")