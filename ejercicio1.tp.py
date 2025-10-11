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
            