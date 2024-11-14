import telebot

# Вставьте сюда ваш токен от BotFather
API_TOKEN = '7543902606:AAGpHNUuVvrj1hC0Wb4U6BBsnLLMBYv3bbE'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)
# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, 'Привет! И тебе всего хорошего!!!!')

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки событий
    bot.polling()