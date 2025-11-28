from .base_model import BaseModel

class Tarifa(BaseModel):
    def create(self, nombre, precio_fijo, valor_descuento, tipo_descuento, categoria_base, estado='Disponible'):
        q = ("INSERT INTO Tarifas (nombre, precio_fijo, valor_descuento, tipo_descuento, categoria_base, estado) "
             "VALUES (%s,%s,%s,%s,%s,%s)")
        return self._execute(q, (nombre, precio_fijo, valor_descuento, tipo_descuento, categoria_base, estado))

    def list_all(self):
        q = "SELECT * FROM Tarifas"
        return self._execute(q, fetch=True)
    
    def get_by_id(self, id_tarifa):
        query = "SELECT * FROM tarifas WHERE id_tarifa = %s"
        resultados = self._execute(query, (id_tarifa,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_tarifa, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_tarifa]
        query = f"UPDATE tarifas SET {campos} WHERE id_tarifa = %s"
        return self._execute(query, valores)