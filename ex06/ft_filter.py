def ft_filter(function, iterable):
    """Custom implementation of the filter function."""

    if function is None:
        function = bool

    return iter([item for item in iterable if function(item)])


def is_even(num): return num % 2 == 0


def main():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(ft_filter(is_even, my_list)))


if __name__ == "__main__":
    main()
