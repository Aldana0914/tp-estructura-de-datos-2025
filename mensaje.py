from mensaje import Mensaje

class Mensaje: # Sea crea el mensaje 

    def __init__(self, emisor, destinatarios, asunto, contenido,urgente=false):

        self._emisor = emisor
        self._destinatarios = destinatarios  # Puede ser una lista o string
        self._asunto = asunto
        self._contenido = contenido   
        self._urgente = urgente 

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

    def urgente(self):
        return self.urgente

    def _str_(self):#devuelde el mensaje legible 
        priorida="urgente "
      if self._urgente
         else "normal"
        return f"de:{self._emisor}/npara:{self._destinatarios}/nasunto:{self._asunto}||urgente:{self._urgente}|nprioridad:{priorida}|ncontenido:{self._contenido}"
        

