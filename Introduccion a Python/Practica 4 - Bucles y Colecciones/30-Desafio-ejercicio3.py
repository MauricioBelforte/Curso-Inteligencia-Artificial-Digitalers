""" 
Ejercicio 3

1. Lee la siguiente situacion problematica:
Un empleado cobro 300 dolares por mes desde
enero a junio, 500 dolares de julio a octubre, y
700 dolares por mes en noviembre y en
diciembre.

2. Crea un programa que calcule el sueldo
promedio y que indique si este empleado esta
cobrando un sueldo bajo, normal o mejor de lo
normal.
* Sueldo bajo: por debajo de 300 dolares.
* Sueldo normal: entre 300 a 900.
* Sueldo mejor de lo normal: mas de 900 dolares. 
"""

sueldo_enero_junio = 300
sueldo_julio_octubre = 500
sueldo_noviembre_diciembre = 700
sueldo_total = (sueldo_enero_junio * 6) + (sueldo_julio_octubre * 4) + (sueldo_noviembre_diciembre * 2)
sueldo_promedio = sueldo_total / 12
print(f"Sueldo promedio: {sueldo_promedio} dólares")
if sueldo_promedio < 300:
    print("Sueldo bajo")
elif 300 <= sueldo_promedio <= 900:
    print("Sueldo normal")
else:
    print("Sueldo mejor de lo normal")
    