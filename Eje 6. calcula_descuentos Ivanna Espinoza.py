def calcular_descuento(cantidad):
    #Esta función calcula el precio total después de aplicar un descuento basado en la cantidad de zapatos comprados.
    
    precio_zapato = 80  # Precio por zapato
    total_compra = cantidad * precio_zapato
    
    if cantidad > 30:
        descuento = 0.40  # 40% de descuento
    elif cantidad > 20:
        descuento = 0.20  # 20% de descuento
    elif cantidad > 10:
        descuento = 0.10  # 10% de descuento
    else:
        descuento = 0.0   # Sin descuento

    total_con_descuento = total_compra * (1 - descuento)
    
    return total_con_descuento, descuento * 100

def obtener_cantidad_zapatos():
    # Esta función solicita al usuario que ingrese la cantidad de zapatos y valida la entrada.
    
    while True:
        try:
            # Solicitar al usuario que ingrese la cantidad de zapatos
            cantidad_zapatos = input("¿Cuántos zapatos deseas comprar? ")
            # Convertir la entrada a un entero
            cantidad_zapatos = int(cantidad_zapatos)

            # Validar que la cantidad sea un número positivo
            if cantidad_zapatos < 0:
                raise ValueError("La cantidad no puede ser negativa. Por favor, ingresa un número válido.")
            
            return cantidad_zapatos  # Retornar la cantidad válida

        except ValueError:
            # Manejo de errores
            print("Parece que no has ingresado una cantidad válida. Asegúrate de escribir un número entero positivo.")

# Ejecución
cantidad_zapatos = obtener_cantidad_zapatos()  # Obtener la cantidad validada de zapatos
total_final, porcentaje_descuento = calcular_descuento(cantidad_zapatos)  # Calcular el total y el descuento
print(f'Total a pagar: ${total_final:3f} (Descuento aplicado: {porcentaje_descuento}%)')  # Mostrar el resultado