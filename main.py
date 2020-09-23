
import telebot
from config import *
from timetable import *
from buttons import *

bot = telebot.TeleBot(TOKEN)  # token from config.py


def day_check_func(message):
    print(message)
    replies_keyboard_btn = {
        "0": {
            "msg": "понедельник",
            "timetable": monday
        },
        "1": {
            "msg": "Вторник",
            "timetable": tuesday
        },
        "2": {
            "msg": "Среду",
            "timetable": wednesday
        },
        "3": {
            "msg": "Четверг",
            "timetable": thursday
        },
        "4": {
            "msg": "Пятницу",
            "timetable": friday
        },
    }
    if message.data:
        if message in replies_keyboard_btn:
            bot.send_message(message.chat.id, f"<b>Расписание на {replies_keyboard_btn[message.data]['msg']}:</b>\n"
                                     f" {replies_keyboard_btn[message.data]['timetable']}",
                                     parse_mode='html')
        else:
            pass
#     if today == 1:
#         bot.send_message(message.chat.id, f"<b>Cегодня вторник</b>\n<em>Расписание</em>: {tuesday}", parse_mode='html')
#     elif today == 2:
#         bot.send_message(message.chat.id, f"<b>Cегодня среда</b>\n<em>Расписание</em>: {wednesday}", parse_mode='html')
#     elif today == 3:
#         bot.send_message(message.chat.id, f"<b>Cегодня четверг</b>\n<em>Расписание</em>: {thursday}", parse_mode='html')
#     elif today == 4:
#         bot.send_message(message.chat.id, f"<b>Cегодня пятница</b>\n<em>Расписание</em>: {friday}", parse_mode='html')
#     elif today == 5:
#         bot.send_message(message.chat.id, "<b>Cегодня суббота!\nСегодня нет уроков!</b>", parse_mode='html')
#     elif today == 6:
#         bot.send_message(message.chat.id, "<b>Cегодня восресенье!\nСегодня нет уроков!</b>", parse_mode='html')
# ------------launch the start command and display the first buttons------------


@bot.message_handler(commands=['start'])
def send_welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    today_table = types.KeyboardButton(first_table_btn)
    bells_table = types.KeyboardButton(bells_table_btn)

    markup.add(today_table, bells_table)

    bot.send_message(message.chat.id, "Привет, {0.first_name}, Выбери в меню, что ты хочешь:".format(message.from_user),
                     reply_markup=markup)

# ------------launch the start command and display the first buttons------------


# -----------check the push buttons of the bottom menu-----------


@bot.message_handler(content_types=['text'])
def first_keyboard_check(message):
    if message.chat.type == 'private':
        if message.text == first_table_btn:

            bot.send_message(message.chat.id, "Выбери день:", reply_markup=markup)

        if message.text == bells_table_btn:
            bot.send_message(message.chat.id, f"<b>Расписание звонков:</b>\n{bells_timetable}", parse_mode="html")

# -----------check the push buttons of the bottom menu-----------


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    replies_inline_btn = {
        "0": {
            "msg": "понедельник",
            "timetable": monday
              },
        "1": {
            "msg": "Вторник",
            "timetable": tuesday
        },
        "2": {
            "msg": "Среду",
            "timetable": wednesday
        },
        "3": {
            "msg": "Четверг",
            "timetable": thursday
        },
        "4": {
            "msg": "Пятницу",
            "timetable": friday

        },

    }

    try:
        if call.data:
            if call.data in replies_inline_btn:
                bot.send_message(call.message.chat.id,
                                 f"<b>Расписание на {replies_inline_btn[call.data]['msg']}:</b>\n"
                                 f" {replies_inline_btn[call.data]['timetable']}",
                                 parse_mode='html')
            else:
                return day_check_func(call.message)

            # show alert

    except Exception as e:
        print(repr(e))

    # Start Bot


if __name__ == '__main__':
    bot.polling(none_stop=True)
