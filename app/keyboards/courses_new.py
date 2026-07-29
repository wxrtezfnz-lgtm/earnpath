from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def design_lessons_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎨 Урок 1")],
            [KeyboardButton(text="🎨 Урок 2")],
            [KeyboardButton(text="🎨 Урок 3")],
            [KeyboardButton(text="⬅️ Назад")]
        ],
        resize_keyboard=True
    )


def finish_lesson_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Завершить урок")],
            [KeyboardButton(text="⬅️ Назад")]
        ],
        resize_keyboard=True
    )