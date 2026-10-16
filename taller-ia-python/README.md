# Taller de Python e inteligencia artificial basada en reglas

## Entrega
- Soluciones_bloques_A_y_B.docx: respuestas razonadas 1 a 8.
- bloque_c: seis programas independientes, ejercicios 9 a 14.
- guiados: cuadernos de referencia sin salidas antiguas y programas finales.
- VERIFICACION.txt: comprobaciones ejecutadas.

## Uso
Instalar Python 3. No se necesitan paquetes externos para los programas.
Desde esta carpeta, ejecutar python seguido de la ruta del archivo:

    python bloque_c/09_detector_saludo.py

    python bloque_c/10_clasificador_tickets.py

    python bloque_c/11_palabras_sospechosas.py

    python bloque_c/12_sentimiento_basico.py

    python bloque_c/13_repetir_hasta_salir.py

    python bloque_c/14_palindromo.py

Los cuadernos se abren en Jupyter y se ejecutan de arriba hacia abajo. Los comandos Git de las celdas Markdown se ejecutan en una terminal.

## Criterios
9. Detecta hola o buenas sin distinguir mayúsculas.
10. Soporte: ayuda, problema, error. Ventas: precio, comprar, cotizar. Soporte tiene prioridad si ambas categorías coinciden. Sin coincidencias: Otro.
11. Lista: gratis, premio, ganaste, urgente, haz clic, contraseña. Cada término suma una vez aunque se repita.
12. Positivas: feliz, excelente, bueno, genial. Negativas: triste, malo, terrible, horrible. Cada positiva encontrada suma 1; cada negativa resta 1. Mayor que cero: Positivo; cero: Neutral; menor que cero: Negativo.
13. Repite hasta salir. Admite mayúsculas y espacios exteriores en la orden de salida.
14. Construye la inversión con for y compara. Ignora mayúsculas y espacios exteriores, rechaza entradas vacías y conserva tildes. Se espera una sola palabra.

Como en las guías, in busca subcadenas, no palabras completas: hola también coincide con holanda. El sentimiento no interpreta negaciones ni ironía: "no estoy feliz" suma por feliz. Son reglas didácticas, no modelos entrenados.

## Revisión de las guías
El clasificador prioriza precio/cuesta, luego ayuda/problema, después hola y finalmente adiós/chao. Solo se ejecuta la primera coincidencia.
Spam: riesgo 0 produce Mensaje normal; riesgo 1 o 2 produce Mensaje sospechoso; riesgo de 3 o más produce Posible spam.
En la primera guía, wd parece un error tipográfico: usar Get-Location en PowerShell o pwd en Bash.

## Git y GitHub
Estos comandos describen el procedimiento; no constituyen evidencia de publicación.
Dentro de esta carpeta, comprobar Git e identidad:

    git --version
    git init
    git config user.name
    git config user.email

Si falta la identidad, usar git config user.name y git config user.email con nombre y correo propios. No es necesario modificar la configuración global.
Registrar los avances:

    git add guiados/ejercicio_guiado_1.ipynb guiados/guiado_1.py
    git commit -m "Implementar clasificador de intenciones"
    git add guiados/ejercicio_guiado_2.ipynb guiados/guiado_2.py
    git commit -m "Agregar detector de spam con bucle"
    git add .
    git commit -m "Resolver banco practico de Python"
    git log --oneline
    git status
    git remote -v

Crear un repositorio vacío en GitHub. Reemplazar URL_DEL_REPOSITORIO por la URL real:

    git remote add origin URL_DEL_REPOSITORIO
    git branch -M main
    git remote get-url origin
    git push -u origin main

Si origin ya existe, revisar su URL antes de cambiarlo o enviar archivos. Para futuras modificaciones: revisar git diff, preparar archivos, crear un commit y usar git push.
