def main():
    #escribe tu código abajo de esta línea
    total = 0
    number = 0
    amount = 0
    while number >= 0:
        number = float(input())
        if number >= 0:
            total += number
            amount += 1
    average = total / amount
    print(average)

if __name__=='__main__':
    main()
