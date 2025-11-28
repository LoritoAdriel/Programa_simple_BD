from .base_model import BaseModel

class Asiento(BaseModel):
    def create(self, id_sala, fila, numero_asiento, estado='disponible'):
        q = "INSERT INTO Asientos (id_sala, fila, numero_asiento, estado) VALUES (%s, %s, %s, %s)"
        return self._execute(q, (id_sala, fila, numero_asiento, estado))

    def list_all(self):
        q = "SELECT * FROM Asientos"
        return self._execute(q, fetch=True)
    
    def get_by_id(self, id_asiento):
        query = "SELECT * FROM asientos WHERE id_asiento = %s"
        resultados = self._execute(query, (id_asiento,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_asiento, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_asiento]
        query = f"UPDATE asientos SET {campos} WHERE id_asiento = %s"
        return self._execute(query, valores)
        
    def get_disponibles(self, id_funcion):
        query = """
            SELECT a.id_asiento, a.fila, a.numero_asiento
            FROM Asientos a
            JOIN Funciones f ON a.id_sala = f.id_sala
            WHERE f.id_funcion = %s
              AND a.estado = 'disponible'
              AND a.id_asiento NOT IN (
                    SELECT e.id_asiento
                    FROM Entradas e
                    WHERE e.id_funcion = %s
              )
            ORDER BY a.fila, a.numero_asiento;
        """
        
        params = (id_funcion, id_funcion)
        return self._execute(query, params, fetch=True)