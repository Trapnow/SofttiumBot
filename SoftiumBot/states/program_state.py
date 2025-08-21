from aiogram.filters.state import State, StatesGroup

class Program(StatesGroup):
    use_computer = State()
    experience = State()
    type_of_thinking = State()
    play_games = State()

