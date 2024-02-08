import sqlite3

from database.config_for_database import data_base_name


async def get_result_from_database(name: str):
    connection = sqlite3.connect(f"{data_base_name}.db")
    cursor = connection.cursor()
    cursor.execute('SELECT file_id, name FROM Videos WHERE name = ?', (name,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result
