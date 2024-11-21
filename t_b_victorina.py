import random
from telebot import TeleBot

# Токен вашего бота
TOKEN = '7247198623:AAETbxbA8OhoUAvVPziaHUAJJpa5TWMRm9Y'

# Создаем экземпляр бота
bot = TeleBot(TOKEN)

# Вопросы и ответы для разных уровней сложности
easy_questions = [{'question1': 'Какой город является столицей Франции?','answer1': 'Париж'}, {'question2': 'Самая длинная река в мире?','answer2': 'Амазонка',}]

medium_questions = [{'question3': 'Самая высокая гора на земле?','answer3': 'Эверест'}, {'question4': 'Какой океан самый большой в мире?','answer4': 'Тихий океан'}]

hard_questions = [ { 'question5': 'Какой самый маленький континент в мире?', 'answer5': 'Австралия' },{'question6': 'Какая пустыня самая большая?', 'answer6': 'Сахара'}]


# Функция для отправки сообщения о старте игры
@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(
        message.chat.id,
        'Добро пожаловать в географическую викторину!\n\nВыберите уровень сложности:\n/level_easy - Легкий\n/level_medium - Средний\n/level_hard - Сложный'
    )


# Функция для обработки команды /level_easy
@bot.message_handler(commands=['level_easy'])
def level_easy(message):
    ask_question(easy_questions, message.chat.id)


# Функция для обработки команды /level_medium
@bot.message_handler(commands=['level_medium'])
def level_medium(message):
    ask_question(medium_questions, message.chat.id)


# Функция для обработки команды /level_hard
@bot.message_handler(commands=['level_hard'])
def level_hard(message):
    ask_question(hard_questions, message.chat.id)


# Функция для генерации вопроса и проверки ответа
def ask_question(questions, chat_id):
    question = random.choice(questions)
    bot.send_message(chat_id, f'Вопрос: {question["question"]}')

    @bot.message_handler(func=lambda msg: True)
    def check_answer(message):
        if message.text.lower() == question['answer'].lower():
            bot.send_message(chat_id, 'Правильно!')
            ask_question(questions, chat_id)
        else:
            bot.send_message(chat_id, f'Неправильно. Правильный ответ: {question["answer"]}.')
            ask_question(questions, chat_id)


if __name__ == '__main__':
    # Запускаем бесконечный цикл для работы бота
    bot.polling(none_stop=True)