from abc import ABC, abstractmethod

class GestionCorreo(ABC):
    @abstractmethod
    def enviar_mensaje(self, destinatarios, asunto, contenido):
        pass

    @abstractmethod    
    def recibir_mensaje(self, mensaje):
        pass

    @abstractmethod
    def listar_mensaje(self, carpeta):
        pass   

class Subcarpetas:
    def __init__(self, subcarpetas):
        self._subcarpetas = []  # lista de subcarpetas

    def agg_subcarpeta(self, subcarpeta):
        self._subcarpetas.append(subcarpeta)

    def mover_msjs(self, mensaje, carpeta_destino):
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agg_msjs(mensaje)

