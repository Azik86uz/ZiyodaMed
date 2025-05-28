import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("API_KEY"))

WEB_APP_URL = "https://Azik86uz.github.io/webapp/?v=1"
GROUP_ID = -1002555740055  # Правильный chat_id супергруппы

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Записаться на массаж", web_app=types.WebAppInfo(url=WEB_APP_URL))
    markup.add(btn)

    bot.send_message(
        message.chat.id,
        "Добро пожаловать! Нажмите кнопку ниже, чтобы записаться на массаж:",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data
    print("📥 Получена заявка от сайта:", data)
    bot.send_message(GROUP_ID, f"📬 Новая заявка:\n{data}")
    bot.send_message(message.chat.id, "✅ Заявка отправлена! Мы свяжемся с вами.")

print("Бот запущен! Для остановки нажмите Ctrl+C")
bot.polling(none_stop=True)