from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from gtts import gTTS
import os

# Telegram bot token (replace 'YOUR_BOT_TOKEN' with your bot token)
TOKEN = 'YOUR_BOT_TOKEN'

# Define button options
button_options = [
    [KeyboardButton('Hello'), KeyboardButton('Goodbye')],
    [KeyboardButton('Speak')],
]

# Create ReplyKeyboardMarkup with buttons
reply_markup = ReplyKeyboardMarkup(button_options, resize_keyboard=True)

# Function to start the conversation and display buttons
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi! I'm a chatbot. Press a button to interact.", reply_markup=reply_markup)

# Function to handle messages with buttons
def button_response(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == 'Hello':
        update.message.reply_text("Hello there!")
    elif text == 'Goodbye':
        update.message.reply_text("Goodbye!")
    elif text == 'Speak':
        tts = gTTS(text="I am speaking!", lang='en', slow=False)
        tts.save("output.mp3")
        os.system("mpg321 output.mp3") # Replace with your OS's audio player command

# Function to handle messages without buttons
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handler to start the conversation
    dispatcher.add_handler(CommandHandler('start', start))

    # Add message handler to respond to button clicks
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, button_response))

    # Add message handler to handle other messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
