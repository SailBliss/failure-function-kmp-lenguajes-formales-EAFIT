# Tarea 1 — Función Failure (Figura 3.19)
Esta tarea consiste en implementar el algoritmo de la figura 3.19 del libro para construir la función failure utilizada por el algoritmo KMP (Knuth–Morris–Pratt), y verificar los resultados solicitados en el ejercicio 3.4.3.
---
## Entorno de desarrollo
* Sistema operativo: Windows
* Lenguaje: Python 3.13.7
* Librerías externas: Ninguna
---
## Fundamento teórico
La función "f(s)" se define como:
-> La longitud del prefijo propio más largo de "b1…bs" que también es sufijo de "b1…bs".
Para cada posición "s" del patrón, buscamos el mayor borde (longest border) del prefijo considerado.
Esta función es fundamental en KMP porque permite que, si sucede un mismatch, el algoritmo no se reinicia desde cero, sino que conserve la mayor coincidencia posible que ya fue validada.
---

## Proceso seguido
1. Estudiar definición formal de prefijo, sufijo y prefijo propio.
2. Realicar el cálculo manual de los ejemplos del ejercicio para entender cómo se obtiene cada valor de "f(s)".
3. Traducír la Figura 3.19 a pseudocódigo respetando el orden de pasos del libro.
4. Implementé el algoritmo en Python manteniendo la misma estructura lógica:

   * Inicialización `t = 0`
   * Asignación `f(1) = 0`
   * Ciclo `for` sobre `s`
   * Ciclo `while` para retroceso con `t = f(t)`
   * Actualización de `f(s+1)`

---
## Verificación de resultados
Se probaron los tres patrones indicados en el Exercise 3.4.3:
* `abababaab`
* `aaaaaa`
* `abbaabb`
Los resultados obtenidos por el programa coinciden exactamente con los cálculos realizados manualmente:

<img width="1671" height="683" alt="image" src="https://github.com/user-attachments/assets/4f29f717-d3ed-4e2b-a7b3-103b6115b81b" />


```
palabra: abababaab
s:    1  2  3  4  5  6  7  8  9
f(s)  0  0  1  2  3  4  5  1  2
--------------------------------------------------
palabra: aaaaaa
s:    1  2  3  4  5  6
f(s)  0  1  2  3  4  5
--------------------------------------------------
palabra: abbaabb
s:    1  2  3  4  5  6  7
f(s)  0  0  0  1  1  2  3
--------------------------------------------------
```
Esto confirma que la implementación reproduce correctamente el comportamiento descrito en la Figura 3.19.
---

## Ejecución
En la carpeta del proyecto ejecutar:

```bash
python failure.py
```

El programa imprime las tablas correspondientes a cada palabra.
