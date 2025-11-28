from .base_model import BaseModel

class Sala(BaseModel):
    def create(self, id_sucursal, numero_sala, capacidad_total, tipo_sala):
        q = "INSERT INTO Salas (id_sucursal, numero_sala, capacidad_total, tipo_sala) VALUES (%s, %s, %s, %s)"
        return self._execute(q, (id_sucursal, numero_sala, capacidad_total, tipo_sala))

    def list_all(self):
        q = "SELECT id_sala, id_sucursal, numero_sala, capacidad_total, tipo_sala FROM Salas"
        return self._execute(q, fetch=True)
    
    def get_by_id(self, id_sala):
        query = "SELECT * FROM salas WHERE id_sala = %s"
        resultados = self._execute(query, (id_sala,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_sala, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_sala]
        query = f"UPDATE salas SET {campos} WHERE id_sala = %s"
        return self._execute(query, valores)