from config import token
import telebot
import time
import os
import random
import requests
from telebot.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
# Инициализация бота с использованием его токена
bot = telebot.TeleBot(token)
images = os.listdir('images')
themes = ['Что такое Глобальное Потепление?', 'Чем вызвано Глобальное Потепление?', 'Как можно замедлить Глобальное Потепление?']
answers = ['Глобальное потепление — это длительное повышение средней температуры климатической системы Земли. Это часть более широкого процесса климатических изменений, который включает не только рост температуры, но и связанные с ним последствия: изменение осадков, таяние ледников, экстремальные погодные явления, смещение климатических зон и другие трансформации.',
'''Причинами Глобального Потепления называют: 
1. Выбросы парниковых газов
2. Изменение землепользования
3. Промышленные аэрозоли
4. Солнечная активность
5. Вулканическая активность
6. Океанские течения
7. Смещение тектонических плит''',
'Мы можем замедлить действие Глобального Потепления на нашу Землю! Для этого нужно перестать пользоваться невозобновляемым топливом, выделяющим газы, и перейти на экологически чистые возобновляемые источники энергии! Также развитие науки и технологий поможет нам создавать улучшенные фильтры, которые будут устанавливаться на различных предприятиях, задерживая вредные выбросы. Нам также стоит вырубать меньшее количество леса и выращивать как можно больше растений!']
images = [["image2.jpg", "image3.jpg", "image4.png", "image5.png", "image6.jpg"], 
          ["image7.png", "image8.jpg", "image9.jpg", "image10.jpg", "image11.jpg"], 
          ["image12.jpg", "image13.png", "image14.png", "image15.png", "image16.png"]]
# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет!👋')
    time.sleep(2)
    bot.reply_to(message, f'Я бот ГБ-5000!🤖')
    time.sleep(2)
    bot.reply_to(message, f'Я расскажу тебе о Глобальном Потеплении, его причинах и способах его замедления!☀')
    with open(f'images/image1.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    time.sleep(3)
    bot.reply_to(message, f'Используй команду /gw чтобы получить список тем на выбор.❓')
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, f'''Вот список комманд этого бота:
    /start - Бот стартует работу и приветствует вас.
    /help - Выводит список комманд для бота.
    /gw - Бот предоставит выбор из нескольких кнопок, при нажатии на каждую пользователь получит ответ на конкретный вопрос по теме.''')
@bot.message_handler(commands=['gw'])
def send_gw(message):
    keyboard=InlineKeyboardMarkup()
    for i, q in enumerate(themes):
        keyboard.add(InlineKeyboardButton(q, callback_data=f'theme {i}'))
    bot.send_message(message.chat.id, f'Выберите тему: ',reply_markup=keyboard)
@bot.callback_query_handler(lambda call: 'theme' in call.data)
def call_data(callback):
    index = int(callback.data.split()[1])
    filename = random.choice(images[index])
    with open(f'images/{filename}', 'rb') as f:
        bot.send_photo(callback.message.chat.id, f, answers[index])
bot.infinity_polling()