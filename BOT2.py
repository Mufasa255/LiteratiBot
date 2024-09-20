from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from typing import Final
import logging

TOKEN: Final = '######'
BOT_USERNAME: Final = '@TheLiteratiBot'

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to LiteratiBot! Join our book-loving community!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here are some commands you can use:\n"
        "- suggest: Suggest a book\n"
        "- vote: Vote for the next book\n"
        "- schedule: View the reading schedule\n"
        "- discussion: Join the book discussion\n"
        "- reviews: Share your review\n"
        "- quote: Get a daily quote\n"
        "- author: Learn about the author\n"
        "- resources: Find additional resources\n"
        "- events: See upcoming events\n"
        "- feedback: Give us feedback!"
    )

async def suggest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please suggest a book for our next read!")

async def vote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cast your vote for the next book!")

async def schedule_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here’s the reading schedule: [insert details].")

async def discussion_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Join the ongoing discussion: What are your thoughts on the current book?")

async def reviews_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Share your review of the last book we read!")

async def quote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here’s a thought-provoking quote: [insert quote].")

async def author_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Learn more about the author of our current book: [insert details].")

async def resources_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here are additional resources for the current book.")

async def events_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Upcoming events: [insert event details].")

async def feedback_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("We value your feedback! Let us know how we can improve.")


# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    if update:
        await update.message.reply_text('An error occurred, please try again later.')


# Handle general responses
def handle_response(text: str) -> str:
    processed = text.lower()

    if 'hello' in processed:
        return "Hey there!"
    
    if 'how are you' in processed:
        return 'I am good, thank you!'
    
    if 'i love books' in processed:
        return 'Welcome Home! This is the right place for you!'

    return "Sorry, I didn’t get that. Try using /help to see available commands."

# Messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the type of chat (private, group, supergroup)
    chat_type: str = update.message.chat.type
    text: str = update.message.text

    logger.info(f'User ({update.message.chat.id}) in {chat_type}: "{text}"')

    # If the chat is a group or supergroup
    if chat_type in ['group', 'supergroup']:
        if BOT_USERNAME in text:  # Check if bot is mentioned/tagged
            # Remove the bot's username from the message and process the rest
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            return  # Stay silent unless explicitly tagged in group chats
    elif chat_type == 'private':
        # In private chats, the bot responds to any message
        response = handle_response(text)

    logger.info('Bot:', response)
    await update.message.reply_text(response)

if __name__ == '__main__':
    print('Starting bot....')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('suggest', suggest_command))
    app.add_handler(CommandHandler('vote', vote_command))
    app.add_handler(CommandHandler('schedule', schedule_command))
    app.add_handler(CommandHandler('discussion', discussion_command))
    app.add_handler(CommandHandler('reviews', reviews_command))
    app.add_handler(CommandHandler('quote', quote_command))
    app.add_handler(CommandHandler('author', author_command))
    app.add_handler(CommandHandler('resources', resources_command))
    app.add_handler(CommandHandler('events', events_command))
    app.add_handler(CommandHandler('feedback', feedback_command))

    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error Handler
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)

