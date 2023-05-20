from pyrogram import Client
import os
from config import api_id, api_hash

app = Client(
    "userbot",
    8887614,
    "ca33af4560d217a03066c4e6c2c7742d"
)

def send_hello():
	app.send_message("consentantaneity", "🌧")
	app.send_message("consentantaneity", f"🌧tantan-userbot запущен")

os.system('cls')
def run():
	# app.start()
	# send_hello()
	# app.stop()
	app.run()