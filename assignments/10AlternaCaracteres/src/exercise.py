def main():
    #escribe tu código abajo de esta línea
    n = int(input())
    cont = 1
    while (cont <= n) :
        if cont % 2 != 0:
            print("#")
        else :
            print("%")
        cont += 1

if __name__=='__main__':
    main()
