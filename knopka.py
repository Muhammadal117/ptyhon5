from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import sqlite3

def asosiymenyubutton(chatid):
    database = sqlite3.connect('shaharlar.sqlite')
    cursor = database.cursor()
    cursor.execute('''SELECT name FROM cities WHERE chatid = ?''', (chatid, ))
    shahar = cursor.fetchall()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for name in shahar:
        markup.add(
            KeyboardButton(text=name[0])
        )
    return markup

def shaharqoshish(sity):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Qoshish', callback_data=f'shahar_{sity}')
    )

    return markup