from loader import app
from pyrogram.types import Message
from pyrogram import filters


text = '📄help\n\n__prefixes: (!, ., /)tan__ - **🕊рассылка черновиками**'

@app.on_message(filters.command(['help'], prefixes=['/', '!', '.']) & filters.all)
async def help(_, message):
	"""
	## Handler for the message help
	"""
	try:
		mess = await message.edit(text)
	except:
		mess = await message.reply(text)
	
