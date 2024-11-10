from aiogram.fsm.state import State, StatesGroup


class FSMProject(StatesGroup):
    choice_project = State()
    set_project = State()
    set_checkout = State()
