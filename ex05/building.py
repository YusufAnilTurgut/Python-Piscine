import sys as sys


def main():
    if (len(sys.argv) == 1):
        print("AssertionError: argument is missing.")
        return

    if (len(sys.argv) != 2):
        print("AssertionError: more or less than 1 argument.")
        return

    totalChars = 0
    upperLetters = 0
    lowerLetters = 0
    punctuationMarks = 0
    space = 0
    digits = 0

    for char in sys.argv[1]:
        totalChars += 1
        if char.isupper():
            upperLetters += 1
        elif char.islower():
            lowerLetters += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digits += 1
        else:
            punctuationMarks += 1

    print(f"The text contains {totalChars} characters:")
    print(f"{upperLetters} upper letters")
    print(f"{lowerLetters} lower letters")
    print(f"{punctuationMarks} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":

    main()
