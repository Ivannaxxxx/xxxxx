def clasificar_alumno(nombre, sexo):
    
    #Esta función clasifica a un alumno en el grupo A o B basado en su nombre y sexo.
    #Grupo A: mujeres con nombre anterior a la M y hombres con nombre posterior a la N.
    #Grupo B: resto de los alumnos.
    
    # Convertir el nombre a mayúsculas para facilitar la comparación
    nombre = nombre.capitalize()
    
    if sexo.lower() == 'mujer' and nombre < 'M':
        return 'Grupo A'
    elif sexo.lower() == 'hombre' and nombre > 'N':
        return 'Grupo A'
    else:
        return 'Grupo B'

def obtener_datos_alumno():
    # Esta función solicita al usuario que ingrese su nombre y sexo, validando la entrada.
    
    while True:
        # Solicitar el nombre del usuario
        nombre_usuario = input("Introduce tu nombre: ").strip()  # Eliminar espacios en blanco

        # Validar que el nombre no esté vacío
        if not nombre_usuario:
            print("El nombre no puede estar vacío. Por favor, intenta de nuevo.")
            continue  # Volver a solicitar el nombre

        # Solicitar el sexo del usuario
        sexo_usuario = input("Introduce tu sexo (hombre/mujer): ").strip().lower()  # Convertir a minúsculas y eliminar espacios

        # Validar que el sexo sea correcto
        if sexo_usuario not in ['hombre', 'mujer']:
            print("Sexo no válido. Por favor, ingresa 'hombre' o 'mujer'.")
            continue  # Volver a solicitar el sexo

        return nombre_usuario, sexo_usuario  # Retornar los datos válidos

# Ejecución
nombre_usuario, sexo_usuario = obtener_datos_alumno()  # Obtener los datos del alumno
grupo_asignado = clasificar_alumno(nombre_usuario, sexo_usuario)  # Clasificar al alumno
print(f'Te corresponde el {grupo_asignado}.')  # Mostrar el grupo asignado