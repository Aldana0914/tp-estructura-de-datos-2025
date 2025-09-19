from abc import ABC, abstractmethod

class GestionCorreo(ABC):
    @abstractmethod
    def enviar_mensaje(self, destinatarios, asunto, contenido):
        pass

    @abstractmethod    
    def recibir_mensaje(self, mensaje):
        pass
     @abstractmethod    
    def recibir_mensaje(self, mensaje):
        pass

    @abstractmethod
    def listar_mensaje(self, carpeta):
        pass

# Clase ServidorCorreo
class ServidorCorreo:  #Representa el servidor de mensajeria
    def __init__(self, email): # Construye la estructura.
        self._email = email # Registra el email del usuario.
        self._usuarios = [] # Lista de usuarios en la que se guardaran los mismos.

    @property
    def email(self):
        return self._email
    
    def agregar_usuario(self, usuario): # Agrega usuarios al servidsdor.
        self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self._usuarios.remove(usuario) # Elimina usuarios del servidor.

    def obtener_usuarios(self):
        return self._usuarios  # Devuelve la lista de usuarios total en el servidor.

# Clase Usuario
class Usuario(GestionCorreo):
    def __init__(self, nombre, email, servidor):
        self._nombre = nombre
        self._email = email
        self._servidor = servidor
        self._carpetas = {
            "Inbox": Carpeta("Inbox"),    # Asignación de nombre a 
            "Enviados": Carpeta("Enviados"),  # Cada Carpeta
            "Papelera": Carpeta("Papelera")
        }    
        
    @property
    def nombre(self):
        return self._nombre
        
    @property
    def email(self):
        return self._email
        
    @property
    def carpetas(self):
        return self._carpetas    
    
    # Métodos de Gestión de correo
    def enviar_mensaje(self, destinatarios, asunto, contenido):
        mensaje = Mensaje(self._email, destinatarios, asunto, contenido)
        self._carpetas["Enviados"].agregar_mensaje(mensaje)
        print(" Mensaje enviado a {destinatarios}")
    
    def recibir_mensaje(self, mensaje):
        self._carpetas["Inbox"].agregar_mensaje(mensaje)
        
    def listar_mensaje(self, carpeta):
        if carpeta in self._carpetas:
            return self._carpetas[carpeta].listar_mensaje()
        return []    
        
# Clase Mensaje
class Mensaje: # Sea crea el mensaje 
    def __init__(self, emisor, destinatarios, asunto, contenido):
        self._emisor = emisor
        self._destinatarios = destinatarios
        self._asunto = asunto
        self._contenido = contenido   
        
    @property
    def emisor(self):
        return self._emisor
        
    @property
    def destinatarios(self):
        return self._destinatarios
    
    @property
    def asunto(self):
        return self._asunto    
    
    @property
    def contenido(self):
        return self._contenido
    
class Carpeta: #Se crea la carpeta correspondiente.
    def __init__(self, nombre):
        self._nombre = nombre #Recibe el nombre de la carpeta (inbox, enviados, etc)
        self._mensajes = [] #Crea la lista vacia de mensajes
    
    @property
    def nombre(self):
        return self._nombre

    def listar_mensaje(self): #Recibe todos los mensajesew.
        return self._mensajes

    def agregar_mensaje(self, mensaje): #Se define la función y recibe el mensaje
        self._mensajes.append(mensaje)

    def delete_mensaje(self, mensaje): #Se define la función y se recibe el parametro del mensaje
        if mensaje in self._mensajes: #Busqueda de msj en la lista de msjs
            self._mensajes.remove(mensaje) #Elimina msj de una lista
            