from aiogram import Router, F
from aiogram.types import Message

from app.courses.design import DESIGN_COURSE
from app.keyboards.courses import design_lessons_keyboard
from app.services.progress import complete_lesson


router = Router()


user_lessons = {}


@router.message(F.text == "📚 Уроки дизайна")
async def design_lessons(message: Message):

    await message.answer(
        "🎨 Курс: Дизайн с нуля\n\n"
        "Выбери урок:",
        reply_markup=design_lessons_keyboard()
    )


@router.message(F.text.startswith("🎨 Урок"))
async def open_lesson(message: Message):

    lesson_number = int(
        message.text.replace(
            "🎨 Урок ",
            ""
        )
    )


    lesson = DESIGN_COURSE.get(
        lesson_number
    )


    if lesson:

        user_lessons[
            message.from_user.id
        ] = lesson_number


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


    lesson_id = user_lessons.get(
        message.from_user.id
    )


    if not lesson_id:

        await message.answer(
            "Сначала открой урок 📚"
        )

        return



    success, user = complete_lesson(
        message.from_user.id,
        message.from_user.username or "user",
        lesson_id
    )


    if success:

        await message.answer(
            "🎉 Урок завершён!\n\n"
            "+10 XP ⚡\n\n"
            f"Всего XP: {user['xp']}\n"
            f"Уровень: {user['level']}"
        )

    else:

        await message.answer(
            "Этот урок уже пройден ✅"
        )