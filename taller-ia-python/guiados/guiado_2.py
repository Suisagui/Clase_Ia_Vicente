mensaje = input("Escribe un mensaje: ").lower()

palabras_sospechosas = ["gratis", "premio", "ganaste", "urgente", "haz clic", "contraseña"]
riesgo = 0  

for palabra in palabras_sospechosas:
    if palabra in mensaje:
        riesgo += 1

print("Puntaje de riesgo:", riesgo)

if riesgo == 0:
    print("Mensaje normal")
elif riesgo <= 2:
    print("Mensaje sospechoso")
else:
    print("Posible spam")
