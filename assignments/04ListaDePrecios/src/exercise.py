def main():
    total = 0
    clave = ' '
    while (clave != 'X') :
        clave = input("Teclea la clave ")
        if clave == "A":
            print(120)
            total += 120
        elif clave == "B" :
            print(250)
            total += 250
        elif clave == "C" :
            print(360)
            total += 360
    print(total)

if __name__=='__main__':
    main()
