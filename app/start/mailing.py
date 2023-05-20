import asyncio
import random
import time

import pyrogram
from pyrogram import Client, filters, raw
from pyrogram.types import Message

from loader import app


async def run_tantan(message: Message):
    """
    Запускает рассылку сообщений пользователям.

    Args:
        message (Message): Объект сообщения, который вызвал функцию.

    Returns:
        None
    """

    start_time = time.time()
    start_text = "**🕊 Рассылочка запущена 🕊**\n__👀 Тебе прилетит сообщение, когда рассылка завершится.__"
    try:
        mess = await message.edit(start_text)
    except:
        mess = await message.reply(start_text)

    usernames = get_usernames_from_csv()
    usernames_txt = get_usernames_from_txt()

    count = 0
    for i in range(100):
        try:
            username = get_random_username(usernames, usernames_txt)
            peer = await app.resolve_peer(username)

            count += 1
            await send_draft_message(peer, "привет")
            await update_progress_message(message.chat.id, mess.id, count)

            save_username_to_txt(username)

            await asyncio.sleep(random.randint(3, 5))
        except:
            continue

    elapsed_time = time.time() - start_time
    completion_message = create_completion_message(count, elapsed_time)
    await send_completion_message(message.chat.id, completion_message)
    await message.delete()


def get_usernames_from_csv() -> list:
    """
    Получает список имен пользователей из CSV-файла.

    Returns:
        list: Список имен пользователей.
    """

    with open("data/usernames.csv", "r", encoding="utf-8") as f:
        usernames = f.read().split("\n")
    return usernames


def get_usernames_from_txt() -> list:
    """
    Получает список имен пользователей из TXT-файла.

    Returns:
        list: Список имен пользователей.
    """

    with open("data/usernames.txt", "r", encoding="utf-8") as f:
        usernames_txt = f.read().split("\n")
    return usernames_txt


def get_random_username(usernames: list, usernames_txt: list) -> str:
    """
    Возвращает случайное имя пользователя, которое еще не было использовано.

    Args:
        usernames (list): Список имен пользователей из CSV-файла.
        usernames_txt (list): Список имен пользователей из TXT-файла.

    Returns:
        str: Случайное имя пользователя.
    """

    while True:
        username = random.choice(usernames)
        if username not in usernames_txt:
            return username


async def send_draft_message(peer, message: str):
    """
    Отправляет черновое сообщение пользователю.

    Args:
        peer: Пир пользователя.
        message (str): Текст сообщения.

    Returns:
        None
    """

    await app.invoke(raw.functions.messages.SaveDraft(peer=peer, message=message))


async def update_progress_message(chat_id, message_id, count):
    """
    Обновляет сообщение с информацией о прогрессе рассылки.

    Args:
        chat_id: ID чата.
        message_id: ID сообщения.
        count (int): Количество отправленных сообщений.

    Returns:
        None
    """

    progress_message = f"**🕊 Рассылочка запущена 🕊**\n__👀 Тебе прилетит сообщение, когда рассылка завершится__\n\n💎 Отправлено: {count}"
    await app.edit_message_text(chat_id, message_id, progress_message)


def save_username_to_txt(username: str):
    """
    Сохраняет использованное имя пользователя в TXT-файл.

    Args:
        username (str): Имя пользователя.

    Returns:
        None
    """

    with open("data/usernames.txt", "a", encoding="utf-8") as f:
        f.write("\n" + username)


def create_completion_message(count: int, elapsed_time: float) -> str:
    """
    Создает сообщение о завершении рассылки.

    Args:
        count (int): Количество отправленных сообщений.
        elapsed_time (float): Время выполнения в секундах.

    Returns:
        str: Сообщение о завершении рассылки.
    """

    completion_message = f"**🌼 Отлично!**\n__👉🏻 {count} чернов__.\n⏱ Время работы: {elapsed_time:.2f} секунд."
    return completion_message


async def send_completion_message(chat_id, message: str):
    """
    Отправляет сообщение о завершении рассылки.

    Args:
        chat_id: ID чата.
        message (str): Сообщение о завершении рассылки.

    Returns:
        None
    """

    await app.send_message(chat_id, message)
