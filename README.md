# Haraslia Bot 🤖

A Telegram bot built with Python. It greets users, echoes messages, and
fetches live weather data for any city using the free
[Open-Meteo](https://open-meteo.com/) API.

## Features

- `/start` — Welcome message
- `/help` — List available commands
- `/sapa` — Personalized greeting
- `/cuaca <kota>` — Current weather (temperature & wind speed) for a city
- Echo reply for any other message

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/dimasd18/bot-telegram-haraslia.git
   cd bot-telegram-haraslia
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a bot via [@BotFather](https://t.me/BotFather) and get your token.

4. Run the bot with the token as an environment variable:
   ```bash
   export BOT_TOKEN="123456789:AAYourTokenHere"
   python bot.py
   ```

> **Note:** Never hardcode your bot token in source code. This project reads
> it from the `BOT_TOKEN` environment variable, and `.env` files are
> git-ignored.

## Tech stack

- Python 3
- [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)
- [requests](https://requests.readthedocs.io/)
- [Open-Meteo API](https://open-meteo.com/) — no API key required

## License

MIT — see [LICENSE](LICENSE).
