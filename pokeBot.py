import telebot

bot = telebot.TeleBot("6059164019:AAEHW-1JVrqgA2iZL9mD2BCpuvdffIF6KpA", parse_mode=None)

@bot.message_handler(commands=['startbattle', 'joinbattle'])
def handle_commands(message):
	if message.text == '/startbattle':
		waiter = message.from_user.first_name
		bot.reply_to(message, f"{waiter} is waiting for someone to battle..")
	if message.text == '/joinbattle':
		challenger = message.from_user.first_name
		bot.reply_to(message, f"{challenger} has joined the battle!!")
		bot.send_message(message.chat.id , 'First choose 3 pokemon types you prefer. Sepatate by comma' )
	

print('Running')

bot.infinity_polling()
