from enum import Enum


class Button(str, Enum):
    CANCEL = "Отмена"
    ADD_VIDEO = "Добавить видео"
    FIND_VIDEO = "Найти видео"


general_buttons = [Button.FIND_VIDEO.value, Button.CANCEL.value]
admin_buttons = [Button.ADD_VIDEO.value, ] + general_buttons
subscriber_buttons = [] + general_buttons
