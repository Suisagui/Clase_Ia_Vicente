mensaje = input("Escribe un mensaje: ").lower()
palabras_sospechosas = ["gratis", "premio", "ganaste", "urgente", "haz clic", "contraseña"]
contador = 0
# Cada termino suma como maximo una vez.
for palabra in palabras_sospechosas:
    if palabra in mensaje:
        contador += 1
print("Palabras sospechosas encontradas:", contador)
