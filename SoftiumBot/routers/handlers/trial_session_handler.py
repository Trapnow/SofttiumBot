from aiogram.types import Message
from aiogram import Router

from functions.functions_programs import validate_email, validate_phone, validate_class
from keyboards.reply_keyboards import found_out_about_us__kb
from states.trial_session_state import Trial
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

router = Router(name=__name__)


@router.message(Trial.name)
async def name_handler(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Trial.child_name)
    await msg.answer("Как зовут ребенка?")


@router.message(Trial.child_name)
async def child_name_handler(msg: Message, state: FSMContext):
    await state.update_data(child_name=msg.text)
    await state.set_state(Trial.school)
    await msg.answer("Из какой вы школы?")


@router.message(Trial.school)
async def school_handler(msg: Message, state: FSMContext):
    await state.update_data(school=msg.text)
    await state.set_state(Trial.grade)
    await msg.answer("В каком классе учится ваш ребенок? (цифра и буква)")


@router.message(Trial.grade)
async def grade_handler(msg: Message, state: FSMContext):
    if not validate_class(msg.text):
        await msg.answer("Введите правильный класс")
    else:
        await state.update_data(grade=msg.text)
        await state.set_state(Trial.email)
        await msg.answer("Укажите адрес электронной почты")


@router.message(Trial.email)
async def email_handler(msg: Message, state: FSMContext):
    if not validate_email(msg.text):
        await msg.answer("Введите корректный email")
    else:
        await state.update_data(email=msg.text)
        await state.set_state(Trial.found_out_about_us)
        await msg.answer("Откуда Вы узнали про нас?", reply_markup=found_out_about_us__kb())


@router.message(Trial.found_out_about_us)
async def email_handler(msg: Message, state: FSMContext):
    await state.update_data(found_out_about_us=msg.text)
    await state.set_state(Trial.phone)
    await msg.answer("Укажите номер телефона, на который Вам может перезвонить менеджер.")


@router.message(Trial.phone)
async def phone_handler(msg: Message, state: FSMContext):
    if not validate_phone(msg.text):
        await msg.answer("Введите корректный номер телефона")
    else:
        await state.update_data(phone=msg.text)

        data = await state.get_data()

        await state.clear()

        await msg.bot.send_message(chat_id=-4860435909,
                                   text=f"Имя: {data["name"]}\n"
                                        f"Имя ребёнка: {data["child_name"]}\n"
                                        f"Школа: {data["school"]}\n"
                                        f"Класс: {data["grade"]}\n"
                                        f"Почта: {data["email"]}\n"
                                        f"Откуда узнали о нас: {data["found_out_about_us"]}\n"
                                        f"Телефон: {data["phone"]}\n")

        await msg.answer("✅ Спасибо за заявку!"
                         "Мы уже получили ваши данные."
                         "📞 Наш менеджер свяжется с вами в ближайшее время с номера 8 963 110 98 86."
                         "⏳ Пожалуйста, оставайтесь на связи — скоро мы договоримся о дате пробного занятия!",
                         reply_markup=ReplyKeyboardRemove()
                         )
