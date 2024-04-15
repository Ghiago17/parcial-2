from menu import SUB, Menu2

class Main:
    @staticmethod
    def run():
        personas = SUB("PERSONAS")
        universidades = SUB("UNIVERSIDADES")
        notas = SUB("NOTAS")
        asignaturas = SUB("ASIGNATURAS")

        menu_principal = Menu2([personas, universidades, notas, asignaturas])
        
        submenu_actual = None

        while True:
            menu_principal.mostrar()
            opcion_principal = input("Seleccione una opción: ")

            try:
                opcion_principal = int(opcion_principal)
            except ValueError:
                print("Error: Por favor ingrese un número válido.")
                continue

            if opcion_principal == 5:
                print("Saliendo del programa...")
                break
            elif 1 <= opcion_principal <= 4:
                submenu_actual = menu_principal.opciones[opcion_principal - 1]
                while True:
                    submenu_actual.mostrar()
                    opcion_submenu = input("Seleccione una acción del submenu: ")

                    try:
                        opcion_submenu = int(opcion_submenu)
                    except ValueError:
                        print("Error: Por favor ingrese un número válido.")
                        continue

                    if opcion_submenu == 4:
                        break
                    else:
                        submenu_actual.seleccionar_accion(opcion_submenu)
            else:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    Main.run()