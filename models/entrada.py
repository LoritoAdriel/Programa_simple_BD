from .base_model import BaseModel

class Entrada(BaseModel):
    def create(self, id_venta, id_funcion, id_asiento, id_tarifa, precio):
        q = ("INSERT INTO Entradas (id_venta, id_funcion, id_asiento, id_tarifa, precio) "
             "VALUES (%s,%s,%s,%s,%s)")
        return self._execute(q, (id_venta, id_funcion, id_asiento, id_tarifa, precio))

    def list_all(self):
        q = ("SELECT e.id_entrada, v.id_venta, p.titulo, s.numero_sala, a.fila, a.numero_asiento, t.nombre, e.precio "
             "FROM Entradas e "
             "JOIN Ventas v ON e.id_venta = v.id_venta "
             "JOIN Funciones f ON e.id_funcion = f.id_funcion "
             "JOIN Peliculas p ON f.id_pelicula = p.id_pelicula "
             "JOIN Salas s ON f.id_sala = s.id_sala "
             "JOIN Asientos a ON e.id_asiento = a.id_asiento "
             "JOIN Tarifas t ON e.id_tarifa = t.id_tarifa")
        return self._execute(q, fetch=True)
    
    def get_by_id(self, id_entrada):
        query = "SELECT * FROM entradas WHERE id_entrada = %s"
        resultados = self._execute(query, (id_entrada,), fetch=True)
        return resultados[0] if resultados else None
    
    def update(self, id_entrada, data):
        campos = ", ".join([f"{col} = %s" for col in data.keys()])
        valores = list(data.values()) + [id_entrada]
        query = f"UPDATE entradas SET {campos} WHERE id_entrada = %s"
        return self._execute(query, valores)