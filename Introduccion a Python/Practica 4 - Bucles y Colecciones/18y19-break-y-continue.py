# break y continue

#continue: salta a la siguiente iteración del bucle.
#break: aborta el bucle.

# Ejemplo de continue
for numero in range(10):
    if numero % 2 == 0:
        continue  # Si el número es par, salta a la siguiente iteración
    print(numero)  # Esto solo se ejecuta para números impares

# Ejemplo de break
for numero in range(10):
    if numero == 5:
        break  # Si el número es 5, termina el bucle
    print(numero)  # Esto se ejecuta para números del 0 al 4

# Ejemplo combinado de break y continue
for numero in range(10):
    if numero % 2 == 0:
        continue  # Si el número es par, salta a la siguiente iteración
    if numero == 7:
        break  # Si el número es 7, termina el bucle
    print(numero)  # Esto se ejecuta para números impares menores que 7 