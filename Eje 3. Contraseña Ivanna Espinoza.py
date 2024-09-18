def verificar_contrasena(contrasena_guardada, contrasena_usuario):

    #Esta función compara la contraseña ingresada por el usuario con la guardada, ignorando las mayúsculas y minúsculas.

    return contrasena_guardada.lower() == contrasena_usuario.lower()

def obtener_contrasena():
    # Esta función solicita al usuario que ingrese su contraseña y valida la entrada.
    
    while True:
        contrasena_ingresada = input("Introduce la contraseña: ").strip()  # Eliminar espacios en blanco

        # Validar que la contraseña no esté vacía
        if not contrasena_ingresada:
            print("La contraseña no puede estar vacía. Por favor, intenta de nuevo.")
            continue  # Volver a solicitar la contraseña

        return contrasena_ingresada  # Retornar la contraseña válida

# Ejecución
contrasena = 'Secreta123'  # Contraseña guardada
intentos = 3  # Número de intentos permitidos

for i in range(intentos):
    contrasena_ingresada = obtener_contrasena()  # Obtener la contraseña validada del usuario
    resultado_verificacion = verificar_contrasena(contrasena, contrasena_ingresada)  # Verificar la contraseña
    
    if resultado_verificacion:
        print("Contraseña correcta.")
        break  # Salir del bucle si la contraseña es correcta
    else:
        print("Contraseña incorrecta.")
        if i < intentos - 1:  # Si no es el último intento
            print(f"Tienes {intentos - i - 1} intento(s) restante(s).")
        else:  # Si es el último intento
            print("Has agotado todos los intentos. Acceso denegado.")