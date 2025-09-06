import sys as sys


def analyze_text(text: str) -> None:
    """Count and display character statistics for the given text."""

    total_chars = 0
    upper_letters = 0
    lower_letters = 0
    punctuation_marks = 0
    space = 0
    digits = 0

    for char in text:
        total_chars += 1
        if char.isupper():
            upper_letters += 1
        elif char.islower():
            lower_letters += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digits += 1
        else:
            punctuation_marks += 1

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuation_marks} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")


def main():
    """takes a single string argument and displays the sums of its chars"""
    if len(sys.argv) == 1:
        text = sys.stdin.readline()
        analyze_text(text)
        return

    if (len(sys.argv) != 2):
        print("AssertionError: more or less than 1 argument.")
        return

    analyze_text(sys.argv[1])


if __name__ == "__main__":

    main()
