# Container With Most Water

## Enunciado

Dado un arreglo de números enteros positivos, donde cada elemento representa la altura de una línea vertical en el eje x, encuentra dos líneas que, junto con el eje x, formen un contenedor capaz de almacenar la mayor cantidad de agua posible. La cantidad de agua está limitada por la altura más baja de las dos líneas y la distancia entre ellas. Devuelva la cantidad máxima de agua que puede almacenar un contenedor teniendo en cuenta que no puede inclinar el contenedor.

## Ejemplo
<p align="left">
    <img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" alt="Diagrama que ilustra el problema Container With Most Water" style="max-width: 400px; width: 100%; height: auto;">
</p>

Input: [1,8,6,2,5,4,8,3,7]

Output: 49

Explicación: las líneas verticales anteriores están representadas por la matriz [1,8,6,2,5,4,8,3,7]. En este caso, el área máxima de agua (sección azul) que puede contener el contenedor es 49.


## Solución

La solución consiste en usar dos punteros, uno al inicio y otro al final del arreglo, e ir moviéndolos hacia el centro, siempre eligiendo el lado con menor altura, calculando el área en cada paso y guardando el máximo encontrado.

Consulta el archivo `solucion.py` para ver la implementación en Python.
