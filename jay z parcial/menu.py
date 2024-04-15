class Menu2:
    def __init__(self, opciones):
        self.opciones = opciones

    def mostrar(self):
        print("MENU PRINCIPAL")
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion.nombre}")
        print("5. SALIR")

class SUB:
    def __init__(self, nombre):
        self.nombre = nombre
        self.acciones = {
            1: self.crear,
            2: self.listar,
            3: self.eliminar,
            4: self.atras
        }

    def mostrar(self):
        print(f"SUBMENU {self.nombre}")
        print("1. CREAR")
        print("2. LISTAR")
        print("3. ELIMINAR")
        print("4. ATRAS")

    def seleccionar_accion(self, opcion):
        accion = self.acciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida.")

    def crear(self):
        print(f"Creando {self.nombre[:-1]}...")

    def listar(self):
        print(f"Listando {self.nombre}...")

    def eliminar(self):
        print(f"Eliminando {self.nombre[:-1]}...")

    def atras(self):
        pass