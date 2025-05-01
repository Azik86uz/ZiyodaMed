import nest_asyncio
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Разрешаем asyncio для Jupyter (если нужно)
nest_asyncio.apply()

async def start(update: Update, context: CallbackContext) -> None:
    # Создаем кнопку для WebApp
    keyboard = [
        [InlineKeyboardButton("Записаться на массаж", web_app={'url': 'https://github.com/Azik86uz/ZiyodaMed'})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        'Добро пожаловать! Нажмите кнопку ниже для записи:',
        reply_markup=reply_markup
    )

async def main():
    # Создаем Application и передаем токен бота
    application = Application.builder().token("7575499621:AAFnd1fpI1LmvL77EdvMpIUX8JSS37gem2w").build()
    
    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())