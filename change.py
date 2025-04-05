def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()
    print("Vuelto")
    print()
    cambio_total = (money-expense)
    pesos = (int(cambio_total))
    print("Pesos:")
    print(pesos)
    centavos = ((cambio_total-pesos) * 100)
    print("Centavos:")
    print(int(centavos))
