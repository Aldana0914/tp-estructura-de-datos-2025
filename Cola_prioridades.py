from servidor import ColaPrioridadMensajes

class Servidor:
    def _init_(self, nombre, red=None):
        self.nombre = nombre
        self.usuarios = {}   # email -> objeto Usuario
        self.cola = ColaPrioridadMensajes()
        self.red = red       # referencia al grafo Red

    def agregar_usuario(self, usuario):
        self.usuarios[usuario.email] = usuario

    def recibir_mensaje(self, mensaje):
        print(f"[{self.nombre}] Mensaje recibido, encolando...")
        self.cola.encolar(mensaje)
        self.procesar_cola()   # <-- automático

    def procesar_cola(self):
        while not self.cola.esta_vacia():
            mensaje = self.cola.desencolar()
            destino = mensaje.destinatario

            # ¿El usuario está en este servidor?
            if destino in self.usuarios:
                print(f"[{self.nombre}] Entregando mensaje a {destino}")
                self.usuarios[destino].recibir_mensaje(mensaje)
            else:
                # Lo envío a través de la red
                print(f"[{self.nombre}] Redirigiendo mensaje hacia la red...")
                if self.red:
                    self.red.enviar_mensaje_red(self.nombre, destino, mensaje)
                else:
                    print(f"[ERROR] Servidor {self.nombre} no tiene red asignada.")