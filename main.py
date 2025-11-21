from usuario import Usuario
from ServidorCorreo import ServidorCorreo
from red import RedServidores
from mensaje import Mensaje
from carpeta import Carpeta
from ServidorCorreo import ServidorCorreo  

# 1. Crear servidores de correo
servidor1 = ServidorCorreo("Servidor1")
servidor2 = ServidorCorreo("Servidor2")

# 2. Crear red y conectar servidores
red = RedServidores()
red.agregar_servidor(servidor1)
red.agregar_servidor(servidor2)
red.conectar("Servidor1", "Servidor2")

# Asignar red a los servidores
servidor1.red = red
servidor2.red = red

# 3. Crear usuarios
usuario1 = Usuario("Alice", "alice@example.com", servidor1)
usuario2 = Usuario("Bob", "bob@example.com", servidor2)
usuario3 = Usuario("Eve", "eve@example.com", servidor2)

# Agregar usuarios a los servidores
servidor1.agregar_usuario(usuario1)
servidor2.agregar_usuario(usuario2)
servidor2.agregar_usuario(usuario3)

# 4. Bloquear a Eve
servidor2.filtro.agregar_bloqueado("eve@example.com")

# 5. Enviar mensajes
usuario1.enviar_mensaje(["bob@example.com"], "Hola Bob", "Este es un mensaje normal")
usuario1.enviar_mensaje(["eve@example.com"], "Hola Eve", "Mensaje bloqueado")
usuario1.enviar_mensaje(["bob@example.com"], "Oferta increíble", "Gana dinero rápido")

# 6. Acceder a mensajes de cada carpeta (para uso interno o pruebas)
inbox_bob = usuario2.listar_mensaje("Inbox")
spam_bob = usuario2.listar_mensaje("Spam")
bloqueados_eve = usuario3.listar_mensaje("Bloqueados")