

def main():
    n = int(input("Escribe un numero entero : "))

    if n <= 1:
        val = False
    else:
        val = True

    for num in range (2,n-1):
        if n % num == 0:
            val = False

    print(val)

if __name__=='__main__':
    main()
