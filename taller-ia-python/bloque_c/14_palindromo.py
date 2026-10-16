palabra = input("Escribe una palabra: ").strip().lower()
invertida = ""
for letra in palabra:
    invertida = letra + invertida
if palabra == "":
    print("Debes escribir una palabra")
elif palabra == invertida:
    print("Es palíndromo")
else:
    print("No es palíndromo")
