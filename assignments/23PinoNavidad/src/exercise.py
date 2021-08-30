def print_tree(height):
    level = 1
    # Each level of the tree
    while level <= height:
        line = ''
        # Print the spaces to the left
        spaces = height - level
        while spaces > 0:
            line += ' '
            spaces -= 1
        # Print the stars
        count = 1
        while count < level:
            line += '* '
            count += 1
        # Add the last * without a space
        line += '*'
        # Move to the next level
        print(line)
        level += 1


def main():
    height = int(input("Enter tree height: "))
    #escribe tu código abajo de esta línea
    print_tree(height)


if __name__=='__main__':
    main()
