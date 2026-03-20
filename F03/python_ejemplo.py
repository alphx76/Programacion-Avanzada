"""
Proyecto de ejemplo: Manejo de estructuras de datos en Python
Autor: (Tu nombre)
Versión: 1.0.0

Este programa demuestra el uso de:
- Listas
- Tuplas
- Diccionarios
- Sets

El objetivo es mostrar cómo almacenar, organizar y procesar datos
de una manera similar a como se haría en C, pero usando las
estructuras de alto nivel de Python.
"""

# -----------------------------
# 1. LISTAS
# -----------------------------

# Creamos una lista de números
numeros = [10, 20, 30, 40, 50]  # Lista modificable

# Agregamos un número al final
numeros.append(60)  # Ahora la lista es [10,20,30,40,50,60]

# Recorremos la lista con un ciclo for
print("Contenido de la lista 'numeros':")
for n in numeros:
    print(f"- {n}")

# -----------------------------
# 2. TUPLAS
# -----------------------------

# Una tupla representa datos que NO deben cambiar
coordenada = (12.5, 9.8)  # (x, y)

print("\nTupla 'coordenada':")
print(f"x = {coordenada[0]}, y = {coordenada[1]}")

# -----------------------------
# 3. DICCIONARIOS
# -----------------------------

# Diccionario que almacena información de un estudiante
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Electrónica"
}

# Acceso por clave
print("\nInformación del estudiante:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# Modificar un valor
estudiante["edad"] = 21  # Actualizamos la edad

# -----------------------------
# 4. SETS (CONJUNTOS)
# -----------------------------

# Un set elimina duplicados automáticamente
materias = {"Cálculo", "Física", "Programación", "Física"}  # "Física" repetida

print("\nMaterias inscritas (sin duplicados):")
for m in materias:
    print(f"- {m}")

# -----------------------------
# 5. PROCESAMIENTO COMBINADO
# -----------------------------

# Lista de calificaciones
calificaciones = [90, 85, 90, 70, 85, 100]

# Convertimos a set para ver valores únicos
calificaciones_unicas = set(calificaciones)

print("\nCalificaciones únicas:")
print(calificaciones_unicas)

# Diccionario que relaciona materia con calificación
boleta = {
    "Cálculo": 90,
    "Física": 85,
    "Programación": 100
}

print("\nBoleta del estudiante:")
for materia, cal in boleta.items():
    print(f"{materia}: {cal}")

# -----------------------------
# FIN DEL PROGRAMA
# -----------------------------
print("\nPrograma finalizado correctamente.")