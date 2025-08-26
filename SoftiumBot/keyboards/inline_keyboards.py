from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu_ikb() -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()
    markup.add(InlineKeyboardButton(text="Презентация о школе",
                                    url="https://drive.google.com/file/d/1Glsu-J9AQkYE9MokNjn1t616K64y6zoV/view?usp=drive_link"),
               InlineKeyboardButton(text="Наш ТГ-канал", callback_data="tg_chanel"),
               InlineKeyboardButton(text="Подобрать программу для ребёнка", callback_data="program"),
               InlineKeyboardButton(text="Запись на пробное занятие", callback_data="trial_session"),
               )
    markup.adjust(2)
    return markup.as_markup()
