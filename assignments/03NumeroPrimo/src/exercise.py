def NumeroPerfecto(num):
        suma = 0
        for i in range(1,num):
            if (num % i == 0):
                suma += i
        
        if num == suma:
            return True
        else:
            return False

def main():
    #escribe tu código abajo de esta línea
    num = int(input())
    
    if NumeroPerfecto(num):
        print("El número es perfecto")
    else:
        print("El NO es número perfecto")

if __name__=='__main__':
    main()
