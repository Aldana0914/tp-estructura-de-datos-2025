from mensaje import Mensaje

class Mensaje: # Sea crea el mensaje 
    def __init__(self, emisor, destinatarios, asunto, contenido):
        self._emisor = emisor
        self._destinatarios = destinatarios
        self._asunto = asunto
        self._contenido = contenido   
        
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