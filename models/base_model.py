class BaseModel:
    def __init__(self, db):
        self.db = db

    def _execute(self, query, params=None, fetch=False):
        conn = self.db.get_connection()
        if conn is None:
            return None
        
        cursor = conn.cursor(dictionary=True)  # <-- CLAVE
        cursor.execute(query, params or ())
        
        if fetch:
            datos = cursor.fetchall()
            cursor.close()
            conn.close()
            return datos
        
        conn.commit()
        cursor.close()
        conn.close()
        return None
