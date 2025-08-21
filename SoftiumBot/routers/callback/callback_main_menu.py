import asyncio

from aiogram.types import CallbackQuery
from aiogram import Router, F
from keyboards.reply_keyboards import yes_or_no_kb
from aiogram.fsm.context import FSMContext

from states.program_state import Program
from states.trial_session_state import Trial

from aiogram.types import ReplyKeyboardRemove

router = Router(name=__name__)


@router.callback_query(F.data == "tg_chanel")
async def callback_tg_chanel(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer("🚀 Запускаем детский интеллект на полную мощность!\n"
                                  "Подпишитесь на канал нашей школы программирования Софтиум и узнайте:\n"
                                  "   🔹 Как технологии делают детей успешнее\n"
                                  "   🔹 Наши акции и события\n"
                                  "   🔹 Победы учеников и вдохновляющие проекты\n"
                                  "\n"
                                  "📲 Жмите сюда https://t.me/softiumpenza — будущее начинается сегодня!",
                                  reply_markup=ReplyKeyboardRemove())


@router.callback_query(F.data == "program")
async def callback_tg_chanel(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.set_state(Program.use_computer)
    await callback.message.answer("Ответе на несколько вопросов, чтобы мы могли подобрать программу.")
    await asyncio.sleep(1)
    await callback.message.answer("Пользуется ли ваш ребенок ПК?", reply_markup=yes_or_no_kb())


@router.callback_query(F.data == "trial_session")
async def callback_trial_session(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.set_state(Trial.name)
    await callback.message.answer("Как Вас зовут?", reply_markup=ReplyKeyboardRemove())
