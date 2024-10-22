from db.connection import DBConnection

class DatabaseManager:
    def __init__(self):
        self.db_connection = DBConnection()
        self.db_connection.connect()
        self.conn = self.db_connection.get_connection()

    def execute_select(self, query: str):
        """Ejecuta una consulta SELECT."""
        if not self.conn:
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Exception as ex:
            print(f"Error al ejecutar SELECT: {ex}")
            return None

    def execute_insert(self, query: str):
        """Ejecuta una consulta INSERT."""
        if not self.conn:
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            print("Inserción exitosa")
        except Exception as ex:
            print(f"Error al ejecutar INSERT: {ex}")