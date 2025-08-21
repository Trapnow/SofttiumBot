__all__ = ('router',)

from aiogram import Router

from .callback_main_menu import router as callback_router

router = Router()

router.include_router(callback_router)