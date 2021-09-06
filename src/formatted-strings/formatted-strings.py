def print_full_name(first, last):
    # print("Hello ", first, " ", last, "! You just delved into python.", sep="")
    # print("Hello %s %s! You just delved into python." % (first, last))

    # https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
    # formatted string literals (f-strings)
    # print(f"Hello {first} {last}! You just delved into python.")

    # str.format
    # print("Hello {} {}! You just delved into python.".format(first, last))
    print("Hello {0} {1}! You just delved into python.".format(first, last))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)