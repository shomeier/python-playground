if __name__ == '__main__':
    # oython program to demonstrate
    # string slicing

    # string slicing
    s = 'HelloWorld'

    # no params provided - orginal string
    print(s[:])
    print(s[::])

    # char at position
    print("\nChar at position:")
    print(s[3])

    # using indexing sequence
    print("\nUsing indexing sequence:")
    print(s[:3])
    print(s[1:5:2])
    print(s[-1:-12:-2])

    # prints string in reverse
    print("\nReverse String:")
    print(s[::-1])

    s1 = s[8:1:-1]
    print(s1)
