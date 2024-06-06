import telebot
from telebot import types

import secret
import gigachat


bot = telebot.TeleBot(secret.token)
gigaChat = gigachat.GigaChat(secret=secret)
inputEnabled = 0

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Приветствую. Я кино-эксперт, который порекомендует вам фильм для просмотра')

@bot.message_handler(commands=["getmovie"])
def getMovie(m, res=False):
    global inputEnabled 
    inputEnabled = 1
    bot.send_message(m.chat.id, 'Введите фильм, от которого будем отталкиваться')

@bot.message_handler(content_types=["text"])
def handleText(message):
    global inputEnabled 
    if inputEnabled == 1:
        answer = askGigaChat(message.text)
        inputEnabled = 0
        bot.send_message(message.chat.id, '' + answer)
    else:
        bot.send_message(message.chat.id, 'Не понимаю вас( Воспользуйтесь меню для взаимодействия со мной')

def askGigaChat(msg):
    ask = gigaChat.ask(msg)
    print(msg)
    if ask:
        print(ask)
        return ask
    return 'По техническим причинам ответить не могу('


def main():
    bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    main()
