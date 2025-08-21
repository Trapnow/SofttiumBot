__all__ = ('router',)

from aiogram import Router

from .commands import router as commands_router
from .training_program_handler import router as training_router
from .trial_session_handler import router as trial_router

router = Router()

router.include_routers(commands_router, training_router, trial_router)
