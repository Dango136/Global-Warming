from config import token
import telebot
import os
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

# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот "ГБ-5000"! Я расскажу тебе о Глобальном Потеплении, его последствиях и способах его замедлить!')
    with open(f'images/image1.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, f'''Вот список комманд этого бота:
    /start - Бот стартует работу и приветствует вас.
    /help - Выводит список комманд для бота.
    /gw - Бот расскажет, что такое Глобальное Потепление.
    /reasons - Бот объяснит причины возникновения и ускорения процесса Глобального Потепления.
    /actions - Бот подскажет, что мы можем сделать для замедления процесса Глобального Потепления.''')
@bot.message_handler(commands=['gw'])
def send_gw(message):
    keyboard=InlineKeyboardMarkup()
    for i, q in enumerate(themes):
        keyboard.add(InlineKeyboardButton(q, callback_data=f'theme {i}'))
    bot.send_message(message.chat.id, f'Выберите тему: ',reply_markup=keyboard)
@bot.callback_query_handler(lambda call: 'theme' in call.data)
def call_data(callback):
    index = int(callback.data.split([1]))
    bot.send_message(callback.message.chat.id, answers[index])
bot.infinity_polling()