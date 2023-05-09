from typing import final
from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler , filters , ContextTypes

Token : final =  "6217520320:AAFiVBe8v748UgfPIWCfOyRcZI_vWY-o8jk"

Bot_userN = "@testEnoughBOt"

async def start_command(update : Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello , im testing bot for learning")

async def help_command(update : Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("what can i do ? can i help you?")

async def custom_command(update : Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this is a custom command:)")

def handle_response(processed:str)-> str:
    processed :str = processed.lower()


    if "hello" in processed:
        return "hey guys"
    
    if "how are you" in processed:
        return "i am good"
    
    if "i love python" in processed :
        return "remember to subscribe!"
    
    return "sorry! i dont unstand what you wrote"


async def handel_message(update :Update, context: ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type
    text : str = update.message.text

    print(f"user ({update.message.chat.id})in (message_type):'{text}'")
     

    if message_type == 'group':
        if Bot_userN in text: 
            new_text : str = text.replace(Bot_userN , '').strip()
            response :str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)



async def error (update: Update, context : ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error {context.error}')



if __name__ == '__main__':
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))



    app.add_handler(MessageHandler(filters.TEXT,handel_message))

    app.add_error_handler(error)

    print('polling...')
    app.run_polling(poll_interval=3)