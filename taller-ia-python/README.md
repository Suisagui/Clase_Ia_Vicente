# Taller de Python

Aquí están las soluciones del banco práctico y los ejemplos guiados de la clase. Los ejercicios avanzan desde leer condiciones y bucles hasta escribir programas que reciben un mensaje y responden según reglas sencillas.

## Por dónde empezar

Para revisar las respuestas, abre el [Word de los bloques A y B](Soluciones_bloques_A_y_B.docx). Incluye los ejercicios 1 al 8 y explica cómo se obtiene cada salida.

Para probar el código, entra a [bloque_c](bloque_c). Cada archivo resuelve un ejercicio del 9 al 14 y funciona de forma independiente. En [guiados](guiados) también están los dos cuadernos de referencia y sus programas finales.

## Ejecutar los ejercicios

Necesitas Python 3. Abre una terminal dentro de esta carpeta y ejecuta el archivo que quieras probar:

```bash
python bloque_c/09_detector_saludo.py
python bloque_c/10_clasificador_tickets.py
python bloque_c/11_palabras_sospechosas.py
python bloque_c/12_sentimiento_basico.py
python bloque_c/13_repetir_hasta_salir.py
python bloque_c/14_palindromo.py
```

Ejecuta una línea a la vez. El programa te pedirá un texto y mostrará el resultado en la misma terminal. No necesitas instalar librerías adicionales para estos archivos.

Los cuadernos `.ipynb` se abren en Jupyter y sus celdas se ejecutan de arriba hacia abajo. Los comandos de Git que aparecen como instrucciones se escriben en una terminal, no en una celda de Python.

## Qué hace cada programa

### Ejercicio 9 · Detector de saludo

Busca “hola” o “buenas” en el mensaje. Si encuentra alguna de las dos, muestra “Saludo detectado”; de lo contrario, “Sin saludo”. Reconoce las palabras aunque estén escritas en mayúsculas.

### Ejercicio 10 · Clasificador de tickets

Usa estas palabras para decidir la categoría:

- **Soporte:** ayuda, problema o error.
- **Ventas:** precio, comprar o cotizar.
- **Otro:** cuando no aparece ninguna de las anteriores.

Si un mensaje incluye palabras de ambas categorías, se clasifica como Soporte porque esa condición se revisa primero. Por ejemplo, “tengo un problema con el precio” queda en Soporte.

### Ejercicio 11 · Palabras sospechosas

Recorre la lista “gratis”, “premio”, “ganaste”, “urgente”, “haz clic” y “contraseña”. Suma un punto por cada término encontrado.

Cada término cuenta una sola vez, aunque se repita. Por eso, “premio premio” da 1 y “ganaste un premio urgente” da 3.

### Ejercicio 12 · Sentimiento básico

Las palabras “feliz”, “excelente”, “bueno” y “genial” suman un punto cada una. “Triste”, “malo”, “terrible” y “horrible” restan un punto cada una.

Un puntaje mayor que cero se clasifica como Positivo; menor que cero, como Negativo; y cero, como Neutral. Si el mensaje contiene “feliz” y “triste”, ambas se compensan y el resultado es Neutral. Si no encuentra ninguna palabra de las listas, también queda en Neutral.

### Ejercicio 13 · Repetir hasta salir

Pide mensajes y los muestra en pantalla hasta que escribas “salir”. La orden también funciona con mayúsculas o espacios a los lados, como “ SALIR ”.

### Ejercicio 14 · Palíndromo

Recibe una palabra, construye su versión invertida con un bucle `for` y compara ambas. Por ejemplo, “reconocer” es un palíndromo y “python” no lo es.

Ignora las mayúsculas y los espacios exteriores. Conserva las tildes y avisa si la entrada está vacía. Está pensado para una sola palabra.

## Los ejemplos guiados

El **clasificador de intención** revisa primero “precio” o “cuesta”, después “ayuda” o “problema”, luego “hola” y finalmente “adiós” o “chao”. Se queda con la primera coincidencia.

El **detector de spam** suma un punto por cada término sospechoso encontrado. Con 0 puntos muestra “Mensaje normal”; con 1 o 2, “Mensaje sospechoso”; y con 3 o más, “Posible spam”.

En la primera guía aparece el comando `wd`. Para consultar la carpeta actual, puedes usar `Get-Location` en PowerShell o `pwd` en Bash.

## Qué tener en cuenta al probarlos

El operador `in` busca un fragmento de texto, no necesariamente una palabra completa. Por eso “hola” también aparece dentro de “holanda”.

El análisis de sentimiento tampoco reconoce negaciones ni ironía: “no estoy feliz” suma por la palabra “feliz”. Estas limitaciones ayudan a entender qué puede resolver una regla sencilla y cuándo haría falta un análisis más completo.

Se comprobaron **39 casos**: 8 de los bloques A y B y 31 de los programas del bloque C y los ejemplos guiados. Los resultados están en [VERIFICACION.txt](VERIFICACION.txt).

## Seguir trabajando con Git

El proyecto ya está publicado en [Clase_Ia_Vicente](https://github.com/Suisagui/Clase_Ia_Vicente). Su historial incluye los pasos del clasificador de intención, el detector de spam y el banco práctico.

Si quieres continuar desde tu computador, clona el repositorio:

```bash
git clone https://github.com/Suisagui/Clase_Ia_Vicente.git
cd Clase_Ia_Vicente
```

Al clonarlo, Git deja configurado el remoto `origin`. Puedes revisar la conexión y la identidad que se usará en tus commits:

```bash
git remote -v
git config user.name
git config user.email
```

Si falta tu nombre o correo, configúralos con tus datos reales mediante `git config user.name` y `git config user.email`.

Después de modificar un ejercicio, revisa los cambios y guarda el avance:

```bash
git status
git diff
git add taller-ia-python/
git commit -m "Mejorar ejercicios del taller"
git push
```

Antes de ejecutar `git add`, comprueba que los archivos mostrados por `git status` sean los que quieres incluir. Puedes consultar las versiones guardadas con `git log --oneline`.
