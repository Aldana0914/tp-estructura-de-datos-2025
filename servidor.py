from servidor import ServidorCorreo

# Clase ServidorCorreo
class ServidorCorreo: #Representa el servidor de mensajeria
    def __init__(self, email): # Construye la estructura.
        self._email = email # Registra el email del usuario.
        self._usuarios = [] # Lista de usuarios en la que se guardaran los mismos.

    @property
    def email(self):
        return self._email
    
    def agregar_usuario(self, usuario): # Agrega usuarios al servidsdor.
        if usuario not in self._usuarios:
            self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)

    def obtener_usuarios(self):
        return self._usuarios  # Devuelve la lista de usuarios total en el servidor.

    def buscar_usuario_por_email(self, email):
        """Busca un usuario por su email y lo devuelve, o None si no existe."""
        for usuario in self._usuarios:
            if usuario.email == email:
                return usuario
        return None

    def enviar_mensaje(self, mensaje):
        """
        Entrega un mensaje a todos los destinatarios existentes en el servidor.
        Devuelve la lista de destinatarios válidos que recibieron el mensaje.
        """
        destinatarios_validos = []
        for email in mensaje.destinatarios:
            usuario = self.buscar_usuario_por_email(email)
            if usuario:
                usuario.recibir_mensaje(mensaje)
                destinatarios_validos.append(email)
        return destinatarios_validos

from heapq import heappush, heappop

class ColaPrioridadMensajes:
    def _init_(self):
        self.cola = []
        self.contador = 0   # Evita errores cuando hay mismas prioridades

    def encolar(self, mensaje):
        # prioridad: -1 = urgente, 0 = normal (heapq saca primero números más chicos)
        prioridad = -1 if mensaje.urgente else 0
        heappush(self.cola, (prioridad, self.contador, mensaje))
        self.contador += 1

    def desencolar(self):
        if self.cola:
            return heappop(self.cola)[2]
        return None

    def esta_vacia(self):
        return len(self.cola) == 0
    
from Filtros import FiltroCorreo   # 👈 importar la clase filtro

class ServidorCorreo:
    """
    Representa un servidor de correo electrónico que administra usuarios
    y aplica filtros automáticos a los mensajes.
    """

    def _init_(self, nombre):
        self._nombre = nombre
        self._usuarios = []  # Lista de objetos Usuario
        self._filtro = FiltroCorreo()   # 👈 filtro global del servidor

    @property
    def filtro(self):
        """Devuelve el filtro del servidor."""
        return self._filtro