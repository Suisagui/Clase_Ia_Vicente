# Taller de Pandas con Iris

Los nueve ejercicios están resueltos en [02_Ejercicios_Iris.ipynb](02_Ejercicios_Iris.ipynb), con el código, las salidas y una respuesta breve debajo de cada solución.

## Archivos

- iris_con_faltantes.csv: datos usados en los ejercicios, con 8 celdas vacías.
- iris_original.csv: datos completos para comparar.
- iris_procesado.csv: resultado del ejercicio 7, con longitud del pétalo en milímetros y código de especie.
- 01_Demostracion_Pinguinos.ipynb: material de referencia de la clase, conservado sin cambios.

## Abrir y ejecutar

Abre esta carpeta en VS Code con las extensiones de Python y Jupyter, selecciona un entorno de Python y ejecuta el cuaderno de Iris de arriba hacia abajo. Si faltan las dependencias, instala:

    python -m pip install pandas ipykernel

Los CSV deben permanecer al lado del cuaderno. El ejercicio 7 vuelve a generar iris_procesado.csv en esta carpeta.

El cuaderno de pingüinos requiere penguins_size.csv, que no venía entre los archivos de esta entrega. Su enlace de descarga aparece en la preparación del propio cuaderno. No es necesario para resolver Iris.

## Resultados

Hay 150 flores, 50 de cada especie. El filtro de virginica con pétalos mayores que 5.5 cm devuelve 25 filas. Virginica tiene el mayor promedio de longitud del pétalo: 5.552 cm.

Al eliminar filas incompletas quedan 142. El relleno del ejercicio 5 usa la mediana de sepal_width_cm, 3.0 cm, y solo modifica una copia. El CSV procesado conserva las 150 filas y los 8 faltantes porque se exporta la copia transformada del ejercicio 6.

La última celda comprueba los resultados y que iris siga igual que al inicio. Los CSV de entrada se conservaron sin cambios.
