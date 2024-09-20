import os
from dotenv import load_dotenv
import telebot

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Command handlers
@bot.message_handler(commands=['start','hello'])
def welcome(message):
    bot.reply_to(message, "Welcome to LiteratiBot! Join our book-loving community!")

@bot.message_handler(commands=['suggest'])
def suggest(message):
    bot.reply_to(message, "Please suggest a book for our next read!")

@bot.message_handler(commands=['vote'])
def vote(message):
    bot.reply_to(message, "Cast your vote for the upcoming book! Reply with your choice.")

@bot.message_handler(commands=['schedule'])
def schedule(message):
    bot.reply_to(message, "Here’s the reading schedule: [insert schedule details].")

@bot.message_handler(commands=['discussion'])
def discussion(message):
    bot.reply_to(message, "Join the ongoing book discussion! What are your thoughts on the current read?")

@bot.message_handler(commands=['reviews'])
def reviews(message):
    bot.reply_to(message, "Share your review of the last book we read!")

@bot.message_handler(commands=['quote'])
def quote(message):
    bot.reply_to(message, "Here’s a thought-provoking quote: [insert quote].")

@bot.message_handler(commands=['author'])
def author(message):
    bot.reply_to(message, "Learn more about the author of our current book: [insert author details].")

@bot.message_handler(commands=['resources'])
def resources(message):
    bot.reply_to(message, "Here are additional resources related to our current book: [insert resources].")

@bot.message_handler(commands=['events'])
def events(message):
    bot.reply_to(message, "Stay updated on our upcoming events: [insert event details].")

@bot.message_handler(commands=['feedback'])
def feedback(message):
    bot.reply_to(message, "We value your feedback! Let us know how we can improve.")

@bot.message_handler(commands=['favorites'])
def favorites(message):
    bot.reply_to(message, "Here’s a list of our community's all-time favorite books: [insert favorites].")

@bot.message_handler(commands=['nextbook'])
def nextbook(message):
    bot.reply_to(message, "Get ready for our next read: [insert next book details].")

# Polling the bot
bot.polling()
