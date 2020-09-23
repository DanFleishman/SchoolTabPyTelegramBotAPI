
from telebot import types

first_table_btn = "📅 Расписание уроков"
bells_table_btn = "🔔 Расписание звонков"

markup = types.InlineKeyboardMarkup(row_width=1)
today_inline_btn = types.InlineKeyboardButton("Сегодня", callback_data='today')
monday_inline_btn = types.InlineKeyboardButton("Понедельник", callback_data='0')
tuesday_inline_btn = types.InlineKeyboardButton("Вторник", callback_data='1')
wednesday_inline_btn = types.InlineKeyboardButton("Среда", callback_data='2')
thursday_inline_btn = types.InlineKeyboardButton("Четверг", callback_data='3')
friday_inline_btn = types.InlineKeyboardButton("Пятница", callback_data='4')

markup.add(today_inline_btn, monday_inline_btn, tuesday_inline_btn, wednesday_inline_btn, thursday_inline_btn,
           friday_inline_btn)
