from usuario import Usuario
from servidor import Servidor
from mensaje import Mensaje

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Crear usuario")
    print("2. Enviar mensaje")
    print("3. Recibir mensaje")
    print("4. Listar mensajes de una carpeta")
    print("5. Mover mensaje")
    print("6. Salir")

def main():
    servidor = Servidor()
    usuario = None

    opcion = 0
    while opcion != 6:
        mostrar_menu()

        try:
            opcion = int(input("Elegí una opción: "))
        except ValueError:
            print("Ingresá un número válido.")
            continue

        # 1. Crear usuario
        if opcion == 1:
            nombre = input("Nombre: ")
            email = input("Email: ")
            usuario = Usuario(nombre, email, servidor)
            print("Usuario creado con éxito.")

        # 2. Enviar mensaje
        elif opcion == 2:
            if usuario is None:
                print("Primero creá un usuario.")
                continue

            dest = input("Destinatario: ")
            asunto = input("Asunto: ")
            contenido = input("Contenido: ")

            usuario.enviar_mensaje(dest, asunto, contenido)

        # 3. Recibir mensaje
        elif opcion == 3:
            if usuario is None:
                print("Primero creá un usuario.")
                continue

            remitente = input("Remitente: ")
            asunto = input("Asunto: ")
            contenido = input("Contenido: ")

            mensaje = Mensaje(remitente, usuario.email, asunto, contenido)
            usuario.recibir_mensaje(mensaje)

        # 4. Listar mensajes
        elif opcion == 4:
            if usuario is None:
                print("Primero creá un usuario.")
                continue

            carpeta = input("Carpeta a listar: ")

            mensajes = usuario.listar_mensaje(carpeta)

            if not mensajes:
                print("No hay mensajes.")
            else:
                for i, m in enumerate(mensajes, 1):
                    print(f"{i}. De: {m.remitente} | Asunto: {m.asunto}")

        # 5. Mover mensaje
        elif opcion == 5:
            if usuario is None:
                print("Primero creá un usuario.")
                continue

            origen = input("Carpeta origen: ")
            destino = input("Carpeta destino: ")

            mensajes = usuario.listar_mensaje(origen)

            if not mensajes:
                print("No hay mensajes para mover.")
                continue

            print("Seleccioná el número del mensaje:")
            for i, m in enumerate(mensajes, 1):
                print(f"{i}. {m.asunto}")

            try:
                idx = int(input("Número: ")) - 1
                mensaje = mensajes[idx]
            except:
                print("Número inválido.")
                continue

            usuario.mover_mensaje(mensaje, origen, destino)
            print("Mensaje movido.")

        # 6. Salir
        elif opcion == 6:
            print("Saliendo...")

        else:
            print("Opción no válida.")

        if __name__ == "__main__":
            main()