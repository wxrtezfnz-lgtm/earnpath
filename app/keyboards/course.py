from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def design_course_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎨 Урок 1: Композиция",
                    callback_data="lesson_composition"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌈 Урок 2: Цвет",
                    callback_data="lesson_color"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🖼 Урок 3: Портфолио",
                    callback_data="lesson_portfolio"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔙 Назад",
                    callback_data="design"
                )
            ]
        ]
    )


def complete_lesson_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Завершить урок",
                    callback_data="complete_lesson"
                )
            ]
        ]
    )