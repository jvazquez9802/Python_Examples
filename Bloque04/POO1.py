#Todo es un objeto, incluimos los tipos de datos y las clases
#Permite utilizar herencia multiple
#No existen metodos ni atributos privados
#Los atributos pueden ser modificados directamente
#monkey patching
#duck typing
#Sobrecarga de operadores
#Permite la creacion de nuevos tipos de datos
    

#Definir una clase persona

#Creamos a la clase persona
class Persona():
    cedula = "CEDULAXXX000X"
    nombre = ""
    apellido = ""
    sexo =""

una_persona = Persona()
una_persona.nombre = "Juan"
otra_persona = Persona()
otra_persona.nombre="Jesús"

"""print(una_persona.nombre)
print(otra_persona.nombre)"""

#public, private. protected


class User():
    id = 0
    user_name = "Unevenly" #SIGNIFICADO ESPECIAL
    email = "Un@g.com"
    __password = "1234asdf" #Privado
    
    """
    @staticmethod
    def contar():
        print(user_name)
        
"""
    @classmethod
    def edit_id(cls):
        cls.id += 1
   
    
    def show_password(self):
        return self.__password
    
    def print_user_name(self):
        print(self.user_name)


usuario1 = User()
usuario1.edit_id()
usuario1.user_name = "HeavensDoor"
usuario1.fp = "Con humanidad y democracia los pueblos nunca han sido liberados"
usuario2 = User()
usuario2.edit_id()



#public static void imprimirEntero(Scanner x){
#   System.out.println("Un numero" + x.nextInt())
#}

#Scanner leer = new Scanner(System.in);
# imprimirEntero(leer)

class Estudiante():
    
    def __init__(self, nombre, no_control):
        self.nombre = nombre
        self.no_control = no_control
        
    
    def loguear(self):
        print(f"{self.nombre} ha iniciado sesion")
    
        
    
        
estudiante1 = Estudiante("Juan", "17460654")
estudiante2 = Estudiante("Marysol", "17460663")
estudiante3 = Estudiante("Edgar", "17460672")

estudiante1.loguear()


#isinstance(estudiante, Estudiante)