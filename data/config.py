from data.get_config import get_config

config_file_name = "config.json"
config = get_config(config_file_name)

BOT_TOKEN = config["bot_token"]
ADMIN_IDS = config["admin_ids"]
GROUP_CHAT_ID = config["group_chat_id"]
