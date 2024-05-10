from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor
from knopka import shaharqoshish, asosiymenyubutton
from obhavo import registrshahar
from weather import obhavo

api = '6730337381:AAGWiINhcA1Tb2ONDZtTaCtsylsOq7ljVBo'
bot= Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid= message.chat.id
    await bot.send_message(chat_id=chatid, text='Xush kelibsiz. Shahar nomini kiriting', reply_markup=asosiymenyubutton(chatid))


@dp.message_handler()
async def getshahar(message: Message):
    chatid= message.chat.id
    shahar = message.text
    await bot.send_message(chat_id=chatid, text=obhavo(shahar), reply_markup=shaharqoshish(shahar))


@dp.callback_query_handler(lambda call: 'shahar' in call.data)
async def addshahar(callback: CallbackQuery):
    chatid = callback.message.chat.id
    shahar  = callback.data.split('_')[1]
    registrshahar(name=shahar, chatid=chatid)
    await bot.send_message(chat_id=chatid, text=shahar, reply_markup=asosiymenyubutton(chatid))


@dp.message_handler(commands='help')
async def help(message: Message):
    text = 'Botni ishlatish uchun /start ni bosing'
    await message.reply(text)



@dp.message_handler()
async def echo(message: Message):
    text = message.text
    info = obhavo(text)

    await message.reply(info)


executor.start_polling(dp, skip_updates=True, )