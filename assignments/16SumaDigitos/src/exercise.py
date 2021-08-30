

def main():
    s=0
    n=int(input("Escribe un numero entero: "))
    if n < 0:
        n*=-1
    while n>0:
        #print(n%10)
        s=s+n%10
        n=n//10
    print(s)


if __name__=='__main__':
    main()
