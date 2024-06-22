from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Вставьте ваш токен API здесь
TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я крипто-бот. Как я могу помочь?')

def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
