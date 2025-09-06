import sys as sys
import ft_filter as ft


def main():
    """Filter words longer than N from the given text."""
    if (len(sys.argv) == 1):
        print("AssertionError: the arguments are bad")
        return

    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
        return

    try:
        nbr = int(sys.argv[2])
        text = sys.argv[1]
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    list_str = text.split()
    x = ft.ft_filter(lambda a: len(a) > nbr, list_str)
    print(list(x))


if __name__ == "__main__":
    main()
