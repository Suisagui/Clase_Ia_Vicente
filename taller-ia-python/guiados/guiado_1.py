mensaje = input("Escribe un mensaje: ").lower()

if "precio" in mensaje or "cuesta" in mensaje:
    print("Intención: consulta de precio")
elif "ayuda" in mensaje or "problema" in mensaje:
    print("Intención: solicitud de ayuda")
elif "hola" in mensaje:
    print("Intención: saludo")
elif "adiós" in mensaje or "chao" in mensaje:
    print("Intención: despedida")
else:
    print("Intención desconocida")
