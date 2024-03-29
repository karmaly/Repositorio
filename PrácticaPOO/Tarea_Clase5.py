# Importo una función que me permite buscar patrones dentro de cadenas.
import re
# Creación de la clase Paciente
class Paciente:
    def __init__(self):
        # Atributos
        self.__nombre = ""
        self.__cedula = int
        self.__genero = ""
        self.__servicio = ""

# Getters de la clase Paciente
    def verNombre(self):
        return self.__nombre  
    def verServicio(self):
        return self.__servicio 
    def verGenero(self):
        return self.__genero   
    def verCedula(self):
        return self.__cedula
    
# Setters de la clase Paciente
    def asignarNombre(self,n):
        self.__nombre = n   
    def asignarServicio(self,s):
        self.__servicio = s  
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

# Creación de la clase Sistema
class Sistema:
    def __init__(self):
        # Atributos
        self.__lista_pacientes = []

# Funciones de la clase Sistema
    def verLista(self):
        return self.__lista_pacientes
    
    def verificarPac(self,cedula):
        encontrado = False
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                encontrado = True
                break
        return encontrado
      
    def ingresarPaciente(self,pac):
        if self.verificarPac(pac.verCedula()):
            return False
        self.__lista_pacientes.append(pac)
        return True

    def eliminarPaciente(self,cedula):
        if self.verificarPac(cedula) == False:
            return None
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                del self.__lista_pacientes[cedula]
                break
            return True
        
    def verNumeroPacientes(self):
        return len(self.__lista_pacientes)

# Funcion para validar entero
def validarNumero(numero):
    try:
        a = int(numero)
        return True
    except ValueError:
        return False
    
# Creación de función main para iniciar el código:    
def main():
    # Creo el objeto Sistema
    sis = Sistema()
    while True:
        # Brindo opciones de lo que se desea hacer en un menú y valido la escogida sea válida.
        opcionv = input("\nIngrese para:\n0. Volver al menu \n1. Ingresar nuevo paciente \n2. Ver paciente \n3. Ver cantidad de pacientes \n>> ")
        a = validarNumero(opcionv)
        if a:
            opcion = int(opcionv)
            if opcion == 1:
                print("\nA continuacion se solicitaran los seguientes datos:\n")
                # 1. Se solicitaran los datos
                nombre = input("Ingrese el nombre: ")
                while True:
                    # Valido si el dato ingresado para la cédula corresponde a un entero
                    cedulav = input("Ingrese la cedula: ")
                    c = validarNumero(cedulav)
                    if c:
                        cedula = int(cedulav)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")
                        continue
                genero = input("Ingrese el genero: ")
                servicio = input("Ingrese el servicio: ")
                # 2. Se crea un objeto Paciente
                pac = Paciente()
                # Como ese paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(nombre)
                pac.asignarCedula(cedula)
                pac.asignarGenero(genero)
                pac.asignarServicio(servicio)
                r = sis.ingresarPaciente(pac)
                # 3. Se almacena en la lista que esta dentro de la clase sistema
                if r == True:
                    print("Paciente ingresado")
                else:
                    print("Paciente ya existe en el sistema")

            elif opcion == 2:
                while True:
                    # Solicito el nombre o cedula que quiero buscar
                    busquedav = input("\nIngrese para:\n0. Busqueda por cédula o parte de ella \n1. Nombre o parte de él\n2. Volver al menú principal\n>> ")
                    a = validarNumero(busquedav)
                    if a:
                        busqueda = int(busquedav)
                        if busqueda == 0:
                            while True:
                                # Valido que sea un dato numérico
                                cedulav = input("Ingrese la cedula o parte de ella: ")
                                c = validarNumero(cedula)
                                if c:
                                    break
                                else:
                                    print("Debe ser un dato numérico (sin puntos ni letras)")
                                    continue
                            # Tomo el valor ingresado como un patrón mediante la función re.compile() para realizar 
                            # operaciones de búsqueda y coincidencia de patrones de manera más eficiente. También creo un contador
                            # que servirá para saber si se obtubieron o no resultados en la búsqueda.
                            patron = re.compile(f".*{cedulav}.*")
                            c = 0
                            # Accedo mediante una visualización el atributo del objeto lista. 
                            listadispobible = sis.verLista()
                            for p in listadispobible:
                            # Modifico a "str" el atributo relacionado con la cédula dado que el método match requiere que argumento sea "str".
                            # En caso de hallar alguna coincidencia se imprimen todos los atributos del objeto "Paciente".
                                if patron.match(str(p.verCedula())):
                                    c += 1
                                    print("Nombre: " + p.verNombre())
                                    print("Cedula: " + str(p.verCedula()))
                                    print("Genero: " + p.verGenero())
                                    print("Servicio: " + p.verServicio())
                            if c == 0: 
                                print("No se tiene coincidencias.")
                        # Se hace el mismo análisis de la anterior busqueda, pero al ser "str" no requiero validar que sea
                        # un dato numérico. Pero procedo con el método re.compile() de igual manera.
                        elif busqueda == 1:
                            nombre = input("Ingrese el nombre o parte de él: ")
                            patron = re.compile(f".*{nombre}.*")
                            c = 0
                            listadispobible = sis.verLista()
                            for p in listadispobible:
                                if patron.match(p.verNombre()):
                                    c += 1
                                    print("Nombre: " + p.verNombre())
                                    print("Cedula: " + str(p.verCedula()))
                                    print("Genero: " + p.verGenero())
                                    print("Servicio: " + p.verServicio())
                            if c == 0: 
                                print("No se tiene coincidencias.")
                        elif busqueda == 2:
                            break
                    else: 
                        print("Ingrese una opción válida")
            elif opcion == 3:
                print(f"La cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
                        
            elif opcion != 0:
                continue
        else:
            print("Seleccione una opción valida")
            continue

if __name__ == '__main__':
    main()