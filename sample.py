def ingresar_puntuacion_y_comentario():
    """Este método solicita al usuario una puntuación y un comentario, luego los guarda en un archivo."""
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point <= 0 or point > 5:
                print('Por favor, introduzca un valor entre 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:  # "with" cierra automáticamente el archivo
                    file_pc.write(f'{post} \n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')


def comprobar_resultados():
    """Este método lee y muestra los resultados guardados hasta el momento."""
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:  # Se maneja el archivo de manera segura
            contenido = read_file.read()
            if contenido:
                print(contenido)
            else:
                print("No hay datos disponibles aún.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Aún no se han registrado puntuaciones.")


def seleccionar_proceso():
    """Este método presenta las opciones al usuario y lo guía según su selección."""
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()  # Llamamos al método para ingresar puntuación
            elif num == 2:
                comprobar_resultados()  # Llamamos al método para comprobar resultados
            elif num == 3:
                print('Finalizando el programa.')
                break  # Finaliza el bucle y el programa
            else:
                print('Por favor, introduzca un número del 1 al 3.')
        else:
            print('Por favor, introduzca un número del 1 al 3.')


# Llamada al método principal para iniciar el programa
if ingresar_puntuacion_y_comentario == "_main_":
    seleccionar_proceso()