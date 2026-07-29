from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query()
async def debug_menu(callback: CallbackQuery):
    print("CALLBACK DATA =", callback.data)

    await callback.answer()

    await callback.message.answer(
        f"Нажата кнопка: <code>{callback.data}</code>"
    )