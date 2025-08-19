print("Ejercicio 1 \n")

print("1. Resuelve el siguiente problema utilizando las herramientas aprendidas en el módulo. \n")

print("Tomás rindió 3 exámenes y desea saber su promedio a partir de esta información: ")


nota_uno=10
nota_dos=6
nota_tres=8

promedio=(nota_uno+nota_dos+nota_tres)/3

print(f"El promedio es: {promedio}\n")

print("Ejercicio 2 \n")

print("1. Calcula los minutos que hay en una semana declarando variables.")

minutos_por_hora=60
horas_por_dia=24
dias_por_semana=7

minutos_por_semana=minutos_por_hora*horas_por_dia*dias_por_semana

print(f"En una semana hay {minutos_por_semana} minutos\n")

print("2. Dada esta situación: Una juguetería tiene mucho éxito en la venta de dos de sus productos: payasos y muñecas. Suele hacer ventas por correo y la empresa de logísticales cobra por el peso de cada paquete, por lo quenecesitan calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca, 75 g.")

peso_payaso=112
peso_muñeca=75

print("Escribe un programa que: Solicite al usuario el número de payasos y muñecas vendidos en el último pedido. Calcule el peso total del paquete que será enviado.")

cantidad_payasos=int(input("Ingrese la cantidad de payasos vendidos: "))
cantidad_muñecas=int(input("Ingrese la cantidad de muñecas vendidas: "))

peso_total=peso_payaso*cantidad_payasos+peso_muñeca*cantidad_muñecas

print(f"El peso total del paquete es: {peso_total} g\n")


