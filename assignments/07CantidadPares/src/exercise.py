def main():
    #escribe tu código abajo de esta línea
    numero = int(input())

    totalPares = 0
    while (numero >= 0):
        if (numero % 2 == 0):
            totalPares += 1
        numero = int(input())
        
    print (f"Total de pares={totalPares}")

if __name__=='__main__':
    main()
