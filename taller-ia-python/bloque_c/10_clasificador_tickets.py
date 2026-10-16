# Soporte tiene prioridad cuando coinciden ambas categorias.
mensaje = input("Escribe tu ticket: ").lower()
if "ayuda" in mensaje or "problema" in mensaje or "error" in mensaje:
    print("Soporte")
elif "precio" in mensaje or "comprar" in mensaje or "cotizar" in mensaje:
    print("Ventas")
else:
    print("Otro")
