from aiogram.types import Message
from aiogram import Router
from functions.functions_programs import determine_program
from keyboards.reply_keyboards import type_talking_kb, yes_or_no_kb

from aiogram.types import ReplyKeyboardRemove

from states.program_state import Program
from aiogram.fsm.context import FSMContext

router = Router(name=__name__)

programs = {
    "Базовая компьютерная грамотность":
        "💻 Поздравляем! Вашему ребёнку идеально подойдёт программа «Базовая компьютерная грамотность».\n"
        "На занятиях он:\n"
        "🔹 Освоит работу с компьютером и безопасный интернет\n"
        "🔹 Научится пользоваться офисными программами\n"
        "🔹 Получит уверенность в цифровом мире\n\n"
        "📄 Узнайте подробности о программе здесь https://drive.google.com/file/d/1ZOCoxZmv_k7R3cZ8DYyFroT0cwzg9GM1/view?usp=drive_link\n"
        "📅 Запишитесь на пробное занятие — это первый шаг к будущим успехам в школе и жизни!",

    "Компьютерная графика и web-дизайн":
        "🎨 Отличный выбор!\n"
        "Вашему ребёнку подойдёт программа «Компьютерная графика и web-дизайн».\n"
        "На занятиях он:\n"
        "🔹 Создаст первые иллюстрации и дизайн-проекты\n"
        "🔹 Освоит графические редакторы\n"
        "🔹 Разовьёт креативное мышление и чувство стиля\n\n"
        "📄 Смотреть презентацию программы https://drive.google.com/file/d/1B2FkOxfnSdSUT202NgcPQ9sPrTDSgl-m/view?usp=drive_link\n"
        "📅 Приглашаем на пробное занятие — пусть его идеи оживут на экране!",

    "Разработка приложений и программирование на Python":
        "🐍 Вау!\n"
        "Ваш ребёнок готов к программе «Разработка приложений и программирование на Python».\n"
        "На занятиях он:\n"
        "🔹 Создаст первые приложения и программы\n"
        "🔹 Научится логически мыслить и решать задачи\n"
        "🔹 Освоит язык программирования, который используют в Google и NASA\n\n"
        "📄 Подробнее о программе — в презентации https://drive.google.com/file/d/1wMXizRdf0ild_FUaLHkJLjSqX5CywZcC/view?usp=drive_link\n"
        "📅 Запишитесь на пробное занятие — пусть он сделает свой первый шаг в IT-профессию!",

    "Создание игр":
        "🎮 Круто!\n"
        "Вашему ребёнку идеально подойдёт программа «Создание игр».\n"
        "На занятиях он:\n"
        "🔹 Разработает собственную компьютерную игру\n"
        "🔹 Научится работать с графикой, анимацией и логикой игр\n"
        "🔹 Получит навыки, которые пригодятся в любой IT-сфере\n\n"
        "📄 Ознакомьтесь с программой в презентации https://drive.google.com/file/d/1kjd-6FOiickhnrsh5x9fTWasxe9Qgm-W/view?usp=drive_link\n"
        "📅 Приглашаем на пробное занятие — пусть он создаст игру, в которую будут играть друзья!"
}


@router.message(Program.use_computer)
async def use_computer_handler(msg: Message, state: FSMContext):
    answer = msg.text.lower()
    if answer not in ['да', 'нет']:
        await msg.answer("Выберите Да или Нет")
    else:
        await state.update_data(use_computer=answer)
        await state.set_state(Program.experience)
        await msg.answer("Есть ли опыт обучения в школе программирования?")


@router.message(Program.experience)
async def experience_handler(msg: Message, state: FSMContext):
    answer = msg.text.lower()
    if answer not in ['да', 'нет']:
        await msg.answer("Выберите Да или Нет")
    else:
        await state.update_data(experience=answer)
        await state.set_state(Program.type_of_thinking)
        await msg.answer("Какой тип мышления у вашего ребёнка?", reply_markup=type_talking_kb())


@router.message(Program.type_of_thinking)
async def type_of_thinking_handler(msg: Message, state: FSMContext):
    answer = msg.text.lower()
    if answer not in ['математический', 'творческий', 'гуманитарный']:
        await msg.answer("Выберите тип мышления")
    else:
        await state.update_data(type_of_thinking=answer)
        await state.set_state(Program.play_games)
        await msg.answer("Любит ли он играть в игры на телефоне или на ПК?", reply_markup=yes_or_no_kb())


@router.message(Program.play_games)
async def use_computer_handler(msg: Message, state: FSMContext):
    answer = msg.text.lower()
    if answer not in ['да', 'нет']:
        await msg.answer("Выберите Да или Нет")
    else:
        await state.update_data(play_games=answer)
        data = await state.get_data()
        await state.clear()
        program = determine_program(data["experience"], data["type_of_thinking"], data["play_games"])
        await msg.answer(programs[program], reply_markup=ReplyKeyboardRemove())
