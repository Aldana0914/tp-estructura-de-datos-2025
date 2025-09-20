# tp-estructura-de-datos-2025
aldana y marko
# Sistema de Gestión de Correos en Python
Este proyecto simula un sistema simple de mensajería (entre usuarios) utilizando programación orientada a objetos. Incluye funciones para poder enviar, recibir, listar y organizar mensajes en carpetas que corresponden a una bandeja de entrada.

# Descripción
El sistema simula el comportamiento de un servidor de correo y la interacción de sus usuarios. Cada usuario puede enviar y recibir mensajes, los cuales se almacenan en carpetas específicas. El diseño está basado en principios de abstracción, encapsulamiento y herencia.

# Tecnologías utilizadas
- Python 3.x
- Programación orientada a objetos (OOP)
- Módulo abc para clases abstractas

# Estructura del proyecto
- GestionCorreo: Interfaz abstracta que define los métodos esenciales para la gestión de correos.
- ServidorCorreo: Clase que representa el servidor, gestiona usuarios registrados.
- Usuario: Implementa la interfaz GestionCorreo, representa un usuario con su email y carpetas.
- Mensaje: Clase que modela un mensaje con emisor, destinatarios, asunto y contenido.
- Carpeta: Clase que gestiona los mensajes dentro de una carpeta específica.

# Proceso de elaboración del programa.
1. Inconvenientes para acceder al repositorio remoto para que cada uno pueda trabajar y visualizar el codigo del compañero.
2. Se trabajó en archivos diferentes (individuales) hasta poder reunir el codigo en el repositorio.
3. Durante el primer día se estableció la base principal del codigo, este incluia las distintas clases a utilizar (GestionCorreo(interfaz), ServidorCorreo, Usuario, Mensaje, Carpeta).
4. Posteriormente se implementaron los atributos y los distintos metodos para cada clase.
5. Una vez concluida la estructuración del código se paso a la fase de elaboración del diagrama en base al codigo para poder visualizar la relación entre las clases.
