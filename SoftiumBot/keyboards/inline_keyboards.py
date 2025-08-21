from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu_ikb() -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()
    markup.add(InlineKeyboardButton(text="Презентация о школе",
                                    url="https://disk.yandex.ru/d/duPIzgz3jNKVtg"),
               InlineKeyboardButton(text="Наш ТГ-канал", callback_data="tg_chanel"),
               InlineKeyboardButton(text="Подобрать программу для ребёнка", callback_data="program"),
               InlineKeyboardButton(text="Запись на пробное занятие", callback_data="trial_session"),
               )
    markup.adjust(2)
    return markup.as_markup()
