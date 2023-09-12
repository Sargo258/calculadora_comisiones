nombre = input("ingresa tu nombre ")
ventas_mes = input("ingresa el numero de ventas realizadas por ti este mes : ")
ventas = int(ventas_mes)
comision = ventas * 13 / 100
print(f"Hola {nombre}, en el mesa has realizado: {ventas_mes} ventas, tu comision sera de: ${round(comision,2)}")