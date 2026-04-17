import telebot
import os
from yt_dlp import YoutubeDL

# Bot Token ကို ဒီမှာထည့်ပါ
BOT_TOKEN = '8300454337:AAEo_SDEnx01V0r5QjJFZulFEw96krMkrk8'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "TikTok Video link ပို့ပေးပါ၊ ဒေါင်းပေးပါမယ်ဗျာ့။")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text
    if 'tiktok.com' in url:
        msg = bot.reply_to(message, "ခဏစောင့်ပါဗျာ့...")
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.mp4',
            'quiet': True
        }
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            with open('video.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video)
            os.remove('video.mp4')
        except Exception as e:
            bot.reply_to(message, f"Error: {str(e)}")
    else:
        bot.reply_to(message, "TikTok link ပို့ပေးပါဗျာ့။")

bot.polling(non_stop=True)
