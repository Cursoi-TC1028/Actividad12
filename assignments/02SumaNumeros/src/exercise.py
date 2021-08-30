def main():
    #escribe tu código abajo de esta línea
    num = int(input())
    sum = 0
    while num != 0:
        sum = sum + num
        #print("Dame otro")
        num = int(input())
    print(sum)


if __name__=='__main__':
    main()
