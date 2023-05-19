<!DOCTYPE html>
<html>
<body>
  <h1>Trabajo Práctico Obligatorio 2</h1>
  
  <h2>Crear una aplicación de línea de comandos para administrar una lista de tareas.</h2>
  <p>La aplicación permitirá al usuario agregar, ver, actualizar y eliminar tareas.</p>
  
  <h3>Requisitos:</h3>
  <ul>
    <li>Utiliza TinyDB para almacenar las tareas en una base de datos.</li>
    <li>Crea una clase Tarea que tenga las siguientes propiedades: id, titulo, descripción, estado, creada y actualizada.</li>
    <li>Crea una clase Administrador de Tareas (AdminTarea) que maneje la interacción con la base de datos TinyDB. La clase debe tener los siguientes métodos:</li>
  </ul>
  
  <h4>Métodos de la clase Administrador de Tareas (AdminTarea):</h4>
  <ul>
    <li>Agregar_tarea(tarea: Tarea) -> int: Agrega una nueva tarea a la base de datos y devuelve su ID.</li>
    <li>Traer_tarea(tarea_id: int) -> Task: Obtiene una tarea de la base de datos según su ID y devuelve una instancia de la clase Tarea.</li>
    <li>Actualizar_estado_tarea(tarea_id: int, estado: str): Actualiza el estado de una tarea en la base de datos según su ID.</li>
    <li>Eliminar_tarea(tarea_id: int): Elimina una tarea de la base de datos según su ID.</li>
    <li>Traer_todas_tareas() -> List[Tarea]: Obtiene todas las tareas de la base de datos y devuelve una lista de instancias de la clase Task.</li>
  </ul>
</body>
</html>