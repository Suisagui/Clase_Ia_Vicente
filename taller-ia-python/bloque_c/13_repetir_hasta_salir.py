mensaje = input("Escribe un mensaje (salir para terminar): ")
while mensaje.strip().lower() != "salir":
    print("Mensaje recibido:", mensaje)
    mensaje = input("Escribe un mensaje (salir para terminar): ")
print("Programa finalizado")
