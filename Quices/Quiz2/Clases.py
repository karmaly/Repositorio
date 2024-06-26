# Importo fuciones para:     
import numpy as np # manejar matrices
import matplotlib.pylab as plt # graficarlas
import pandas as pd # leer(crear) y manipular ciertos archivos (Se convierten en DataFrame)
import scipy.io as sio # y librería para leer archivos .mat

# Clase que almacena por id_ el tipo de dato leído
class sistema: 
    def __init__(self):
        self.__diccsv = {}
        self.__dicmat = {}

    # Me permite ver los diccionarios creados 
    def verdiccsv(self):
        return self.__diccsv
    def verdicmat(self):
        return self.__dicmat
    
    # Me permite añadir información a los diccionarios creados 
    def agregaracsv(self, id_, dic):
        self.verdiccsv()[id_] = dic
        return print('Asigando con éxito')
    def agregaramat(self, id_, dic):
        self.verdicmat()[id_] = dic
        return print('Asigando con éxito')
    
    # Me permite verificar si el id_ ingresado existe en algúno de los diccionarios propios de la clase. 
    def verificarexistecsv(self, id_):
        if id_ in self.__diccsv:
            return True
        else:
            return False
    def verificarexistemat(self, id_):
        if id_ in self.__dicmat:
            return True
        else:
            return False
      
    # Me permite escoger y redimensionar el arreglo y lo retorna para ser usado en la clase graficarmat.
    def dimensionado(self, id_):
        cont = 0
        catalogo = {}
        print('La información contenida en el archivo es la siguiente: ')
        for clave, info_ in self.verdicmat()[id_].items(): 
            print(f'''Posición {cont}: El diccionario es "{clave}" y su Clave es:
            {info_}\n''')
            catalogo[cont] = info_
            cont = cont + 1 
        posicion = int(input('Eliga la posición del arreglo que desea usar: '))
        arreglo = catalogo[posicion]
        dim = arreglo.ndim
        if dim == 2:
            return arreglo
        else:
            size = arreglo.size
            if size % 2 == 0:
                shape = int(size//2)
                arreglo = arreglo.reshape(2,shape)
                return arreglo
            else: 
                size = size - 1
                shape = int(size//2)
                arreglo = arreglo.reshape(2,shape+1)
                return arreglo

    # Son funciones que me permiten manejar la opción de mostrar información relacionada con archivos .csv
    def mostrarcolumnas(self, id_):
        listacolumnas = self.verdiccsv()[id_].columns
        print('Las columnas del archivo son:\n')
        for i in range(len(listacolumnas)):
            print({listacolumnas[i]})  
    def graficarcolumna(self, id_):
        tabla = self.verdiccsv()[id_]
        while True:
            print('Esta es la visualización del archivo almacenado')
            print(tabla)
            try:
                columna = input('Indique el nombre de la columna que posee datos númericos que desea graficar: ')
                print(f'''La columna escogida es la siguiente: 
                      
                      {tabla[columna]}\n''')
                break
            except KeyError:
                print('El nombre debe ser exactemente el mismo.')
        plt.scatter(tabla.index, tabla[columna])  # Utiliza los indices como valores para el eje x si tu DataFrame tiene un índice numérico
        plt.xlabel('Índice') 
        plt.ylabel('Valor de la columna')
        plt.title(f'Scatter de la columna {columna}')
        plt.grid(True)
        plt.show() 
    def crearcolumna(self, id_):
        while True:
            tabla = self.verdiccsv()[id_]
            print(tabla)
            try:
                print('\nCreacción de nueva columna. Indique los nombres de las columnas a sumar.')
                c1 = input('Primera columna: ')
                c2 = input('Segunda columna: ')
                c3 = input('Tercera columna: ')
                c4 = input('Cuarta columna: ')
                self.verdiccsv()[id_]['Nueva_Columna'] =  self.verdiccsv()[id_][[c1, c2, c3, c4]].sum(axis=1, skipna=True) 
                media = tabla['Nueva_Columna'].mean()
                moda = tabla['Nueva_Columna'].mode().iloc[0]  # En caso de que haya múltiples modas, esto selecciona la primera
                desv = tabla['Nueva_Columna'].std()
                return print(f'La nueva colmuna tiene una media, moda y desviación de {media}, {moda} y {desv} respectivamente.')
            except KeyError:
                print('El nombre debe ser exactemente el mismo. Sin espacios antes o después.')
            except TypeError:
                print('Deben ser columnas con datos numéricos')
        
# Clase que se encarga de graficar todo arreglo. Como se exige una ubicación en particular de las gráficas
# se dispone de la figura de la siguiente manera: se crean 3 subplots que se ubicarán
class graficarmat:
    def __init__(self):
        self.__figura = plt.figure()
        self.__eje1 = self.__figura.add_subplot(2,3,3) #en la esquina superior derecha
        self.__eje2 = self.__figura.add_subplot(2,3,4) #en la esquina inferior izquierda
        self.__eje3 = self.__figura.add_subplot(2,3,5) #en la centro de la zona inferior

    def graf1(self, arreglo):
        print('\nGRÁFICA 1')
        shapev, shapeh = arreglo.shape
        print(f'Tiene disponible {shapev} canal(es) para graficar.')
        while True:
            canal1 = int(input('Seleccione el canal que desea graficar en la desviación estándar: '))-1
            if 0 <= canal1 <= shapev:
                break
            else:
                print(f'Ingrese un valor entre 1 y {shapev}: ')
        x = np.random.randn(shapeh)
        leyenda = input('Ingrese leyenda: ')
        titulo = input('Ingrese título: ')
        nomx = input('Ingrese etiqueta del eje x: ')
        nomy = input('Ingrese etiqueta del eje y: ')
        self.__eje1.scatter(x, arreglo[canal1,:], label=leyenda)
        self.__eje1.set_title(titulo)
        self.__eje1.set_xlabel(nomx)
        self.__eje1.set_ylabel(nomy)
        self.__eje1.legend()
        self.__eje1.grid(True)
    def graf2(self, arreglo):
        print('\nGRÁFICA 2')
        sum = np.sum(arreglo, axis=0)
        shapeh = arreglo.shape[1]
        while True:
            a = int(input(f'Ingrese un valor entre 0 y {shapeh-1} para el límite inferior del segmento que desea graficar: '))
            b = int(input(f'Ingrese un valor entre 0 y {shapeh-1} para el límite superior del segmento que desea graficar: '))
            if a < b and 0 <= a <= shapeh-1 and 0 <= b <= shapeh-1:
                break
            else:
                print(f'Ingrese un valor entre 0 y {shapeh-1} para cada segmento. Recuerde que el primer número debe ser menor que el segundo')
        leyenda2 = input('Ingrese leyenda: ')
        titulo2 = input('Ingrese título: ')
        nomx2 = input('Ingrese etiqueta del eje x: ')
        nomy2 = input('Ingrese etiqueta del eje y: ')
        self.__eje2.plot(sum[a:b], color='red', label=leyenda2)
        self.__eje2.set_title(titulo2)
        self.__eje2.set_xlabel(nomx2)
        self.__eje2.set_ylabel(nomy2)
        self.__eje2.legend()
        self.__eje2.grid(True)
    def graf3(self, arreglo):
        print('\nGRÁFICA 3')
        shapev, shapeh = arreglo.shape
        print(f'Tiene disponible {shapev} canal(es) para graficar.')
        while True:
            canal2 = int(input('Seleccione el canal que desea graficar con ruido: '))-1
            if 0 <= canal2 <= shapev-1:
                break
            else:
                print(f'Ingrese un valor entre 1 y {shapev}')
        shape = arreglo.shape
        x2 = np.random.randn(shapeh)
        arreglo2 = arreglo+np.random.random(shape)
        leyenda3 = input('Ingrese leyenda: ')
        titulo3 = input('Ingrese título: ')
        nomx3 = input('Ingrese etiqueta del eje x: ')
        nomy3 = input('Ingrese etiqueta del eje y: ')
        self.__eje3.plot(x2, arreglo2[canal2,:], color='yellow', label=leyenda3)
        self.__eje3.set_title(titulo3)
        self.__eje3.set_xlabel(nomx3)
        self.__eje3.set_ylabel(nomy3)
        self.__eje3.legend()
        self.__eje3.grid(True)
