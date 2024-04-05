import telebot

bot = telebot.TeleBot('7128094167:AAEGqYAmzsa1f0txk3MhsMUr8iGnVmLN0aI')

@bot.message_handler(commands=['start','help'])
def reply_message(message):
    bot.reply_to(message, 'مرحبا برسالتك')

bot.infinity_polling()
