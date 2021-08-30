def print_letter_pyramid(height):
    # Each level of the pyramid
    for level in range(1, height + 1):
        line = ''
        # Print the spaces to the left
        for spaces in range(height - level):
            line += '  '
        # Print the letters from A
        for index in range(level - 1):
            line += chr(ord('A') + index) + ' '
        # Print letters down to B
        for index in range(level - 1, 0, -1):
            line += chr(ord('A') + index) + ' '
        # Add the last 'A' without a space
        line += 'A'
        # Move to the next level
        print(line)


def main():
    height = int(input("Enter pyramid height: "))
    #escribe tu código abajo de esta línea
    if height < 1 or height > 26:
        print("Out of range")
    else:
        print_letter_pyramid(height)


if __name__=='__main__':
    main()
