

def main():
    numero = int(input("Escribe un numero : "))

    resultado = 1

    while( resultado*resultado <= numero ):
        resultado = resultado +1

    print(resultado)


if __name__=='__main__':
    main()
