def main():
    #escribe tu código abajo de esta línea
    amount = int(input())
    total = 0
    counter = 0
    while counter < amount:
        total += float(input())
        counter += 1
    average = total / amount
    print(average)

if __name__=='__main__':
    main()
