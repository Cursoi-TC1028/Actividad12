def main():
    #escribe tu código abajo de esta línea
    """
    Program to print all the numbers from 1 until a limit entered by the user.
    Basic exercise using while loops

    Gilberto Echeverria
    g.echeverria@tec.mx
    """

    limit = int(input())
    counter = 1
    while counter <= limit:
        print(counter)
        counter = counter + 1

if __name__=='__main__':
    main()
