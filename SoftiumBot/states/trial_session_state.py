from aiogram.filters.state import State, StatesGroup

class Trial(StatesGroup):
    name = State()
    child_name = State()
    school = State()
    grade = State()
    email = State()
    phone = State()
    found_out_about_us = State()