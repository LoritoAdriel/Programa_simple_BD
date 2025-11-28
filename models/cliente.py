from .base_model import BaseModel

class Cliente(BaseModel):
    def create(self, nombre, apellido, dni, fecha_nacimiento=None, telefono=None, email=None):
        q = ("INSERT INTO Clientes (nombre, apellido, dni, fecha_nacimiento, telefono, email) "
             "VALUES (%s,%s,%s,%s,%s,%s)")
        return self._execute(q, (nombre, apellido, dni, fecha_nacimiento, telefono, email))

    def list_all(self):
        q = "SELECT id_cliente, nombre, apellido, dni FROM Clientes"
        return self._execute(q, fetch=True)
    
    def get_by_dni(self, dni):
        query = "SELECT * FROM clientes WHERE dni = %s"
        resultados = self._execute(query, (dni,), fetch=True)
        return resultados[0] if resultados else None
    
    def get_by_id(self, id_cliente):
        query = "SELECT * FROM clientes WHERE id_cliente = %s"
        resultados = self._execute(query, (id_cliente,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_cliente, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_cliente]
        query = f"UPDATE clientes SET {campos} WHERE id_cliente = %s"
        return self._execute(query, valores)