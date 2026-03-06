# python_optimizado.py
# Versión: 2.0.0
# Ejemplo optimizado: código más claro, compacto y eficiente
# Por qué es más eficiente y mejor:
#   - elif evita if anidados y comparaciones extra.
#   - += es más idiomático y ligeramente más rápido que x = x + 1.
#   - Código más corto → menos errores, más fácil de leer y mantener.


numeros = [3, -1, 0, 5, -7, 0, 2]      # lista de enteros de ejemplo

positivos = 0                          # contador de números > 0
negativos = 0                          # contador de números < 0
ceros = 0                              # contador de números == 0

for n in numeros:                      # recorrer cada número de la lista
    if n > 0:                          # si el número es mayor que cero
        positivos += 1                 # sumar 1 a positivos (operador +=)
    elif n < 0:                        # si no, pero es menor que cero
        negativos += 1                 # sumar 1 a negativos
    else:                              # en cualquier otro caso (n == 0)
        ceros += 1                     # sumar 1 a ceros

print(f"Positivos: {positivos}")       # mostrar cantidad de positivos
print(f"Negativos: {negativos}")       # mostrar cantidad de negativos
print(f"Ceros: {ceros}")               # mostrar cantidad de ceros