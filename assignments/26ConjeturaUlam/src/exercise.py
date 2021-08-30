def hailstone_sequence(num):
    # Store the original number in the result
    result = str(num)
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        # Add the new number to the string
        result += " " + str(num)
    return result


def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    if num > 0:
        print(hailstone_sequence(num))
    else:
        print("Invalid input")


if __name__=='__main__':
    main()
