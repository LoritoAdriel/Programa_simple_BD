from .base_model import BaseModel
from datetime import date

class Venta(BaseModel):
    def create(self, id_cliente, fecha_venta, total_venta, tipo_pago):
        q = ("INSERT INTO Ventas (id_cliente, fecha_venta, total_venta, tipo_pago) "
             "VALUES (%s,%s,%s,%s)")
        return self._execute(q, (id_cliente, fecha_venta, total_venta, tipo_pago))

    def list_all(self):
        q = "SELECT id_venta, id_cliente, fecha_venta, total_venta, tipo_pago FROM Ventas"
        return self._execute(q, fetch=True)
    
    def list_end_id(self):
        q = "SELECT id_venta, id_cliente, fecha_venta, total_venta, tipo_pago FROM Ventas"
        resultados = self._execute(q, fetch=True)
        return len(resultados)-1
    
    def get_by_id(self, id_venta):
        query = "SELECT * FROM ventas WHERE id_venta = %s"
        resultados = self._execute(query, (id_venta,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_venta, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_venta]
        query = f"UPDATE ventas SET {campos} WHERE id_venta = %s"
        return self._execute(query, valores)