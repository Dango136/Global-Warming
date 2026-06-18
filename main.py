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
# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Я расскажу тебе о Глобальном Потеплении, его последствиях и способах его замедлить!')
    with open(f'images/image1.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, f'Вот список комманд этого бота: /start , /help , /gw , /reasons , /actions ')

bot.infinity_polling()