from telegram.ext import * #load python-telegram-bot module
from telegram.update import Update #load python-telegram-bot module
from telegram.bot import Bot #load python-telegram-bot module
import config #load conig.py file
from pytube import YouTube # load module that use to download YT videos
from telegram import ReplyKeyboardMarkup #load python-telegram-bot module


def respons(update: Update, context: CallbackContext): # function to get text updates of bot
    text = update.message.text # assining text of the message to a variable
    chat_id = update.effective_chat.id # assining chat id to a variable
    f_name = update.effective_user.first_name # assining first name of user to a variable
    chat_type = update.effective_chat.type # assining chat type(private, group, channel) to a variable
    
    if chat_type == 'private': # get private message only
        if text in ('/start', '/Start', '⏪ BACK'): # if user send this command,  
            Main_menu(chat_id, f_name)
        elif text in ('/help', '/Help'): # else if user send this command, 
            bot.send_message(chat_id = chat_id, text = 'Bot Admin: @F0restron09') # reply this message 
        elif text == 'DOWNLOAD YOUTUBE VIDEOS ⬇️': # if user press that button send below message
            bot.send_message(chat_id = chat_id, text = 'Hello {} 👋. Send me a youtube link to download.'.format(f_name)) # send this message to chat id
        elif text in ('COLLEGE NOTES 📚', '⏪⏪ BACK'): # if user press this buttons move to this COLLEGE_NOTES function 
            COLLEGE_NOTES(chat_id)
        elif text in ('Cociricular','⏪ BACK'): # same - check button and move funtion
            cocuricular(text, chat_id)    
        elif text in ('🔰 SEMESTER 3', '🔰 SEMESTER 4'): # same - check button and move funtion
            Send_PDF_urls(text, chat_id)
        elif text == '🔹 DBMS': # check button and send message
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem4_DBMS)) # get variable from config file, assing it to the message and send message
        elif text == '🔹 PYTHON':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem4_PYTHON))
        elif text == '🔹 DAA':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem4_DAA))
        elif text == '🔹 OS':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem4_OS))
        elif text == '🔹 MATHS':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem4_MATHS))
        elif text == '🔹 SE':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem4_SE))
        elif text == '🔹 EXAMS':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem4_EXAMS))
        elif text == '🔹 JOURNALS':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem4_JOURNALS))
        elif text == '🔸 CO':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem3_CO))
        elif text == '🔸 DE':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem3_DE))
        elif text == '🔸 DS':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem3_DS))
        elif text == '🔸 MATHS':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem3_MATHS))
        elif text == '🔸 JAVA': 
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem3_JAVA))
        elif text == '🔸 EXAMS':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem3_EXAMS))
        elif text == '🔸 WP':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.sem3_WP))
        elif text == 'INTERNSHIP ONGOING AND UPCOMING 🎁':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.url_INTERNSHIP))
        elif text == 'nptel':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.n_nptel))
        
        elif text == '🔰 WEB DEVELOPMENT':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.c_WEB_DEVELOPMENT))
        elif text == '🔰 JAVASCRIPT':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.c_JAVASCRIPT))
        elif text == '🔰 STOCKMARKET':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.c_STOCKMARKET))
        elif text == '🔰 CRYPTO':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.c_CRYPTO))
        elif text == '🔰 C++':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.c_C_plus))
        elif text == '🔰 JAVA':
            bot.send_message(chat_id = chat_id, text = '🔰 Thank you for using the bot here is your link: {}'.format(config.c_JAVA))
        elif text == 'COURSES 📁':
            COURSES(chat_id)
        elif text=='cocuricular':
            cocuricular(chat_id)
        elif text=='valorant':
            bot.send_message(chat_id= chat_id,text='🔰 Thank you for using the bot here is your link: {}'.format(config.cocuricular_valorant))
        elif text=='csgo':
            bot.send_message(chat_id= chat_id,text='🔰 Thank you for using the bot here is your link: {}'.format(config.cocuricular_csgo))
        else: #  filter all other message without /start and /help
            bot.send_message(chat_id = chat_id, text = 'Please wait. Your video is downloading... 👨🏼‍💻'.format(f_name)) # reply this message And
            Download_video(text, chat_id) # pass that message update(YT link) to download function

