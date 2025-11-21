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