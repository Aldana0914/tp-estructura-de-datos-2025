from collections import deque
from typing import Dict, List, Optional

class RedServidores:
    def _init_(self):
        # Mapa nombre_servidor -> instancia ServidorCorreo
        self.servidores: Dict[str, object] = {}
        # Lista de adyacencia: nombre_servidor -> set de nombres de servidores conectados
        self.adyacencia: Dict[str, set] = {}

    # -----------------------
    # Gestión de servidores
    # -----------------------
    def agregar_servidor(self, servidor):
        """
        Agrega un servidor (nodo) a la red.
        servidor debe tener el atributo nombre (string).
        """
        nombre = servidor.nombre
        if nombre in self.servidores:
            return  # ya existe
        self.servidores[nombre] = servidor
        self.adyacencia[nombre] = set()

    def eliminar_servidor(self, nombre):
        """Elimina un servidor y todas sus conexiones."""
        if nombre not in self.servidores:
            return
        # eliminar de la adyacencia de otros
        for vecino in list(self.adyacencia[nombre]):
            self.adyacencia[vecino].discard(nombre)
        # eliminar entradas
        del self.adyacencia[nombre]
        del self.servidores[nombre]

    # -----------------------
    # Gestión de conexiones
    # -----------------------
    def conectar(self, nombre_a: str, nombre_b: str):
        """Crea una conexión bidireccional entre dos servidores existentes."""
        if nombre_a not in self.servidores or nombre_b not in self.servidores:
            raise ValueError("Ambos servidores deben existir en la red antes de conectar.")
        self.adyacencia[nombre_a].add(nombre_b)
        self.adyacencia[nombre_b].add(nombre_a)

    def desconectar(self, nombre_a: str, nombre_b: str):
        """Elimina la conexión entre dos servidores (si existe)."""
        self.adyacencia.get(nombre_a, set()).discard(nombre_b)
        self.adyacencia.get(nombre_b, set()).discard(nombre_a)

    # -----------------------
    # Búsqueda de ruta: BFS y DFS
    # -----------------------
    def bfs_camino(self, origen: str, destino: str) -> Optional[List[str]]:
        """
        Encuentra el camino más corto (en número de aristas) entre origen y destino usando BFS.
        Devuelve la lista de nombres de servidores en el camino (incluyendo origen y destino),
        o None si no hay ruta.
        """
        if origen not in self.servidores or destino not in self.servidores:
            return None

        visitado = set()
        padre = {}  # para reconstruir ruta
        cola = deque([origen])
        visitado.add(origen)

        while cola:
            actual = cola.popleft()
            if actual == destino:
                # reconstruir ruta
                ruta = []
                nodo = destino
                while nodo:
                    ruta.append(nodo)
                    nodo = padre.get(nodo)
                ruta.reverse()
                return ruta

            for vecino in self.adyacencia[actual]:
                if vecino not in visitado:
                    visitado.add(vecino)
                    padre[vecino] = actual
                    cola.append(vecino)
        return None

    def dfs_camino(self, origen: str, destino: str) -> Optional[List[str]]:
        """
        Busca *algún* camino entre origen y destino usando DFS recursivo.
        No garantiza el camino más corto. Devuelve lista de nombres o None.
        """
        if origen not in self.servidores or destino not in self.servidores:
            return None

        visitado = set()
        camino = []

        def dfs(nodo):
            if nodo == destino:
                camino.append(nodo)
                return True
            visitado.add(nodo)
            for vecino in self.adyacencia[nodo]:
                if vecino not in visitado:
                    if dfs(vecino):
                        camino.append(nodo)
                        return True
            return False

        if dfs(origen):
            camino.reverse()
            return camino
        return None

    # -----------------------
    # Buscar usuario en la red
    # -----------------------
    def encontrar_servidor_por_usuario(self, email: str) -> Optional[str]:
        """
        Recorre todos los servidores y usa su método buscar_usuario_por_email(email)
        para determinar en qué servidor está ese usuario (si existe).
        Devuelve el nombre del servidor o None si no se encuentra.
        """
        for nombre, servidor in self.servidores.items():
            # asumimos que cada ServidorCorreo tiene buscar_usuario_por_email
            usuario = servidor.buscar_usuario_por_email(email)
            if usuario is not None:
                return nombre
        return None

    # -----------------------
    # Simulación de envío de mensaje por la red
    # -----------------------
    def enviar_mensaje_red(self, origen_nombre: str, destino_email: str, mensaje):
        """
        Simula el ruteo de mensaje desde origen_nombre hasta el servidor
        donde vive destino_email. Usa BFS (camino más corto).
        - Imprime los saltos.
        - Si encuentra al usuario en el servidor destino, entrega el mensaje
          usando usuario.recibir_mensaje(mensaje).
        - Si no hay ruta o no existe el usuario, informa el error.
        """
        if origen_nombre not in self.servidores:
            print(f"[Red] Servidor origen '{origen_nombre}' no existe en la red.")
            return False

        destino_servidor_nombre = self.encontrar_servidor_por_usuario(destino_email)
        if destino_servidor_nombre is None:
            print(f"[Red] El destinatario '{destino_email}' no existe en la red.")
            return False

        # obtener ruta usando BFS (corto en saltos)
        ruta = self.bfs_camino(origen_nombre, destino_servidor_nombre)
        if ruta is None:
            print(f"[Red] No hay ruta entre '{origen_nombre}' y '{destino_servidor_nombre}'.")
            return False

        # Simular recorrido
        print(f"[Red] Ruta encontrada: {' -> '.join(ruta)}")
        for salto in ruta:
            print(f"[Red] paquetes pasando por: {salto}")

        # Entregar el mensaje en el servidor destino
        servidor_dest = self.servidores[destino_servidor_nombre]
        usuario_dest = servidor_dest.buscar_usuario_por_email(destino_email)
        if usuario_dest:
            usuario_dest.recibir_mensaje(mensaje)
            print(f"[Red] Mensaje entregado a {destino_email} en servidor '{destino_servidor_nombre}'.")
            return True
        else:
            # Esto no debería pasar si encontrar_servidor_por_usuario devolvió ese servidor
            print(f"[Red] Error: no se pudo encontrar al usuario en el servidor destino.")
            return False