

def main():
    n = int(input("Escribe un numero entero no negativo para calcular su factorial: "))
    if ( n < 0):
        print("Factorial no definido para negativos")
    else:
        fact = 1
        for x in range(2,n+1):
            fact = fact * x
        print(fact)


if __name__=='__main__':
    main()
