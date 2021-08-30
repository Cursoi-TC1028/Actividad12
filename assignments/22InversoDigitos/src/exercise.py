def invert_digits(num):
    # Store the sign of the original number
    negative = num < 0
    # Make number positive
    num = abs(num)
    # Extract digits
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num //= 10
    # Restore the original sign
    if negative:
        result *= -1
    return result


def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    if num >= 1000000 or num <= -1000000:
        print("Too long")
    else:
        print(invert_digits(num))


if __name__=='__main__':
    main()
