import telebot
import requests

TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def mulai(message):
    bot.reply_to(message, "Halo! Saya Haraslia Bot! 🤖\nKetik /help untuk bantuan.")

@bot.message_handler(commands=["help"])
def bantuan(message):
    bot.reply_to(message, "Perintah yang tersedia:\n/start - Mulai bot\n/sapa - Sapa saya\n/help - Bantuan\n/Cuaca - cek cuaca kota")

@bot.message_handler(commands=["sapa"])
def sapa(message):
    nama = message.from_user.first_name
    bot.reply_to(message, f"Halo, {nama}! Selamat datang! 😊")

@bot.message_handler(commands=["cuaca"])
def cek_cuaca(message):
    teks = message.text.split()
    if len(teks) < 2:
        bot.reply_to(message, "Format: /cuaca nama_kota\nContoh: /cuaca bogor")
        return
    kota = teks[1]
    geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={kota}&count=1")
    data_geo = geo.json()
    if not data_geo.get("results"):
        bot.reply_to(message, f"Kota '{kota}' tidak ditemukan!")
        return
    lat = data_geo["results"][0]["latitude"]
    lon = data_geo["results"][0]["longitude"]
    nama_kota = data_geo["results"][0]["name"]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    data_cuaca = requests.get(url).json()["current_weather"]
    bot.reply_to(message, f"Cuaca di {nama_kota}:\nSuhu: {data_cuaca['temperature']} C\nAngin: {data_cuaca['windspeed']} km/h")

@bot.message_handler(func=lambda m: True)
def balas_pesan(message):
    bot.reply_to(message, f"Kamu bilang: {message.text}")

bot.polling()