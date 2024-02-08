import sqlite3

from database.config_for_database import data_base_name


async def create_database():
    connection = sqlite3.connect(f"{data_base_name}.db")
    cursor = connection.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS Videos(
            name TEXT,
            file_id TEXT)''')
    connection.commit()
    connection.close()
    