from gestion_talleres import inscribir_participante, mostrar_inscripciones
from manejo_archivos import cargar_datos, guardar_dato

def menu():
    while True:
        print("\n--- Sistema de Inscripciones ---")
        print("1. Inscribir participante")
        print("2. Mostrar inscripciones")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            inscribir_participante()
        elif opcion == '2':
            mostrar_inscripciones()
        elif opcion == '3':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

