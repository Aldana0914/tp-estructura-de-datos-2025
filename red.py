from collections import deque
from typing import Dict, List, Optional

class RedServidores:
    def _init_(self):
        self.servidores: Dict[str, object] = {}
        self.adyacencia: Dict[str, set] = {}

    def agregar_servidor(self, servidor):
        nombre = servidor.nombre
        if nombre in self.servidores:
            return 
        self.servidores[nombre] = servidor
        self.adyacencia[nombre] = set()

    def eliminar_servidor(self, nombre):
        if nombre not in self.servidores:
            return
        for vecino in list(self.adyacencia[nombre]):
            self.adyacencia[vecino].discard(nombre)
        del self.adyacencia[nombre]
        del self.servidores[nombre]

    def conectar(self, nombre_a: str, nombre_b: str):
        if nombre_a not in self.servidores or nombre_b not in self.servidores:
            raise ValueError("Ambos servidores deben existir en la red antes de conectar.")
        self.adyacencia[nombre_a].add(nombre_b)
        self.adyacencia[nombre_b].add(nombre_a)

    def desconectar(self, nombre_a: str, nombre_b: str):
        self.adyacencia.get(nombre_a, set()).discard(nombre_b)
        self.adyacencia.get(nombre_b, set()).discard(nombre_a)

    def bfs_camino(self, origen: str, destino: str) -> Optional[List[str]]:
        if origen not in self.servidores or destino not in self.servidores:
            return None

        visitado = set()
        padre = {}  
        cola = deque([origen])
        visitado.add(origen)

        while cola:
            actual = cola.popleft()
            if actual == destino:
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

    def encontrar_servidor_por_usuario(self, email: str) -> Optional[str]:
        for nombre, servidor in self.servidores.items():
            usuario = servidor.buscar_usuario_por_email(email)
            if usuario:
                return nombre
        return None

    def enviar_mensaje_red(self, origen_nombre: str, destino_email: str, mensaje):
        if origen_nombre not in self.servidores:
            print(f"[Red] Servidor origen '{origen_nombre}' no existe.")
            return False

        destino_servidor_nombre = self.encontrar_servidor_por_usuario(destino_email)
        if destino_servidor_nombre is None:
            print(f"[Red] Destinatario '{destino_email}' no existe en la red.")
            return False

        ruta = self.bfs_camino(origen_nombre, destino_servidor_nombre)
        if ruta is None:
            print(f"[Red] No hay ruta entre '{origen_nombre}' y '{destino_servidor_nombre}'.")
            return False

        print(f"[Red] Ruta: {' -> '.join(ruta)}")
        for salto in ruta:
            print(f"[Red] Paquete pasando por: {salto}")

        servidor_dest = self.servidores[destino_servidor_nombre]
        usuario_dest = servidor_dest.buscar_usuario_por_email(destino_email)
        if usuario_dest:
            usuario_dest.recibir_mensaje(mensaje)
            print(f"[Red] Mensaje entregado a {destino_email} en servidor '{destino_servidor_nombre}'.")
            return True
        else:
            print("[Red] Error: no se pudo encontrar al usuario en el servidor destino.")
            return False