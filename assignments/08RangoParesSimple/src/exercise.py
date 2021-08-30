def main():
    #escribe tu código abajo de esta línea
    a = int(input())
    b = int(input())
    if a % 2 != 0 :
        a = a + 1
    while (a <= b) :
        print(a)
        a = a + 2

if __name__=='__main__':
    main()
