class FiltroCorreo:
    def __init__(self):
        # Palabras que activan el filtro SPAM (puede ampliarse)
        self.palabras_spam = [
            "gratis", "oferta", "promo", "descuento", "urgente",
            "haz clic", "regalo", "gana dinero", "click aquí"
        ]
        self.remitentes_bloqueados = set()

    def agregar_bloqueado(self, email):
        self.remitentes_bloqueados.add(email)

    def quitar_bloqueado(self, email):
        self.remitentes_bloqueados.discard(email)

    def aplicar(self, mensaje):
        if mensaje.emisor in self.remitentes_bloqueados:
            return "Bloqueados"

        contenido = mensaje.contenido.lower()
        if any(pal in contenido for pal in self.palabras_spam):
            return "Spam"

        return "Inbox"