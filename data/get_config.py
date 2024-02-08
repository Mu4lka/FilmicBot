import json
import os
import sys
import keyboard


def get_config(path):
    if not os.path.exists(path):
        with open(path, 'w') as config_path:
            config = {
                "bot_token": "BOT_TOKEN",
                "admin_ids": "0000000000, 1111111111",
                "group_chat_id": "@group_chat_id (or 0000000001)"
            }
            json.dump(config, config_path)
            print(f"Не нашел файл {path}, в следствии чего он был создан, "
                  f"теперь поменяйте в нем данные и перезапустите приложение")
        keyboard.read_key()
        sys.exit()

    with open(path) as path:
        return json.load(path)
