def main():
    #escribe tu código abajo de esta línea
    numero = int(input())
    suma = 0

    for i in range(1, numero+1):
        suma = suma + i
    print(suma)

if __name__=='__main__':
    main()
