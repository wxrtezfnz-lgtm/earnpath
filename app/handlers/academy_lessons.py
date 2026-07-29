from aiogram import Router
from aiogram.types import CallbackQuery

from content.academy import ACADEMY


router = Router()


@router.callback_query(
    lambda callback: callback.data.startswith("academy_")
)
async def academy_lessons_handler(
    callback: CallbackQuery
):
    """
    Отображение уроков курса
    """

    course = callback.data.replace(
        "academy_",
        ""
    )

    if course not in ACADEMY:
        await callback.answer(
            "Курс скоро появится 🚧"
        )
        return


    data = ACADEMY[course]

    buttons = []

    for index, lesson in enumerate(
        data["lessons"],
        start=1
    ):
        buttons.append(
            [
                {
                    "text": f"📖 {index}. {lesson['title']}",
                    "callback_data": f"lesson_{course}_{index-1}"
                }
            ]
        )


    from aiogram.types import (
        InlineKeyboardMarkup,
        InlineKeyboardButton
    )


    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=item["text"],
                    callback_data=item["callback_data"]
                )
            ]
            for row in buttons
            for item in row
        ]
    )


    await callback.message.edit_text(
        f"""
📚 <b>{data['title']}</b>

Выбери урок:
        """,
        reply_markup=keyboard
    )


    await callback.answer()



@router.callback_query(
    lambda callback: callback.data.startswith("lesson_")
)
async def lesson_handler(
    callback: CallbackQuery
):
    """
    Отображение материала урока
    """

    _, course, lesson_id = callback.data.split("_")

    lesson = ACADEMY[course]["lessons"][
        int(lesson_id)
    ]


    await callback.message.edit_text(
        f"""
📖 <b>{lesson['title']}</b>


{lesson['text']}


🎯 После изучения переходи к следующему уроку.
        """
    )


    await callback.answer()