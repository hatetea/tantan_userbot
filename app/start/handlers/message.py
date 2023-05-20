from loader import app
from pyrogram.types import Message
from pyrogram import filters
from app.start.mailing import run_tantan

@app.on_message(filters.command(['tan'], prefixes=['/', '!', '.']) & filters.all)
async def run(_, message: Message):
	"""
	## Handler for the message run mailing (with Draft)
	
	"""
	# await message.delete()
	await run_tantan(message)