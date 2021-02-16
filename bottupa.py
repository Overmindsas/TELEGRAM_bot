import telebot
from config import token, HOST, URL_EURO, URL_BUCKS, HEADERS, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK
from telebot import types
import random
import requests
from bs4 import BeautifulSoup
from courdeOOP import Course
from telebot import types
import time


bot = telebot.TeleBot(token)
@bot.message_handler(commands=['goroskop'])
def goroskop(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Овен', callback_data=10))
    markup.add(types.InlineKeyboardButton(text='Телец', callback_data=11))
    markup.add(types.InlineKeyboardButton(text='Близнецы', callback_data=12))
    markup.add(types.InlineKeyboardButton(text='Рак', callback_data=13))
    markup.add(types.InlineKeyboardButton(text='Лев', callback_data=14))
    markup.add(types.InlineKeyboardButton(text='Дева', callback_data=15))
    markup.add(types.InlineKeyboardButton(text='Весы', callback_data=16))
    markup.add(types.InlineKeyboardButton(text='Скорпион', callback_data=17))
    markup.add(types.InlineKeyboardButton(text='Стрелец', callback_data=18))
    markup.add(types.InlineKeyboardButton(text='Козерог', callback_data=19))
    markup.add(types.InlineKeyboardButton(text='Водолей', callback_data=20))
    markup.add(types.InlineKeyboardButton(text='Рыбы', callback_data=21))
    bot.send_message(message.chat.id, text='Выбери знак зодиака:', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='💵курс доллара💵', callback_data=1))
    markup.add(types.InlineKeyboardButton(text='курс евро', callback_data=2))
    markup.add(types.InlineKeyboardButton(text='Three hundred bucks', callback_data=3))
    markup.add(types.InlineKeyboardButton(text='секретная функция', callback_data=4))
    markup.add(types.InlineKeyboardButton(text='погода', callback_data=5))
    bot.send_message(message.chat.id, text='Команды бота:', reply_markup=markup)
    
@bot.callback_query_handler(func = lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    answer = ''
    if call.data == '1':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_BUCKS)
        bot.send_message(call.message.chat.id, 'Курс доллара в данный момент: ' + COURSE.get_CONTENT(html) +' руб.')
    elif call.data == '2':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_EURO)
        bot.send_message(call.message.chat.id, 'Курс евро в данный момент: ' + COURSE.get_CONTENT(html) + ' руб.')
    elif call.data == '3':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_BUCKS)
        bot.send_message(call.message.chat.id, 'Three hundred bucks в данный момент в рублях: ' + str(300*float(COURSE.get_CONTENT(html)))+' руб.')
    elif call.data == '4':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_PORN)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='нASSлаждение', url=COURSE.get_porn_CONTENT(html))
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id, 'Приготовься к rand_porn (Если с телефона, то включи VPN)', reply_markup=keyboard)
    elif call.data == '5':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_WEATHER)
        bot.send_message(call.message.chat.id, str(COURSE.get_WEATHER(html)))
    elif call.data == '10':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'oven.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '11':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'telec.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '12':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'bliznecy.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '13':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'rak.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '14':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'lev.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '15':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'deva.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '16':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'vesy.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '17':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'skorpion.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '18':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'strelec.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '19':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'kozerog.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '20':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'vodolei.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
    elif call.data == '21':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_GOROSKOP+'ryby.html')
        bot.send_message(call.message.chat.id, COURSE.get_goroskop(html))
        


@bot.message_handler(commands = ['нет'])
def minet(message):
    a = ['минет', 'пакет', 'паркет', 'говна пакет', 'мент', 'портрет']
    c = len(a)
    b = random.randint(0, c-1) 
    bot.send_message(message.chat.id, str(a[b]))


@bot.message_handler(commands=['bucks'])
def bucks(message):
    COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
    html = COURSE.get_HTML(URL_BUCKS)
    bot.send_message(message.chat.id, 'Курс доллара в данный момент: ' + COURSE.get_CONTENT(html) +' руб.')


@bot.message_handler(commands=['euro'])
def euro(message):
    COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
    html = COURSE.get_HTML(URL_EURO)
    bot.send_message(message.chat.id, 'Курс евро в данный момент: ' + COURSE.get_CONTENT(html) + ' руб.')


@bot.message_handler(commands = ['300bucks', '300'])
def THB(message):
    COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
    html = COURSE.get_HTML(URL_BUCKS)
    bot.send_message(message.chat.id, 'three hundred bucks в данный момент в рублях: ' + str(300*float(COURSE.get_CONTENT(html)))+' руб.')

#@bot.message_handler(commands = [''])    


@bot.message_handler(commands = ['pogoda'])
def weather(message):
    COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
    html = COURSE.get_HTML(URL_WEATHER)
    bot.send_message(message.chat.id, str(COURSE.get_WEATHER(html)))

@bot.message_handler(commands=['anekdot'])
def anekdot(message):
    spisok = ['Анекдот', 'анекдот', 'анек', 'анекдотус', 'ржомба']
    COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
    html = COURSE.get_HTML(URL_ANEKDOT)
    bot.send_message(message.chat.id, 'лови ржомбу сука')
    bot.send_message(message.chat.id, str(COURSE.get_ANEKDOT(html)))


@bot.message_handler(commands=['porn'])
def rand_porn(message):
    COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
    html = COURSE.get_HTML(URL_PORN)
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='наслаждение', url=COURSE.get_porn_CONTENT(html))
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Лови, сладенький', reply_markup=keyboard)

@bot.message_handler(commands=['анекдот'])
def anekdot(message):
    #receptdnya = ['рецепт дня', 'Рецепт дня', 'рецепт дня!', 'Рецепт дня!']
    #anekdot = ['анек', 'анекдот', 'Ржомба', 'Анекдот', 'Ухахатабл']
    COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
    html = COURSE.get_HTML(URL_ANEKDOT) 
    bot.send_message(message.chat.id, 'лови ржомбу сука')
    bot.send_message(message.chat.id, str(COURSE.get_ANEKDOT(html)))


@bot.message_handler(commands=['праздник'])
def prazdnik(message):
    COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
    html = COURSE.get_HTML(URL_PRAZDNIK)
    bot.send_message(message.chat.id, "🤡Какие праздники сегодня отмечаются🤡") 
    bot.send_message(message.chat.id, str(COURSE.get_prazdnik(html)))

@bot.message_handler(content_types=['text'])
def recept(message):
    if message.text=='рецепт дня':
        COURSE = Course(HOST, URL_BUCKS, URL_EURO, URL_PORN, URL_WEATHER, URL_EDA, URL_ANEKDOT, URL_GOROSKOP, URL_PRAZDNIK)
        html = COURSE.get_HTML(URL_EDA)
        keyboard = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, 'Рецепт дня!')
        url_button = types.InlineKeyboardButton(text='Ссылка на рецептик :)', url=COURSE.get_EDA(html))
        bot.send_photo(message.chat.id, COURSE.get_EDA_photo(html))
        keyboard.add(url_button)
        bot.send_message(message.chat.id, '🍔🍔🍔🍔🍔🍔🍔', reply_markup=keyboard)





if __name__ == "__main__":
    bot.polling(none_stop=True)