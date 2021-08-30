def fibonacci_at(index):
    # Base cases
    if index < 2:
        return index
    # Initialize the values
    a = 0
    b = 1
    pos = 1
    # Get each next element in the sequence
    while pos < index:
        a, b = b, a + b
        pos += 1
    return b


def main():
    index = int(input("Enter the index: "))
    #escribe tu código abajo de esta línea
    if index >= 0:
        print(fibonacci_at(index))
    else:
        print("Invalid input")


if __name__=='__main__':
    main()
