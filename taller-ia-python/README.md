# Ejercicios del taller

Las respuestas de los ejercicios 1 al 8 están en [el documento Word](Soluciones_bloques_A_y_B.docx). Los ejercicios 9 al 14 están en la carpeta [bloque_c](bloque_c), cada uno en su propio archivo.

## Ejecutar el bloque C

Abre una terminal en esta carpeta y elige uno de estos comandos:

```bash
python bloque_c/09_detector_saludo.py
python bloque_c/10_clasificador_tickets.py
python bloque_c/11_palabras_sospechosas.py
python bloque_c/12_sentimiento_basico.py
python bloque_c/13_repetir_hasta_salir.py
python bloque_c/14_palindromo.py
```

Ejecuta uno a la vez y escribe el texto que te pida. Se necesita Python 3, sin librerías adicionales.

## Reglas utilizadas

- **9 — Saludos:** busca “hola” o “buenas”, sin distinguir mayúsculas.
- **10 — Tickets:** “ayuda”, “problema” y “error” corresponden a Soporte; “precio”, “comprar” y “cotizar”, a Ventas. Si coinciden ambas categorías, gana Soporte porque se evalúa primero. Sin coincidencias, muestra Otro.
- **11 — Palabras sospechosas:** busca “gratis”, “premio”, “ganaste”, “urgente”, “haz clic” y “contraseña”. Cada término suma una sola vez: “premio premio” cuenta como 1.
- **12 — Sentimiento:** “feliz”, “excelente”, “bueno” y “genial” suman un punto cada una; “triste”, “malo”, “terrible” y “horrible” restan uno. El resultado es positivo si el puntaje supera cero, negativo si es menor y neutral si queda en cero.
- **13 — Repetición:** sigue pidiendo mensajes hasta escribir “salir”. También acepta “SALIR” y espacios a los lados.
- **14 — Palíndromos:** invierte una palabra con un `for` y la compara con la original. “Reconocer” es un palíndromo; “python”, no. Ignora mayúsculas y espacios exteriores, conserva las tildes y avisa si no se escribe nada.

Como en los ejemplos de clase, `in` busca fragmentos de texto: “hola” también coincide dentro de “holanda”. El sentimiento se calcula solo con las palabras de las listas, por lo que no reconoce negaciones como “no estoy feliz”.

## Ejercicios guiados

En [guiados](guiados) están los cuadernos de clase y sus versiones finales en `.py`. Los cuadernos se abren en Jupyter y se ejecutan de arriba hacia abajo. Las instrucciones de Git se ejecutan en la terminal.

El clasificador revisa primero precio/cuesta, después ayuda/problema, luego hola y finalmente adiós/chao. El detector de spam clasifica el mensaje según su puntaje: 0 es normal, 1 o 2 es sospechoso y 3 o más es posible spam.

## Comprobaciones y avances

El [registro de pruebas](VERIFICACION.txt) contiene 39 comprobaciones: 8 de los bloques A y B y 31 del bloque C y los ejemplos guiados. Incluye mensajes vacíos, coincidencias entre categorías y la salida del bucle.

Los avances están guardados en el historial de Git. Desde una copia clonada, puedes revisar y guardar cambios con:

```bash
git status
git diff
git add .
git commit -m "Actualizar ejercicios"
git push
```

Revisa los archivos antes de ejecutar `git add .`. Para consultar el historial, usa `git log --oneline`.
