from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from dotenv import load_dotenv
load_dotenv()
import os
BOT_TOKEN=os.environ.get('BOT_TOKEN')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}! Welcome to my CV bot. Use /help to see available commands.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
    Available commands:
    /contact - Get my contact information
    /experience - See my work experience
    /education - Check my educational background
    /skills - View my key skills
    /projects - View my notable projects

    """
    await update.message.reply_text(help_text)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📞My Contact Information:\n"
        "👋Hi! I'm Sumit,\n"
        "- Email: sumitsonawane418@gmail.com\n"
        "- LinkedIn: www.linkedin.com/in/sumit-sonawane-34a0322aa\n"
        "- GitHub: https://github.com/Sumitsonawane30"
        
    )

async def experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🔧Work Experience:\n"
        " 1. Made an Educational resource sharing 3D-website for our IT Department.\n"
        " 2. Created 'landing page' and 'To-Do-List' as a task assigned during web-development Internship.\n"    
    )

async def education(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🎓Education:\n"
        "- SSC from Deolali High School.\n"
        "- HSC from SVKT College Nashik.\n"
        "- Pursuing BTech in Information Technology in KBTCOE,Nashik.\n"
       
    )

async def skills(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🛠️ My key Skills:\n"
        "-  Web Development\n"
        "-  Chatbot Development\n"
        "-  DSA in C,Cpp\n"
        
    )

async def Projects(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        " Notable projects:\n"
        " 1.Developed an educational notes sharing website with interactable 3D model of our college.\n"
        "  Link:https://sumitsonawane30.github.io/CampusConnectCollab/\n"
        " 2.Tri-Colour of Indian Flag using Html,Css.\n"
        "  Link:https://sumitsonawane30.github.io/Indian_Flag/"
        
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("experience", experience))
app.add_handler(CommandHandler("education", education))
app.add_handler(CommandHandler("skills", skills))
app.add_handler(CommandHandler("Projects", Projects))

app.run_polling()
print("Bot is running...")
