/* c_optimizado.c
   Versión: 2.0.0
   Ejemplo optimizado: código más claro, compacto y eficiente
   Por qué es más eficiente y mejor:
	- else if evita if anidados y reduce comparaciones.
	- ++ es más natural y puede ser más eficiente que x = x + 1.
	- Guardar numeros[i] en v evita leer el arreglo varias veces.
	- Código más claro y fácil de extender o modificar

*/

#include <stdio.h>                      // para printf

int main() {
    int numeros[] = {3, -1, 0, 5, -7, 0, 2};  // arreglo de enteros
    int n = 7;                          // cantidad de elementos

    int positivos = 0;                  // contador de números > 0
    int negativos = 0;                  // contador de números < 0
    int ceros = 0;                      // contador de números == 0

    for (int i = 0; i < n; i++) {       // recorrer el arreglo
        int v = numeros[i];             // copiar valor a variable local

        if (v > 0) {                    // si el valor es mayor que cero
            positivos++;                // incrementar positivos (operador ++)
        } else if (v < 0) {             // si no, pero es menor que cero
            negativos++;                // incrementar negativos
        } else {                        // en cualquier otro caso (v == 0)
            ceros++;                    // incrementar ceros
        }
    }

    printf("Positivos: %d\n", positivos); // imprimir cantidad de positivos
    printf("Negativos: %d\n", negativos); // imprimir cantidad de negativos
    printf("Ceros: %d\n", ceros);         // imprimir cantidad de ceros

    return 0;                           // fin del programa
}