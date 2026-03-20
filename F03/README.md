# Proyecto: Estructuras de Datos en Python y su Equivalente en C  
## Instrucciones Generales para el Estudiante

Este repositorio contiene un ejemplo introductorio cuyo propósito es que practiques **listas, tuplas, diccionarios y sets en Python**, y luego reproduzcas **el mismo comportamiento en C**, donde estas estructuras no existen de forma nativa y deben simularse manualmente.

El objetivo es que entiendas cómo funcionan estas estructuras en un lenguaje de alto nivel (Python) y cómo se implementan de manera equivalente en un lenguaje de bajo nivel (C).

---

## 1. Archivos esperados en el repositorio

Cada integrante del equipo debe realizar al menos un commit significativo.

---

## 2. Objetivo del programa en Python

El archivo `python_ejemplo.py` demuestra:

- Uso de **listas** para almacenar y modificar colecciones de datos.
- Uso de **tuplas** para representar datos inmutables.
- Uso de **diccionarios** para almacenar pares clave–valor.
- Uso de **sets** para eliminar duplicados y trabajar con conjuntos.
- Impresión ordenada de resultados para que puedan compararse con la versión en C.

---

## 3. Objetivo del programa en C

El archivo `c_ejemplo.c` debe reproducir **la misma salida** que el programa en Python, pero implementando manualmente las estructuras:

### Listas → Arreglos
Debes usar un arreglo de enteros y simular operaciones como agregar elementos y recorrerlos.

### Tuplas → `struct` con dos valores
Debes crear un `struct` que represente una coordenada o un par de datos inmutables.

### Diccionarios → `struct` con campos
Debes crear un `struct` que contenga varios campos (por ejemplo: nombre, edad, carrera).

### Sets → Arreglo + función para eliminar duplicados
Debes implementar una función que recorra un arreglo y genere otro sin elementos repetidos.

---

## 4. Requisitos del programa en C

Tu programa debe:

- Imprimir la información en el **mismo orden** que el programa en Python.
- Usar:
  - Arreglos
  - `struct`
  - Funciones
  - Ciclos `for` y/o `while`
- Estar **comentado** explicando cada parte.
- Compilar correctamente con:
