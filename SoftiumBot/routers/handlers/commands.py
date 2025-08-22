from aiogram.types import Message
from aiogram import Router

from aiogram.filters import CommandStart, Command

from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboards import main_menu_ikb

router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Добро пожаловать в школу программирования Софтиум!", reply_markup=main_menu_ikb())


@router.message(Command("description"))
async def cmd_description(msg: Message):
    await msg.answer("Школа программирования СОФТИУМ — IT-навыки для учёбы и жизни 🚀\n"
                     "📘 О нашей школе и занятиях\n"
                     "🎓 Подбор программы обучения\n"
                     "🎮 Запись на пробное занятие")