from manejo_archivos import guardar_inscripcion, leer_inscripciones

def inscribir_participante():
    nombre = input("Ingrese el nombre del participante: ")
    taller = input("Ingrese el nombre del taller: ")
    
    inscripcion = f"{nombre},{taller}\n"
    guardar_inscripcion(inscripcion)
    print("Inscripción realizada con éxito.")

def mostrar_inscripciones():
    inscripciones = leer_inscripciones()
    if inscripciones:
        print("\n--- Lista de Inscripciones ---")
        for linea in inscripciones:
            nombre, taller = linea.strip().split(',')
            print(f"Participante: {nombre} - Taller: {taller}")
    else:
        print("No hay inscripciones registradas.")
