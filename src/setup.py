import subprocess
import sys
import os

REQUERIMENTS = [
    'python-telegram-bot==20.3',
    'deep-translator',   
    'python-dotenv==1.0.0' 
]

def installation():
    """
    Installation of the necessary dependencies to run the bot.
        telegram: classes to interact with the telegram API
        deep-translator
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requeriments.txt"])
        print("Dependencies installed correctly :)")
        return True
    except subprocess.CalledProcessError:
        print("Error Installing depency :(")
        print("Try manually")
        print("pip install -r requeriments.txt")
        return False
    
if __name__ == "__main__":
    print("Installing Dependencies...")
    if installation():
        print("Execute Bot: python -m src.bot.py")




