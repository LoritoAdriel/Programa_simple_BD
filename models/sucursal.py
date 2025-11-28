from .base_model import BaseModel

class Sucursal(BaseModel):
    def create(self, nombre, direccion, numero_sucursal, id_cine):
        q = "INSERT INTO Sucursales (nombre, direccion, numero_sucursal, id_cine) VALUES (%s, %s, %s, %s)"
        return self._execute(q, (nombre, direccion, numero_sucursal, id_cine))

    def list_all(self):
        q = "SELECT id_sucursal, nombre, direccion, numero_sucursal, id_cine FROM Sucursales"
        return self._execute(q, fetch=True)
    
    def get_by_id(self, id_sucursal):
        query = "SELECT * FROM sucursales WHERE id_sucursal = %s"
        resultados = self._execute(query, (id_sucursal,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_sucursal, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_sucursal]
        query = f"UPDATE sucursales SET {campos} WHERE id_sucursal = %s"
        return self._execute(query, valores)
        
    def get_peliculas_disponibles(self, id_sucursal):
        query = """
            SELECT DISTINCT p.*
            FROM Peliculas p
            JOIN Funciones f ON p.id_pelicula = f.id_pelicula
            JOIN Salas s ON f.id_sala = s.id_sala
            WHERE s.id_sucursal = %s
        """
        return self._execute(query, (id_sucursal,), fetch=True)