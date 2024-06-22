from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ваш токен Telegram бота
TOKEN = '6795426623:AAGe0sDjCotDWSwQbxN-c_Ig4e08c1QJF0Q'
# URL вашего веб-приложения на Render
WEB_APP_URL = 'https://cryptobot-0cs7.onrender.com/'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Open Crypto App", web_app=WebAppInfo(url=WEB_APP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Open the Crypto App:', reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
