from carpeta import Carpeta

class Carpeta: #Se crea la carpeta correspondiente.
    def __init__(self, nombre):
        self._nombre = nombre #Recibe el nombre de la carpeta (inbox, enviados, etc)
        self._mensajes = [] #Crea la lista vacia de mensajes
        self._subcarpetas = [] #Crea la lista vacia de subcarpetas
    
    @property
    def nombre(self):
        return self._nombre

    def listar_mensaje(self): #Recibe todos los mensajesew.
        return self._mensajes

    def agregar_mensaje(self, mensaje): #Se define la función y recibe el mensaje
        self._mensajes.append(mensaje)

    def elimnar_mensaje(self, mensaje): #Se define la función y se recibe el parametro del mensaje
        if mensaje in self._mensajes: #Busqueda de msj en la lista de msjs
            self._mensajes.remove(mensaje) #Elimina msj de una lista
            
    def agregar_subcarpeta(self, subcarpeta): #Agrega subcarpetas a la carpeta
        self.subcarpetas.append(subcarpeta)
        
    def buscar_mensaje(self, texto):
        resultado = []
        texto = texto.lower()

        for mensaje in self._mensajes:
            if (texto in mensaje.asunto.lower() or
                texto in mensaje.contenido.lower() or
                texto in mensaje.emisor.lower()):
                resultado.append(mensaje)

        for subcarpeta in self._subcarpetas:
            resultado.extend(subcarpeta.buscar_mensaje(texto))

        return resultado
        
    def mover_mensaje(self, mensaje, carpeta_destino):
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)
            return True

        for subcarpeta in self._subcarpetas:
            if subcarpeta.mover_mensaje(mensaje, carpeta_destino):
                return True

        return False