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

