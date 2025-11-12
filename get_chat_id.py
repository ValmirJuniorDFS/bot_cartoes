import telebot

# Substitua pelo seu token
TOKEN = "8152732950:AAGiXy62zvTu kR6bj-jNACqbFV_xoSALLa8".replace(" ", "")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Seu chat_id é: {message.chat.id}")

print("Bot rodando... Envie /start para o bot no Telegram.")
bot.polling()
