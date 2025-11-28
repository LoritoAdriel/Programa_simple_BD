from .base_model import BaseModel

class Funcion(BaseModel):
    def create(self, id_pelicula, id_sala, fecha, hora_inicio, hora_fin):
        q = ("INSERT INTO Funciones (id_pelicula, id_sala, fecha, hora_inicio, hora_fin) "
             "VALUES (%s,%s,%s,%s,%s)")
        return self._execute(q, (id_pelicula, id_sala, fecha, hora_inicio, hora_fin))

    def list_all(self):
        q = ("SELECT f.id_funcion, p.titulo, s.numero_sala, f.fecha, f.hora_inicio, f.hora_fin "
             "FROM Funciones f JOIN Peliculas p ON f.id_pelicula = p.id_pelicula "
             "JOIN Salas s ON f.id_sala = s.id_sala")
        return self._execute(q, fetch=True)
    
    def get_by_id(self, id_funcion):
        query = "SELECT * FROM funciones WHERE id_funcion = %s"
        resultados = self._execute(query, (id_funcion,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_funcion, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_funcion]
        query = f"UPDATE funciones SET {campos} WHERE id_funcion = %s"
        return self._execute(query, valores)
        
    def get_funciones(self, id_pelicula, id_sucursal):
        query = """
            SELECT f.id_funcion, f.fecha, f.hora_inicio,
                   s.id_sala, s.numero_sala,
                   su.id_sucursal, su.nombre 
            FROM funciones f
            JOIN salas s ON f.id_sala = s.id_sala
            JOIN sucursales su ON s.id_sucursal = su.id_sucursal
            WHERE f.id_pelicula = %s
              AND su.id_sucursal = %s
            ORDER BY f.fecha;
        """
        params = (id_pelicula, id_sucursal)
        return self._execute(query, params, fetch=True)