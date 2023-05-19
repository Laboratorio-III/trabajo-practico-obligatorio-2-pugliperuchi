from tinydb import TinyDB, Query
from typing import List

class Tarea:
    def __init__(self, id, titulo, descripcion, estado, creada, actualizada):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.creada = creada
        self.actualizada = actualizada

class AdminTarea:
    def __init__(self, db_file):
        self.db = TinyDB(db_file)
        self.tareas_table = self.db.table('tareas')

    def agregar_tarea(self, tarea: Tarea) -> int:
        tarea_dict = vars(tarea)
        tarea_id = self.tareas_table.insert(tarea_dict)
        return tarea_id

    def traer_tarea(self, tarea_id: int) -> Tarea:
        tarea_dict = self.tareas_table.get(doc_id=tarea_id)
        tarea = Tarea(**tarea_dict)
        return tarea

    def actualizar_estado_tarea(self, tarea_id: int, estado: str):
        self.tareas_table.update({'estado': estado}, doc_ids=[tarea_id])

    def eliminar_tarea(self, tarea_id: int):
        self.tareas_table.remove(doc_ids=[tarea_id])

    def traer_todas_tareas(self) -> List[Tarea]:
        tareas_dict = self.tareas_table.all()
        tareas = [Tarea(**tarea) for tarea in tareas_dict]
        return tareas

if __name__ == "__main__":
    admin_tareas = AdminTarea('tareas_db.json')

    
    tarea1 = Tarea(1, 'Tarea 1', 'Descripción de la tarea 1', 'pendiente', '2023-05-19', '2023-05-19')
    tarea1_id = admin_tareas.agregar_tarea(tarea1)
    print(f"Tarea agregada con ID: {tarea1_id}")

    
    tarea_recuperada = admin_tareas.traer_tarea(tarea1_id)
    print("Tarea recuperada:")
    print(f"ID: {tarea_recuperada.id}")
    print(f"Título: {tarea_recuperada.titulo}")
    print(f"Descripción: {tarea_recuperada.descripcion}")
    print(f"Estado: {tarea_recuperada.estado}")
    print(f"Creada: {tarea_recuperada.creada}")
    print(f"Actualizada: {tarea_recuperada.actualizada}")

    admin_tareas.actualizar_estado_tarea(tarea1_id, 'completada')
    print("Estado de la tarea actualizado")

    admin_tareas.eliminar_tarea(tarea1_id)
    print("Tarea eliminada")

    todas_tareas = admin_tareas.traer_todas_tareas()
    print("Todas las tareas:")
    for tarea in todas_tareas:
        print(f"ID: {tarea.id}")
        print(f"Título: {tarea.titulo}")
        print(f"Descripción: {tarea.descripcion}")
        print(f"Estado: {tarea.estado}")
        print(f"Creada: {tarea.creada}")
        print(f"Actualizada: {tarea.actualizada}")