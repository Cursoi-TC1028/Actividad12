def main():
    cantidad = float(input("Escribe la cantidad de dinero inicial : "))
    porcentaje = int(input("Escribe el porcentaje de interes anual : "))
    if cantidad>0 and porcentaje>0:
        mensual = porcentaje/12/100
        final=cantidad
        for i in range(12):
            final = final * (1 + mensual)
        print(f"{final:.2f}")
    else:
        print("Error en los datos")

if __name__=='__main__':
    main()
