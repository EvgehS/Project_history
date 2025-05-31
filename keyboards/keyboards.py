from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

kb_builder = ReplyKeyboardBuilder()
kb_builder.row(KeyboardButton(text="▶️ Новый вопрос"),
               KeyboardButton(text="❓ Помощь"), width=1)
kb = kb_builder.as_markup()


def create_answer_keyboard(answers: list[str]) -> InlineKeyboardBuilder:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        *[InlineKeyboardButton(text=answer, callback_data=f"answer_{i}")
          for i, answer in enumerate(answers)],
        width=2
    )
    return kb_builder.as_markup()


def create_explain_keyboard(explanation_offer_text) -> InlineKeyboardBuilder:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(text="📚 " + explanation_offer_text,
                             callback_data="explain"),
    )
    return kb_builder.as_markup()

