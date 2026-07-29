from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from sqlalchemy.ext.asyncio import AsyncSession
from aiogram import Bot

from app.database.engine import async_session
from app.services.progress import complete_lesson_progress
from app.keyboards.courses import design_lessons_keyboard
from app.courses.design import DESIGN_COURSE


router = Router()


# временное хранение открытого урока
active_lessons = {}



@router.message(F.text == "📚 Уроки дизайна")
async def lessons(message: Message):

    await message.answer(
        "🎨 Академия дизайна\n\n"
        "Выбери урок:",
        reply_markup=design_lessons_keyboard()
    )



@router.message(F.text.startswith("🎨 Урок "))
async def open_lesson(message: Message):

    try:
        lesson_id = int(
            message.text.replace(
                "🎨 Урок ",
                ""
            )
        )

    except:

        return


    lesson = DESIGN_COURSE.get(
        lesson_id
    )


    if not lesson:

        await message.answer(
            "Урок не найден"
        )

        return


    active_lessons[
        message.from_user.id
    ] = lesson_id


    await message.answer(
        f"{lesson['title']}\n\n"
        f"{lesson['text']}"
    )


    await message.answer(
        "После изучения нажми:\n\n"
        "✅ Завершить урок"
    )



@router.message(F.text == "✅ Завершить урок")
async def finish_lesson(message: Message):


    lesson_id = active_lessons.get(
        message.from_user.id
    )


    if not lesson_id:

        await message.answer(
            "Сначала открой урок 📚"
        )

        return



    async with async_session() as session:

        user = await complete_lesson_progress(
            session=session,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )



    await message.answer(
        "🎉 Урок завершён!\n\n"
        "+10 прогресса ⚡\n\n"
        f"📊 Прогресс: {user.progress}\n"
        f"⭐ Уровень: {user.level}"
    )