def verificar_mayoria_edad(edad):
    # Esta función toma la edad como argumento y devuelve un mensaje indicando si el usuario es mayor de edad (18 años o más) o no.
    
    if edad >= 18:
        return 'Eres mayor de edad.'
    else:
        return 'Eres menor de edad.'

def obtener_edad():
    # Esta función solicita al usuario que ingrese su edad y valida la entrada.
    
    while True:
        try:
            # Solicitar al usuario que ingrese su edad
            edad_usuario = input("¿Cuál es tu edad? ")
            # Convertir la entrada a un entero
            edad_usuario = int(edad_usuario)

            # Validar que la edad sea un número positivo
            if edad_usuario < 0:
                raise ValueError("Por favor, ingresa una edad válida que no sea negativa.")
            
            return edad_usuario  # Retornar la edad válida

        except ValueError:
            # Manejo de errores
            print("Parece que no has ingresado una edad válida. Asegúrate de escribir un número entero positivo.")

# Ejecución
edad_usuario = obtener_edad()  # Obtener la edad validada del usuario
resultado = verificar_mayoria_edad(edad_usuario)  # Verificar la mayoría de edad
print(resultado)  # Mostrar el resultado