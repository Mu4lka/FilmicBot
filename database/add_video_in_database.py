import sqlite3

from database.config_for_database import data_base_name


async def add_video_in_database(name: str, file_id: str):
    connection = sqlite3.connect(f"{data_base_name}.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Videos (name, file_id) VALUES (?, ?)',
                   (f'{name}', f'{file_id}')
                   )
    connection.commit()
    connection.close()
