'''
a) Registrar al personal de la institución.
b) Visualizar todo el listado del personal de la institución.
c) Versionamiento de su programa y link de GitHub
d) Realizar capturas de su programa.
'''

class docente:
    '''
    Clase docente
        Clase para ingresar cada uno de los datos requidos
        en el enunciado
    '''
    def __init__ (self, nombre, apellido, edad):
        '''
        Atribtutos a construir
        nombre=nombre del docente
        apellido=apellido del docente
        edad=edad del docente
        '''
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

'''
Creación de subclase o clase hija para herencia
para el ingreso respectivo del rol, departamento y salario
'''
class personalInstitucion (docente):
    ''' 
    Subclase personalInstitucion
        Clase para ingresar:
        Rol=Rol que cumpre el docente dentro de la institución
        Departamento=Departamento en el que se encuentra el docente
        Salario=Salario del docente
    '''
    def __init__(self, nombre, apellido, edad, rol, departamento, salario):
        super().__init__(nombre, apellido, edad)
        self.rol=rol
        self.departamento=departamento
        self.salario=salario

#Lista Docentes
'''
Clase lista, para guardar los docentes a ingresar
'''
listaDocentes=[]
'''
numerosDocentes=Variables donde vamos a almacenar el número de docentes a ingresar
'''
#peidmos al usuario la cantidad de datos a ingresar
numerosDocentes=int(input("Digite el número de docentes a ingresar: "))
if (numerosDocentes>0):
    '''
    Condicional para permitir el ingreso de más de 0 usuarios
    '''
    #Agregar a la lista
    for i in range (numerosDocentes):
        '''
        Bucle For:
            Ingreso de los datos de cada uno de los docentes:
            Variables a almacenar en la lista:
            nombreDocente
            apellidoDocente
            edadDocente
            departamentoDocente
            salarioDocente
            rolDocente
        format= La función format nos permite incluir en una cadena, texto ordinario y 
        caracteres de formateo, que representan un tipo en particular de datos, tales 
        como entero, cadena o flotante (Beazley, 2009).
        '''
        nombreDocente=str(input("Ingrese el nombre {}: ".format(i+1)))
        apellidoDocente=str(input("Ingrese el apellido {}: ".format(i+1)))
        edadDocente=str(input("Ingrese el edad {}: ".format(i+1)))
        departamentoDocente=str(input("Ingrese el departamento {}: ".format(i+1)))
        salarioDocente=str(input("Ingrese el salario {}: ".format(i+1)))
        rolDocente=str(input("Ingrese el rol {}: ".format(i+1)))
        '''
        Instancia de personalInstitucion(subclase)
            Para almacernar los datos del docente junto con los del personal acádemico
        '''
        datosDocente=personalInstitucion(nombreDocente, apellidoDocente, edadDocente, rolDocente, departamentoDocente, salarioDocente)
        listaDocentes.append(datosDocente.nombre)
        listaDocentes.append(datosDocente.apellido)
        listaDocentes.append(datosDocente.edad)
        listaDocentes.append(datosDocente.rol)
        listaDocentes.append(datosDocente.departamento)
        listaDocentes.append(datosDocente.salario)
    '''
    Mostramos por pantalla la lista de docentes ingresados
    '''
    print (listaDocentes)
else:
    print("Ingrese un número de docentes mayor a 0")



