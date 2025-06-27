# 🤖 LinguaTranslateSpark

LinguaTranslateSpark is my personal Telegram bot that translates text on the fly using Google Translate via the `deep-translator` library. I built it to sharpen my skills with bots and automatic translation, and figured it might be handy for anyone who needs a quick translation in chat.

---

## 🚀 Key Features

* **Instant Translation:** Send any text and get it translated in seconds.
* **100+ Languages:** Supports a wide variety of languages (English, Spanish, German, Chinese, and more).
* **Interactive Buttons:** Change your target language, view current settings, or get help, all with a tap.
* **Per-User Preferences:** Your language choice sticks for your session—no need to retype it every time.
* **Easy Deployment:** Works locally or on PythonAnywhere with minimal setup.

---

## 🛠 Tech Stack

* **Language:** Python 🐍
* **Telegram Framework:** `python-telegram-bot`
* **Translation API:** `deep-translator` (Google Translate)

---

## 📦 Local Setup

1. Clone or download this repository.
2. Install dependencies:

   ```bash
   pip install python-telegram-bot deep-translator
   ```
3. Open `bot.py` and insert your BotFather token:

   ```python
   TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   ```
4. Run the bot:

   ```bash
   python bot.py
   ```
5. Chat with your bot on Telegram! 🎉

---

## ☁️ Deploy on PythonAnywhere

1. Upload `bot.py` to your PythonAnywhere account (Files tab).
2. In a Bash console, install dependencies:

   ```bash
   pip install --user python-telegram-bot deep-translator
   ```
3. Run the bot:

   ```bash
   python3 bot.py
   ```

> **Note:** Free accounts sleep after some idle time. To keep the bot running, leave the console open or set up a scheduled task.

---

## 📋 Bot Commands

| Command  | Description                       |
| -------- | --------------------------------- |
| `/start` | Show welcome message and buttons. |
| `/lang`  | Pick a new target language.       |
| `/info`  | View your current settings.       |
| `/help`  | Get a quick command overview.     |

Plus: any plain text you send will get auto-translated to your selected language.

---

## 🎮 Example Session

1. Send `/start` to see the welcome message with buttons.
2. Tap **Change Language** and choose **Spanish**.
3. Send `Hello, how are you?`.
4. The bot replies with `Hola, ¿cómo estás?`.

---

## 🔒 Privacy & Data

* This bot does **not** log or store your messages permanently.
* Language preferences are kept in memory for each session only.

---

## 👤 About Me

I’m Jean Estevez

* Twitter: [@jeantvz](https://twitter.com/jeantvz)
* GitHub: [Jean-EstevezT](https://github.com/Jean-EstevezT)

---

## 🙏 Acknowledgements

* Huge thanks to everyone who tests the bot and sends feedback!

---

## 📄 License

This project is released under the MIT License. Feel free to use, modify, and share it as you like.
