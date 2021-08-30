def print_triangle(height):
    # Each level of the triangle
    for level in range(1, height + 1):
        line = ''
        # Print the spaces to the left
        for _ in range(height - level):
            line += ' '
        # Print the stars
        for _ in range(1, level):
            line += '*'
        # Add the last * without a space
        line += '*'
        # Move to the next level
        print(line)


def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    print_triangle(height)


if __name__=='__main__':
    main()
