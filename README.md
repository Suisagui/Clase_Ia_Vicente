# Primeros pasos con Python e inteligencia artificial

Este repositorio reúne los ejercicios de la clase: desde entender qué imprime una condición hasta crear pequeños programas que clasifican mensajes con palabras clave.

La idea es practicar lo básico de Python —variables, condiciones, listas y bucles— y usar Git y GitHub para guardar el avance del trabajo.

## Qué encontrarás aquí

La entrega está organizada en la carpeta [taller-ia-python](taller-ia-python):

- **[Bloques A y B en Word](taller-ia-python/Soluciones_bloques_A_y_B.docx):** respuestas de los ejercicios 1 al 8, con una explicación de cada resultado.
- **[Bloque C en Python](taller-ia-python/bloque_c):** seis programas para detectar saludos, clasificar tickets, contar palabras sospechosas, analizar sentimientos, repetir mensajes y reconocer palíndromos.
- **[Ejercicios guiados](taller-ia-python/guiados):** los cuadernos de clase y las versiones finales del clasificador de intención y del detector de spam.
- **[Comprobaciones](taller-ia-python/VERIFICACION.txt):** resultados de los 39 casos revisados.

## Cómo probar los programas

Necesitas Python 3. Puedes descargar el repositorio desde **Code → Download ZIP**, descomprimirlo y abrir una terminal en su carpeta. Si usas Git, también puedes clonarlo:

```bash
git clone https://github.com/Suisagui/Clase_Ia_Vicente.git
cd Clase_Ia_Vicente
```

Para empezar, prueba el detector de saludos:

```bash
python taller-ia-python/bloque_c/09_detector_saludo.py
```

El programa te pedirá un mensaje. Si escribes `Hola, ¿cómo estás?`, responderá `Saludo detectado`. Cada ejercicio se ejecuta por separado y los archivos `.py` no necesitan librerías adicionales.

En la [guía del taller](taller-ia-python/README.md) están los comandos de los demás ejercicios y las reglas que utiliza cada uno.

## Sobre las reglas

Estos programas toman decisiones a partir de palabras que aparecen en el texto. Sirven para entender cómo construir una clasificación sencilla, pero todavía no interpretan el contexto. Por ejemplo, el analizador de sentimiento encuentra la palabra “feliz” incluso en “no estoy feliz”.

El historial conserva los tres pasos principales del trabajo: el clasificador de intención, el detector de spam y la solución del banco práctico.
