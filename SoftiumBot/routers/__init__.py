__all__ = ('router',)

from aiogram import Router

from .callback import router as callback_main_menu_router
from .handlers import router as handlers_router

router = Router()

router.include_routers(callback_main_menu_router,
                       handlers_router)
