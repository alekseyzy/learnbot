from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings



logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

def greet_user(update, context):
    logging.info('Вызвана функция gret_user')

    context.bot.send_message(chat_id=update.message.chat_id, text='Hello')

def talk_to_me(update, context):
    logging.info('Open function talk_to_me')
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
        update.message.chat.id, update.message.text)
    user_text = 'Привет {}! Ты написал {}'.format(update.message.chat.first_name, update.message.text)
    update.message.reply_text(user_text)
    print(update.message)
    

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)
    
    logging.info('The bot runs')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()