def COURSES(chat_id): # course function
    custom_keyboard = [['🔰 WEB DEVELOPMENT', '🔰 JAVASCRIPT'],['🔰 STOCKMARKET', '🔰 CRYPTO'],['🔰 C++', '🔰 JAVA'], 
                        ['⏪ BACK']] # create buttons and assing variable
    inline = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True) # connect buttons with telegram module
    bot.send_message(
            chat_id = chat_id, # the chat bot send this message
            text = '👨🏼‍💻 Please select a Cours that you want to get:', # message
            reply_markup= inline # Assing buttons to the message
        )
# other functions same as COURSES function

def COLLEGE_NOTES(chat_id):
    custom_keyboard = [['🔰 SEMESTER 3', '🔰 SEMESTER 4'], 
                        ['⏪ BACK']]
    inline = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True)
    bot.send_message(
            chat_id = chat_id, 
            text = '👨🏼‍💻 Please select a semester that you want to get pdfs:', 
            reply_markup= inline
        )

def cocuricular(chat_id):
    custom_keyboard =[['valorant','csgo'],['⏪ BACK']]
    inline = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True)
    bot.send_message(
        chat_id=chat_id,
        text = '👨🏼‍💻 Please select a game You want to play', 
        reply_markup= inline
    )
    
def Send_PDF_urls(text, chat_id):
    if text == '🔰 SEMESTER 4':
        custom_keyboard = [['🔹 DBMS', '🔹 PYTHON'], ['🔹 DAA', '🔹 OS'], ['🔹 MATHS', '🔹 SE'], ['🔹 EXAMS', '🔹 JOURNALS'], 
                        ['⏪⏪ BACK']]
    elif text == '🔰 SEMESTER 3':
        custom_keyboard = [['🔸 CO', '🔸 DE'], ['🔸 DS', '🔸 MATHS'], ['🔸 JAVA', '🔸 EXAMS'], ['🔸 WP'], 
                        ['⏪⏪ BACK']]
    inline = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True)
    bot.send_message(
            chat_id = chat_id, 
            text = '👨🏼‍💻 Please select a Subject that you want to get pdfs:', 
            reply_markup= inline
        )

def Main_menu(chat_id, f_name):
    custom_keyboard = [['COLLEGE NOTES 📚', 'COURSES 📁'], 
                        ['INTERNSHIP ONGOING AND UPCOMING 🎁'], 
                        ['DOWNLOAD YOUTUBE VIDEOS ⬇️','cocuricular'],['nptel']]
    inline = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True)
    bot.send_message(
            chat_id = chat_id, 
            text = 'Hello {} 👋.\n\n{}'.format(f_name, config.welcome_msg), 
            reply_markup= inline
        )
       
def Download_video(text, chat_id): # function that download YT videos
    try: # check errors of bellow 7 lines
        yt = YouTube(text) # connect user input text with YT download python module and assing it to a variable
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() # get mp4 file and filter best resolution and assing it to variable        
        video_saved_path = yt.download(filename='Downloaded_Video') # Download video and assing it to variable(variable gives downloaded path)
        bot.send_video( # Send downloaded video
            chat_id = chat_id, # chat of bot and user
            video = open(video_saved_path, 'rb') # load video to send
        )
        
    except: # if abow lines gives errors send that message to user
        bot.send_message(chat_id = chat_id, text = '❌ Invalid URL. Please try again')
            

if __name__ == '__main__': # tha way to run abow lines in python
    bot = Bot(config.token) # load bot token and assing it to avariable
    updater = Updater(config.token, use_context=True) # connect bot token and assing it to avariable
    dp = updater.dispatcher 
    dp.add_handler(MessageHandler(Filters.text, respons)) # filter all text messages of users and send it to respons function
    updater.start_polling() # start bot
    updater.idle() 
