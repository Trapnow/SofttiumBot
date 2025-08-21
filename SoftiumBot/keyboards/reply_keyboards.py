from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def yes_or_no_kb() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardBuilder()
    markup.add(KeyboardButton(text="Да"),
               KeyboardButton(text="Нет"),
               )
    markup.adjust(2)
    return markup.as_markup(resize_keyboard=True)

def type_talking_kb() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardBuilder()
    markup.add(KeyboardButton(text="Математический"),
               KeyboardButton(text="Творческий"),
               KeyboardButton(text="Гуманитарный"),
               )
    markup.adjust(3)
    return markup.as_markup(resize_keyboard=True)


def found_out_about_us__kb() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardBuilder()
    markup.add(KeyboardButton(text="С родительского собрания"),
               KeyboardButton(text="Из группы в TG или VK"),
               KeyboardButton(text="Из школьного чата"),
               KeyboardButton(text="Рассказал ребёнок"),
               KeyboardButton(text="Другое"),
               )
    markup.adjust(1)
    return markup.as_markup(resize_keyboard=True)
