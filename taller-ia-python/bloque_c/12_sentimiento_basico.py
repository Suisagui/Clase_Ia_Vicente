mensaje = input("Escribe un mensaje: ").lower()
positivas = ["feliz", "excelente", "bueno", "genial"]
negativas = ["triste", "malo", "terrible", "horrible"]
puntaje = 0
for palabra in positivas:
    if palabra in mensaje:
        puntaje += 1
for palabra in negativas:
    if palabra in mensaje:
        puntaje -= 1
print("Puntaje:", puntaje)
if puntaje > 0:
    print("Positivo")
elif puntaje == 0:
    print("Neutral")
else:
    print("Negativo")
