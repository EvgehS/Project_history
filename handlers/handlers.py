from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import (
    kb,
    create_answer_keyboard,
    create_explain_keyboard,
)
import random
from Config.config import questions


router = Router()


@router.message(Command("start"))
async def start_command_handler(message):
    await message.answer(
        "👋 Привет!\n"
        "Я — бот с викториной по истории.\n"
        "Проверь свои знания, узнай новые факты и получи удовольствие от игры!"
        "\n\n"
        "Готов? Жми кнопку ниже и начнём!", reply_markup=kb
    )


@router.message(Command("help"))
async def help_command_handler(message):
    await message.answer(
        "ℹ️ Это историческая викторина.\n"
        "Тебе будут предложены вопросы с четырьмя вариантами ответов.\n"
        "Выбирай, и я сразу скажу, правильно ли ты ответил, "
        "и расскажу подробнее о теме вопроса.\n\n"
        "Удачи!🙂"
    )


@router.message(F.text == "❓ Помощь")
async def help_button_handler(message: Message):
    await help_command_handler(message)


@router.message(F.text == "▶️ Новый вопрос")
async def new_question_button_handler(message: Message):
    question = random.choice(questions)
    await message.answer(question['question'],
                         reply_markup=create_answer_keyboard(
                             question['answers']))


@router.callback_query(
    F.data[:-2] == "answer"
)
async def answer_callback_handler(callback_query: CallbackQuery):
    answer_id = int(callback_query.data[-1])
    question = next(
        (
            q for q in questions
            if callback_query.message.text == q["question"]
        ),
        None
    )

    if question:
        correct_answer = question['answer']
        if question["answers"][answer_id] == correct_answer:
            result_text = "✅ Правильно! 🎉"
        else:
            result_text = f"❌ Неправильно! Правильный ответ: {correct_answer}"

        await callback_query.message.answer(
            result_text,
            reply_markup=create_explain_keyboard(
                question['explanation_offer']
            )
        )
        await callback_query.answer()
    else:
        await callback_query.answer("Ошибка: вопрос не найден.")


@router.callback_query(F.data == "explain")
async def explain_callback_handler(callback_query: CallbackQuery):
    question = next(
        (
            q for q in questions if q['explanation_offer'] in
            callback_query.message.reply_markup.inline_keyboard[0][0].text
        ),
        None
    )

    if question:
        await callback_query.message.answer(question['explanation'])
        await callback_query.answer()
    else:
        await callback_query.answer("Ошибка: объяснение не найдено.")


@router.message()
async def unknown_command(message: Message):
    await message.answer('Неизвестная команда')
