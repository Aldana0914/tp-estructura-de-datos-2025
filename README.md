# tp-estructura-de-datos-2025
Aldana Ibarra y Marco de Hoyos

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


# Diagrama de Flujo (en imagen)

![alt text](ServidorCorreo.jpg)

Entrega 2: Estructuras de Datos y Recursividad

Se implementó un sistema de carpetas y subcarpetas usando una estructura recursiva tipo árbol, donde cada carpeta puede contener mensajes y otras carpetas dentro.

El programa permite:

Crear y eliminar carpetas.

Agregar, eliminar y mover mensajes entre carpetas.

Realizar búsquedas recursivas de mensajes por asunto o remitente.

Cada carpeta es un nodo del árbol que contiene una lista de mensajes y una lista de subcarpetas.
Las búsquedas y movimientos se hacen de forma recursiva, recorriendo todo el árbol.

En cuanto a eficiencia:

Crear carpetas o agregar mensajes.

Búsquedas y movimientos recursivos.

## Entrega 3 de Programación Orientada a Objetos. 31/10 - 01/11
El trabajo consistió en crear un *simulador de correo electrónico* aplicando los conceptos de clases, herencia, composición y polimorfismo en Python.

Durante el desarrollo tuvimos varios desafíos. Al principio, nos costó organizarnos con la estructura de las clases y cómo hacer que los filtros funcionaran correctamente. Fuimos probando distintas maneras de aplicar el filtrado de spam y bloqueados, hasta lograr que el sistema los clasificara automáticamente en las carpetas correspondientes.

También tuvimos que ajustar cómo se manejaban los mensajes urgentes, para que se procesaran en el orden correcto sin interferir con los mensajes comunes.

En mi caso, *no tengo computadora en este momento porque se me rompió*, así que gran parte del trabajo lo hicimos de forma colaborativa:
yo le fui pasando a Marcos toda la información, las ideas del diseño y las pruebas que quería que hiciera. Nos conectamos varias veces para revisar el código juntos y hacer los cambios necesarios. Marcos fue quien se encargó de escribir y probar el código en su máquina, mientras que yo me dediqué más a revisar la lógica, la estructura y la documentación.

A pesar de las dificultades técnicas, logramos terminar el simulador completo y funcional. Aprendimos bastante sobre cómo organizar un proyecto grande con varias clases, y sobre cómo trabajar en equipo a distancia, compartiendo ideas y responsabilidades.

---

## 📌 Descripción del Sistema

El sistema permite simular el manejo de un correo electrónico con funcionalidades básicas como:

### 👤 Usuarios (`usuario.py`)
Cada usuario tiene:
- Un nombre y dirección de email
- Una referencia al servidor al que pertenece
- Tres carpetas por defecto:
  - Inbox (mensajes recibidos)
  - Enviados
  - Papelera

✅ **Envia y recibe mensajes**  
✅ **Puede mover mensajes entre carpetas**  
✅ **Accede a sus carpetas y subcarpetas**  

---

### 📬 Mensajes (`mensaje.py`)
Cada mensaje incluye:
- Emisor
- Lista de destinatarios
- Asunto
- Contenido del mensaje

No incluye fechas ni IDs automáticos (simple y directo).

---

### 🗂️ Carpetas y Subcarpetas (`carpeta.py`)
Las carpetas:
- Guardan mensajes
- Pueden tener subcarpetas
- Pueden buscar mensajes de manera **recursiva**
- Soportan mover mensajes de una carpeta a otra (también recursivo)

#### ✅ Funcionalidades clave:
| Acción                         | Soporte |
|--------------------------------|---------|
| Agregar mensaje                | ✅      |
| Eliminar mensaje               | ✅      |
| Agregar subcarpeta             | ✅      |
| Buscar mensaje (asunto / texto / emisor) | ✅ (recursivo) |
| Mover mensaje entre carpetas/subcarpetas | ✅ (recursivo) |

> Nota: Si el mensaje no se encuentra, el método **no falla**, solo no hace nada.

---

### 🖥️ Servidor (`servidor.py`)
Administración de usuarios en un servidor de correo.

- Agrega y elimina usuarios
- Devuelve todos los usuarios registrados

---

---

###  Red.py (Grafos)

Simula una red de servidores interconectados (grafo).
*Funciones principales:*

* agregar_servidor(servidor) → añade un servidor a la red.
* conectar_servidores(nombre1, nombre2) → conecta dos servidores.
* recorrido_bfs(inicio) → recorre la red utilizando el algoritmo BFS, mostrando los servidores visitados.

---

###  ColaPrioridad.py

Maneja una *cola de prioridad* para los mensajes urgentes.
*Funciones principales:*

* agregar(mensaje) → inserta mensajes, dando prioridad a los urgentes.
* procesar() → procesa los mensajes en orden de prioridad.

---

### Filtros.py

Contiene filtros automáticos que clasifican los mensajes.
*Subclases:*

* FiltroSpam → busca palabras prohibidas y envía los mensajes a la carpeta “Spam”.
* FiltroBloqueados → bloquea mensajes cuyo emisor esté en la lista negra.

Ambos heredan de la clase abstracta Filtro, que define el método aplicar().

---

### SimuladorCorreo.py`

Archivo principal que integra todas las clases.
Incluye una función demo() que ejecuta una simulación completa:

1. Crea servidores y usuarios.
2. Aplica filtros a un usuario.
3. Envía distintos tipos de mensajes (normales, spam y urgentes).
4. Procesa la cola de urgentes.
5. Muestra las bandejas de mensajes y el recorrido de la red de servidores.

#Conceptos aplicados

* *Encapsulamiento:* manejo interno de atributos dentro de cada clase.
* *Herencia:* los filtros heredan de una clase base.
* *Polimorfismo:* distintos filtros implementan el mismo método aplicar().
* *Composición:* un usuario contiene carpetas, filtros y una cola de prioridad.
* *Abstracción:* se modelan entidades reales (usuario, mensaje, servidor, red)