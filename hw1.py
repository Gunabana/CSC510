def execute(inp):
    arr = []
    # if (inp == ("Y" or "y")):
    if inp in ("Y", "y"):
        arr[-1]	# error here
    # elif (inp == ("N" or "n")):
    elif inp in ("N", "n"):
        print("Okay, that is smart. Shutting down.")
    else:
        print("Invalid input. Shutting down.")

if __name__ == "__main__":
    print("Hey, I heard you want to download a virus!")
    execute(input("Do you want a virus? (Y/n)\n>"))