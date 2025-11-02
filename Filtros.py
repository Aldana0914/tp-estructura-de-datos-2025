class FiltroCorreo:
    
    def _init_(self):
        # Palabras que activan el filtro SPAM (puede ampliarse)
        self.palabras_spam = [
            "gratis", "oferta", "promo", "descuento", "urgente",
            "haz clic", "regalo", "gana dinero", "click aquí"
        ]

        # Lista de emails bloqueados
        self.remitentes_bloqueados = set()

    # =============== MÉTODOS DE GESTIÓN ===============

    def agregar_bloqueado(self, email):
        """Agrega un email a la lista de bloqueados."""
        self.remitentes_bloqueados.add(email)

    def quitar_bloqueado(self, email):
        """Elimina un email de la lista de bloqueados."""
        self.remitentes_bloqueados.discard(email)

    # =============== APLICAR FILTRO ===============

    def aplicar(self, mensaje):
        """
        Analiza un mensaje y devuelve el nombre de la carpeta donde debe ir.
        Devuelve:
            - 'Bloqueados' si el remitente está bloqueado
            - 'Spam' si contiene palabras sospechosas
            - 'Inbox' si pasa los filtros
        """

        #Filtro de bloqueados
        if mensaje.emisor in self.remitentes_bloqueados:
            return "Bloqueados"

        #Filtro SPAM por palabras
        contenido = mensaje.contenido.lower()
        if any(pal in contenido for pal in self.palabras_spam):
            return "Spam"

        #Si no entra en ningún filtro, va al Inbox
        return "Inbox"