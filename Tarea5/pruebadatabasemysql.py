

import mysql.connector



def conectar():
    host = "sql10.freesqldatabase.com"
    user = "sql10689405"
    password = "ACM1wVFXPb"
    database = "sql10689405"

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def Crear_tabla(nombre):
    connection = conectar()

    if connection:
        try:
            print("Connected to MySQL database")

            # Crear un objeto cursor para ejecutar consultas SQL
            cursor = connection.cursor()

            insert_query = f"""CREATE TABLE {nombre} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            fecha DATE
            )"""
            cursor.execute(insert_query)

            # Commit para aplicar los cambios
            connection.commit()
            print(f"New table '{nombre}' inserted successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
            if 'cursor' in locals() and cursor is not None:
                cursor.close()

            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print("Connection closed")
    else:
        print("Error connecting to the database.")


def imprimir_registros(Nombre):
    connection = conectar()

    if connection:
        try:
            print("Connected to MySQL database")

            # Crear un objeto cursor para ejecutar consultas SQL
            cursor = connection.cursor()

            # Ejemplo: Realizar una consulta SELECT
            select_query = f"SELECT * FROM {Nombre}"
            cursor.execute(select_query)

            # Obtener todos los resultados de la consulta
            rows = cursor.fetchall()

            # Mostrar los resultados
            for row in rows:
                print(row)

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
            if 'cursor' in locals() and cursor is not None:
                cursor.close()

            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print("Connection closed")
    else:
        print("Error connecting to the database.")

def insertar_registro(tabla,nombre,fecha):
    connection = conectar()

    if connection:
        try:
            print("Connected to MySQL database")

            # Crear un objeto cursor para ejecutar consultas SQL
            cursor = connection.cursor()

            # Ejemplo: Insertar un nuevo registro en la tabla 'ejemplo'
            insert_query = f"INSERT INTO {tabla} (nombre, fecha) VALUES ('{nombre}','{fecha}')"
            cursor.execute(insert_query)

            # Commit para aplicar los cambios
            connection.commit()
            print(f"New record with nombre '{nombre}' and date {fecha} inserted successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
            if 'cursor' in locals() and cursor is not None:
                cursor.close()

            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print("Connection closed")
    else:
        print("Error connecting to the database.")

def eliminar_registro(id_registro):
    connection = conectar()

    if connection:
        try:
            print("Connected to MySQL database")

            # Crear un objeto cursor para ejecutar consultas SQL
            cursor = connection.cursor()

            # Ejemplo: Eliminar un registro de la tabla 'ejemplo'
            delete_query = f"DELETE FROM ejemplo WHERE id = {id_registro}"
            cursor.execute(delete_query)

            # Commit para aplicar los cambios
            connection.commit()
            print(f"Record with id {id_registro} deleted successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Cerrar el cursor y la conexión en el bloque 'finally' para asegurar una limpieza adecuada
            if 'cursor' in locals() and cursor is not None:
                cursor.close()

            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print("Connection closed")
    else:
        print("Error connecting to the database.")

# Uso de las funciones con los nuevos valores
insertar_registro("Reporte","test2","2024-03-07")
imprimir_registros("Reporte")

