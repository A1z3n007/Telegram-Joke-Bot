import telebot
import random

BOT_TOKEN = 'YOU_API_TOKEN'
bot = telebot.TeleBot(BOT_TOKEN)

jokes = [
    "— Why do programmers confuse New Year and Halloween?\n— Because October 31 = 31(8) = 25(10).",
    "The boss says to the programmer:\n— Why is your program so slow?\n— Because you asked to make it as clear as possible for other programmers!",
    "The engineers created a time machine. The programmers made a rollback.",
    "If the program is too slow, add a loading screen with the inscription 'Optimizing data...' — users love magic.",
    "The programmer's wife sent him to the store: 'Buy some bread. If there are eggs, take a dozen.' The programmer came back with ten loaves of bread.",
    "Why do IT people like dark theme? Because light theme zeroes out their eyes faster than deadline projects.",
    "Programmer with a girl in a restaurant: 'I'd like a burger, please. And a burger for her, to avoid a merge conflict.'",
    "Developer at a meeting: 'I don't have bugs, I have features with unexpected behavior.'",
    "Teacher: 'What's more important: theory or practice?' Programmer: 'Google.'",
    "The difference between an engineer and a programmer? A programmer fixes a bug, an engineer fixes the process that creates it."
]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi! I'm a joke bot 🤣\nSend /joke to get a random joke!")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = random.choice(jokes)
    bot.send_message(message.chat.id, joke)

@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    bot.send_message(message.chat.id, "Unknown command. Use /joke to get a joke.")

print("Bot launched... ✅")
bot.polling(none_stop=True)
