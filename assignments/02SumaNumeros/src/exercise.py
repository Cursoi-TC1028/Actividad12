def main():
    #escribe tu código abajo de esta línea
    cont=1
    acum=0
    num = int(input())
    acum+=num
    while( acum <= 1000 ):
        num = int(input())
        acum+=num
        cont+=1

    print("suma =",acum)
    print("cantidad de números =",cont)

if __name__=='__main__':
    main()
