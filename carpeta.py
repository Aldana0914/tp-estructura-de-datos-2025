from carpeta import Carpeta

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
            