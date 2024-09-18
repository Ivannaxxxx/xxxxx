def calcular_area_rectangulo(base, altura):
    #Esta función calcula el área de un rectángulo y verifica si el área es mayor a 40 la altura es mayor a 10, retornando un mensaje personalizado en caso afirmativo.

    area = base * altura
    if area > 40 and altura > 10:
        return f'El área es {area}, que es mayor a 40 y la altura es mayor a 10.'
    return f'El área es {area}.'

def obtener_dimension(prompt):
    # Esta función solicita al usuario que ingrese una dimensión (base o altura) y valida la entrada.
    
    while True:
        try:
            dimension = float(input(prompt))  # Solicitar la dimensión
            if dimension <= 0:
                raise ValueError("Por favor, ingresa un número positivo mayor que cero.")
            return dimension  # Retornar la dimensión válida
        except ValueError:
            print("Oops! Asegúrate de escribir un número válido. Inténtalo de nuevo.")

# Ejecución

base_usuario = obtener_dimension("Introduce la base del rectángulo: ")  # Obtener base válida
altura_usuario = obtener_dimension("Introduce la altura del rectángulo: ")  # Obtener altura válida
resultado_area = calcular_area_rectangulo(base_usuario, altura_usuario)  # Calcular el área
print(resultado_area)  # Mostrar el resultado