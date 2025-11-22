class Mensaje:
    def __init__(self, emisor, destinatarios, asunto, contenido, urgente=False):
        self._emisor = emisor
        self._destinatarios = destinatarios  # Puede ser una lista o string
        self._asunto = asunto
        self._contenido = contenido
        self._urgente = urgente  # Para la cola de prioridades (Entrega 3)

    # ===== PROPIEDADES =====
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

    @property
    def urgente(self):
        return self._urgente

    def __str__(self):
        return f"Asunto: {self._asunto} | De: {self._emisor} | Urgente: {self._urgente}"
