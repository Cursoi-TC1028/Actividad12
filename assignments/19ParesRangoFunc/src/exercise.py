
def pares_rango(lim_inf, lim_sup):

    if (lim_sup == lim_inf and lim_sup % 2 == 1):
        print("No hay pares")
    else:
        if (lim_sup < lim_inf):
            temp = lim_sup
            lim_sup = lim_inf
            lim_inf = temp

        if (lim_inf % 2 == 1):
            lim_inf += 1

        for  x in range(lim_inf, lim_sup+1, 2):
            print(x)


def main():
    lim_inf = int(input("Valor 1: "))
    lim_sup = int(input("Valor 2: "))
    pares_rango(lim_inf, lim_sup)


if __name__=='__main__':
    main()
