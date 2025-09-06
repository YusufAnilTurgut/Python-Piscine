import sys as sys

def main():

	if (len(sys.argv) == 1):
		return


	if (len(sys.argv) != 2):
		print("AssertionError: more or less than 1 argument.")
		return

	try:
		nbr = int(sys.argv[1])
	except:
		print("AssertionError: argument is not an integer")
		return


	if (nbr % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")


if __name__ == "__main__":
    main()
