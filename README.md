# TanTan Userbot

This is a user bot that can perform various tasks. It includes a command to send draft messages to users and a command to run a mailing with drafts.

## Installation

1. Clone this repository.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
3. Create a `config.py` file and configure the necessary variables. Make sure to include the API credentials for the bot.

## Usage

1. Import the necessary modules and create a Pyrogram client instance.
   ```python
   from pyrogram import Client

   app = Client("user_bot")
   ```

2. Create a `config.py` file with the required configurations. Include the API credentials for the bot.

3. Define the handlers for the commands in your script. For example:

   ```python
   from pyrogram.types import Message
   from pyrogram import filters

   text = '📄help\n\n__prefixes: (!, ., /)tan__ - **🕊рассылка черновиками**'

   @app.on_message(filters.command(['help'], prefixes=['/', '!', '.']) & filters.all)
   async def help(_, message):
       """
       Handler for the message help
       """
       try:
           mess = await message.edit(text)
       except:
           mess = await message.reply(text)
   ```

   ```python
   @app.on_message(filters.command(['tan'], prefixes=['/', '!', '.']) & filters.all)
   async def run(_, message: Message):
       """
       Handler for the message run mailing (with Draft)
       """
       await run_tantan(message)
   ```

4. Implement the `run_tantan` function in your script. This function runs the mailing with draft messages, which is a safer approach for sending bulk messages.

   ```python
   import asyncio
   import random
   import time

   import pyrogram
   from pyrogram.types import Message

   async def run_tantan(message: Message):
       """
       Runs the mailing with draft messages.

       Args:
           message (Message): The message object that triggered the function.

       Returns:
           None
       """

       # Your code for running the mailing goes here

   ```

5. Run your script and start using the user bot commands.

Note: Make sure to create the necessary files and directories mentioned in the code (`data/usernames.csv` and `data/usernames.txt`) and adjust the file paths accordingly.

Remember to handle errors and exceptions appropriately based on your specific use case.

## Feedback and Support

For any feedback, suggestions, or issues, you can contact the bot creator at [Telegram](https://t.me/consentantaneity).

You can also join the official channel [here](https://t.me/instantaneity) for updates and announcements.

The user bot will be periodically updated to improve functionality and address any issues.

Please refer to the Pyrogram documentation for more information on how to use the library: [Pyrogram Documentation](https://docs.pyrogram.org/)

Enjoy using the user bot!
