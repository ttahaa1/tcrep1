import pyrogram
import asyncio
from pyrogram import Client, filters, idle
import re
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
import os
from pyrogram.types import Message
from pyromod import listen
import os
import pyrogram
import redis, re
import asyncio
from pyrogram import Client, idle
from pyrogram import Client as app
from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod import listen
from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, ChatPrivileges
from pyrogram.enums import ChatType
import asyncio
import random

API_ID = int("22665066")
API_HASH = "92dbe89d182f72f427972d8993850130"
DEVS = ["@l_s_I_I"] 
app = Client(
    "mbhfho",
    api_id=int("22665066"),
    api_hash="92dbe89d182f72f427972d8993850130",
    bot_token="7013868761:AAGpTTknQpl7UOhqfLhMqNHI9BwxxcZFY5s", 
    )

@app.on_message(filters.command("دعوة الحسابات للقناة", "") & filters.private, group=8272727727)
async def invite_accounts_to_group(client, message):
    if message.from_user.username not in DEVS:
        return
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        sessions = [session for session in sessions if session.strip()]
    name = await client.ask(message.chat.id, "أرسل الآن الرابط")
    name = name.text
    if "https" in name:
        if not "+" in name:
            name = name.replace("https://t.me/", "")
    for session in sessions:
        user = Client("zomb", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.join_chat(name)
        except Exception as e:
            print(f"Error inviting user: {e}")
        await user.stop()
    await client.send_message(message.chat.id, "تم انضمام {num_accounts} بنجاح")    

@app.on_message(filters.command("انضمام الحسابات للقناة ₂", "") & filters.private, group=8272727727)
async def invite_accounts_to_group(client, message):
    if message.from_user.username not in DEVS:
        return
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        sessions = [session for session in sessions if session.strip()]
    name = await client.ask(message.chat.id, "أرسل الآن الرابط")
    name = name.text
    if "https" in name:
        if not "+" in name:
            name = name.replace("https://t.me/", "")
    for session in sessions:
        user = Client("zomb", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.join_chat(name)
            await user.archive_chats(name)
        except Exception as e:
            print(f"Error inviting user: {e}")
        await user.stop()
    await client.send_message(message.chat.id, "تم انضمام {num_accounts} بنجاح")    
    
@app.on_message(filters.command("مغادره الحسابات للقناة", "") & filters.private, group=827272772772626)
async def leave_accounts_to_group(client, message):
    if message.from_user.username not in DEVS:
        return
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        sessions = [session for session in sessions if session.strip()]
    name = await client.ask(message.chat.id, "أرسل الآن الرابط")
    name = name.text
    if "https" in name:
        if not "+" in name:
            name = name.replace("https://t.me/", "")
    for session in sessions:
        user = Client("zomb", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.leave_chat(name)
        except Exception as e:
            print(f"Error leaving chat: {e}")
        await user.stop()
    await client.send_message(message.chat.id, "تم مغادرة الحساب المساعد بنجاح")

@app.on_message(filters.command("اضف حساب", "") & filters.private, group=827363666)
async def add_assistant_account(client, message):
    if not message.from_user.username in DEVS:
        return
    ask = await client.ask(message.chat.id, "هل لديك جلسة؟", timeout=300)
    me = ask.text
    if me == "لا":
        ask = await client.ask(message.chat.id, "ارسل لي الآن الرقم", timeout=300)
        hossahm = ask.text
        await message.reply_text("انتظر، جاري إرسال الكود")
        cliehnt = Client(name="hfhhfg", api_id=API_ID, api_hash=API_HASH, in_memory=True)
        await cliehnt.connect()
        try:
            code = await cliehnt.send_code(hossahm)
        except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
            return
        ask = await client.ask(message.chat.id, "تم إرسال الكود إلى حسابك، قم بإرسال الكود بهذه الطريقة: 1 2 3 4 5", timeout=300)
        hoam = ask.text
        try:
            await cliehnt.sign_in(hossahm, code.phone_code_hash, hoam)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await message.reply_text("الكود غير صحيح أو انتهت صلاحية الكود")
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await message.reply_text("الكود غير صحيح أو انتهت صلاحية الكود")
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                ask = await client.ask(message.chat.id, "الحساب محمي بكلمة سر، ارسل كلمة السر الآن", timeout=300)
                hm = ask.text
            except TimeoutError:
                return
            try:
                await cliehnt.check_password(password=hm)
                session = await cliehnt.export_session_string()
            except:
                await message.reply_text("كلمة السر غير صحيحة")
                return
        else:
            session = await cliehnt.export_session_string()
        await cliehnt.disconnect()
    elif me == "نعم":
        ask = await client.ask(message.chat.id, "ارسل الجلسه", timeout=300)
        session = ask.text
    file_exists = os.path.exists("sessions.txt")
    with open("sessions.txt", "a") as file:
        if not file_exists:
            file.write(f"{session}\n")
        else:
            file.write("\n")
            file.write(f"{session}\n")
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        user = Client("zomb", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        for dev in DEVS:
            try:
                await user.send_message(dev, "تم تشغيل الحساب عزيزي")
            except Exception as e:
                print(f"Error sending message to developer: {e}")
        await user.stop()
    await client.send_message(message.chat.id, "تم إضافة الحساب بنجاح")

@app.on_message(filters.command("استخراج جلسه", "") & filters.private)
async def mamhcmfbjvbie(client, message):
    ask = await client.ask(message.chat.id, "ارسل لي الان الرقم", timeout=300)
    hossahm = ask.text
    await message.reply_text("انتظر جاري ارسال الكود")
    cliehnt = Client(name="hfhhfg", api_id=API_ID, api_hash=API_HASH, in_memory=True)
    await cliehnt.connect()
    try:
        code = await cliehnt.send_code(hossahm)
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return
    ask = await client.ask(message.chat.id, "تم ارسال الكود الي حسابك قم بارسال الكود \n بهذهي الطريقه : 1 2 3 4 5", timeout=300)
    hoam = ask.text  
    try:
        await cliehnt.sign_in(hossahm, code.phone_code_hash, hoam)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        await message.reply_text("الكود غير صحيح او انتهي صلاحيه الكود")
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        await message.reply_text("الكود غير صحيح او انتهي صلاحيه الكود")
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            ask = await client.ask(message.chat.id, "الحساب محمي بكلمه سر ارسل كلمه السر الان", timeout=300)
            hm = ask.text
        except TimeoutError:
            return
        try:
            await cliehnt.check_password(password=hm)
            string_session = await cliehnt.export_session_string()
        except:
            await message.reply_text("كلمه السر غير صحيحه")
            return  
    else:
        string_session = await cliehnt.export_session_string()
    await cliehnt.disconnect()
    SESSION = string_session
    await client.send_message(message.chat.id, f"تم استخراج الجلسه بنجاح \n `{SESSION}`")
    
@app.on_message(filters.command(["/start"], "") & filters.private, group=71365578)
async def kep(client, message):
    if message.from_user.username not in DEVS:
        return
    kep = ReplyKeyboardMarkup([["جلب نسخة الارقام"], ["اضف حساب", "استخراج جلسه"], ["دعوة الحسابات للقناة", "مغادره الحسابات للقناة"], ["عدد الحسابات", "انضمام الحسابات للقناة ₂"], ["قفل الكيبورد"]], resize_keyboard=True)
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك كيب التحكم بالبوت في سورس سيمو❤️‍🔥", reply_markup=kep)

@app.on_message(filters.command(["قفل الكيبورد"], "") & filters.private, group=71328934689)
async def keplook(client, message):
    m = await message.reply("**- تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب /start**", reply_markup=ReplyKeyboardRemove(selective=True))
 
@app.on_message(filters.command(["جلب نسخة الارقام"], "") & filters.private, group=72636343)
async def upbkgt(client: Client, message: Message):
    with open("sessions.txt", "rb") as file:
        await message.reply_document(document=file)
        
@app.on_message(filters.command("عدد الحسابات", "") & filters.private, group=7263638299)
async def caesar_accounts(client, message):
    if not message.from_user.username in DEVS:
        return
    with open("sessions.txt", "r") as file:
        sessions = file.read().splitlines()
        sessions = [session for session in sessions if session.strip()]
    num_accounts = len(sessions)
    await client.send_message(message.chat.id, f"عدد الحسابات المضافة حالياً هو {num_accounts}")


if __name__ == "__main__": app.run()
