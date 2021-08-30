def russian_multiplication(factor1, factor2):
    # Initialize the resulting sum
    result = 0
    while factor2 >= 1:
        print(f"{factor1} {factor2}")
        if factor2 % 2 != 0:
            result += factor1
        factor1 *= 2
        factor2 //= 2
    return result


def main():
    factor1 = int(input("Enter factor 1: "))
    factor2 = int(input("Enter factor 2: "))
    #escribe tu código abajo de esta línea
    if factor1 >= 0 and factor2 >= 0:
        print(russian_multiplication(factor1, factor2))
    else:
        print("Invalid input")


if __name__=='__main__':
    main()
