import telebot

# Вставьте сюда ваш токен от BotFather
TOKEN = '7247198623:AAETbxbA8OhoUAvVPziaHUAJJpa5TWMRm9Y'

bot = telebot.TeleBot(TOKEN)

# Список вопросов и ответов для каждого уровня сложности
questions = {
    'easy': [
        {'question': 'Какой город является столицей Франции?', 'answer': 'Париж'},
        {'question': 'Какое самое большое озеро в мире?', 'answer': 'Каспийское море'},
        {'question': 'В каком городе находится Эйфелева башня?', 'answer': 'Париже'}
    ],
    'normal': [
        {'question': 'Где находится гора Эверест?', 'answer': 'Непал'},
        {'question': 'Столица Японии?', 'answer': 'Токио'},
        {'question': 'Самое глубокое озеро в мире?', 'answer': 'Байкал'}
    ],
    'hard': [
        {'question': 'Самая длинная река в мире?', 'answer': 'Нил'},
        {'question': 'Самый большой океан в мире?', 'answer': 'Тихий океан'},
        {'question': 'Страна с самой длинной береговой линией?', 'answer': 'Канада'}
    ]
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 f'Привет! Хочешь сыграть в викторину? Выбери уровень сложности:\n/level_easy\n/level_normal\n/level_hard')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == '/level_easy':
        start_quiz('easy', message.chat.id)
    elif message.text == '/level_normal':
        start_quiz('normal', message.chat.id)
    elif message.text == '/level_hard':
        start_quiz('hard', message.chat.id)


def start_quiz(level, chat_id):
    score = 0
    current_question_index = 0
    total_questions = len(questions[level])

    def ask_next_question():
        nonlocal current_question_index
        if current_question_index < total_questions:
            question = questions[level][current_question_index]['question']
            bot.send_message(chat_id, question)
            bot.register_next_step_handler_by_chat_id(chat_id, check_answer)
        else:
            finish_quiz(score, total_questions, chat_id)

    def check_answer(user_message):
        nonlocal current_question_index, score
        answer = questions[level][current_question_index]['answer'].lower().strip()
        user_answer = user_message.text.lower().strip()
        if user_answer == answer:
            score += 1
            bot.send_message(chat_id, 'Правильно!')
        else:
            bot.send_message(chat_id, f'Не правильно. Правильный ответ: {answer}')

        current_question_index += 1
        ask_next_question()

    def finish_quiz(score, total_questions, chat_id):
        bot.send_message(chat_id, f"Твой результат: {score}/{total_questions}")

    # Начинаем викторину
    ask_next_question()


if __name__ == '__main__':
    bot.polling()
