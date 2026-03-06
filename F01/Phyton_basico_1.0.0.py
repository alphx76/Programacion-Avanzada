# python_basico.py
# Versión: 1.0.0
# Ejemplo básico con if/else y bucles (no optimizado)
# Funciona, pero los if anidados y x = x + 1 hacen el código más largo y menos claro.


numeros = [3, -1, 0, 5, -7, 0, 2]      # lista de enteros de ejemplo

positivos = 0                          # contador de números > 0
negativos = 0                          # contador de números < 0
ceros = 0                              # contador de números == 0

for n in numeros:                      # recorrer cada número de la lista
    if n > 0:                          # si el número es mayor que cero
        positivos = positivos + 1      # incrementar contador de positivos
    else:                              # si no es mayor que cero
        if n < 0:                      # verificar si es menor que cero
            negativos = negativos + 1  # incrementar contador de negativos
        else:                          # si no es mayor ni menor, es cero
            ceros = ceros + 1          # incrementar contador de ceros

print("Positivos:", positivos)         # mostrar cantidad de positivos
print("Negativos:", negativos)         # mostrar cantidad de negativos
print("Ceros:", ceros)                 # mostrar cantidad de ceros