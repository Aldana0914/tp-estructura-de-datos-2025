from Filtros import FiltroCorreo
from Cola_prioridades import ColaPrioridadMensajes

class ServidorCorreo:
    def _init_(self, nombre):
        self._nombre = nombre
        self._usuarios = []
        self._filtro = FiltroCorreo()
        self.cola = ColaPrioridadMensajes()

    @property
    def nombre(self):
        return self._nombre

    @property
    def filtro(self):
        return self._filtro

    def agregar_usuario(self, usuario):
        if usuario not in self._usuarios:
            self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)

    def obtener_usuarios(self):
        return self._usuarios

    def buscar_usuario_por_email(self, email):
        for usuario in self._usuarios:
            if usuario.email == email:
                return usuario
        return None

    def enviar_mensaje(self, mensaje):
        destinatarios_validos = []
        for email in mensaje.destinatarios:
            usuario = self.buscar_usuario_por_email(email)
            if usuario:
                usuario.recibir_mensaje(mensaje)
                destinatarios_validos.append(email)
        return destinatarios_validos