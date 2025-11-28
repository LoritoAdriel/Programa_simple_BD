from .base_model import BaseModel

class Pelicula(BaseModel):
    def create(self, titulo, reparto, sinopsis, duracion, genero, clasificacion, valoracion):
        q = ("INSERT INTO Peliculas (titulo, reparto, sinopsis, duracion, genero, clasificacion, valoracion) "
             "VALUES (%s,%s,%s,%s,%s,%s,%s)")
        return self._execute(q, (titulo, reparto, sinopsis, duracion, genero, clasificacion, valoracion))

    def list_all(self):
        q = "SELECT id_pelicula, titulo, duracion, genero, clasificacion, valoracion FROM Peliculas"
        return self._execute(q, fetch=True)
    
    def get_by_id(self, id_pelicula):
        query = "SELECT * FROM peliculas WHERE id_pelicula = %s"
        resultados = self._execute(query, (id_pelicula,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_pelicula, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_pelicula]
        query = f"UPDATE peliculas SET {campos} WHERE id_pelicula = %s"
        return self._execute(query, valores)