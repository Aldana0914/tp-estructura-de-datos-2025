from ejercicio1 import GestionCorreo
from carpeta import Carpeta
from mensaje import Mensaje

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

    def mover_mensaje(self, mensaje, carpeta_origen, carpeta_destino):
        if carpeta_origen in self._carpetas and carpeta_destino in self._carpetas:
            self._carpetas[carpeta_origen].mover_mensaje(
                mensaje, self._carpetas[carpeta_destino]
            )
