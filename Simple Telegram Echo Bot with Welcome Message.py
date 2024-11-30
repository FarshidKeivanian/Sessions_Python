import telebot

# Replace with your bot's API token
API_TOKEN = '7520777117:AAGyc3xO7h5RRmRayOQi8PvuKeF9XOEBVnY'

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Command to handle the '/start' or '/hello' message
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to my bot, Farshidkeivanian!")

# Command to handle text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

# Poll the server for new messages
print("Bot is running... Press Ctrl+C to stop.")
bot.polling()
