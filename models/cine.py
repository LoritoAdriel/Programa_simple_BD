from .base_model import BaseModel

class Cine(BaseModel):
    def create(self, nombre, direccion, cuit):
        q = "INSERT INTO Cine (nombre, direccion, cuit) VALUES (%s, %s, %s)"
        return self._execute(q, (nombre, direccion, cuit))

    def list_all(self):
        q = "SELECT id_cine, nombre, direccion, cuit FROM Cine"
        return self._execute(q, fetch=True)
    
    def get_by_id(self, id_cine):
        query = "SELECT * FROM cine WHERE id_cine = %s"
        resultados = self._execute(query, (id_cine,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_cine, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_cine]
        query = f"UPDATE cine SET {campos} WHERE id_cine = %s"
        return self._execute(query, valores)