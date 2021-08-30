def main():
    #escribe tu código abajo de esta línea
    n = int(input("ingresa un numero"))
    cont = 1
    while (cont <= n) :
        if cont % 2 != 0:
            print(f"{cont}-#")
        else :
            print(f"{cont}-%")
        cont += 1

if __name__=='__main__':   
    main()
