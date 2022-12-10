from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from random import randint

TOKEN = "TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboardbutton = KeyboardButton("клавіатура")  # створення клавіатурної кнопки
inlinebutton = InlineKeyboardButton(text="кнопка", callback_data="buttondata")  # створення inline кнопки

@dp.message_handler(commands=["start"])  # сворення функції що реагує на початакову команду /start
async def random(msg: types.Message):
    await msg.answer(reply_markup=builder, text="<b>Привіт!</b>\n<u><b>Я бот з крутими командами!</b></u>", parse_mode="html")


@dp.message_handler(commands=["inline"])  # сворення функції що реагує на команду /inline
async def random(msg: types.Message):
    builder = InlineKeyboardMarkup()  # створення inline клавіатури
    builder.add(inlinebutton)  # додавання кнопки до клавіатури
    await msg.answer(reply_markup=builder, text="це повідомлення з inline кнопкою")


@dp.callback_query_handler(text="button")  # пишемо функцію що реагує на натискання inline кнопки
async def send_random(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))  # відправляє раптову цифру


@dp.message_handler(commands=["openkeyboard"])  # функция реагує на команду openkeyboard
async def withkeyboard(msg: types.Message):
    builder = ReplyKeyboardMarkup()  # створюємо клавіатуру
    builder.add(keyboardbutton)  # додаємо кнопку в клавіатуру
    await msg.answer(text="це повідомлення з клавіатурною кнопкою", reply_markup=builder)


@dp.message_handler()
async def text(msg: types.Message):
    if (msg.text == "клавіатура"):
        await msg.answer(text="ви натиснули на клавіатуру")


if __name__ == "__main__":
    executor.start_polling(dp)


