from db.queries import DatabaseManager

# Inicializar el administrador de la base de datos
db_manager = DatabaseManager()

# Ejecutar SELECT
select_query = "SELECT * FROM SGSSDB.PLACORD"
result = db_manager.execute_select(select_query)

# Mostrar resultados
if result:
    for row in result:
        print(row)

# Cerrar conexión
db_manager.db_connection.close()
