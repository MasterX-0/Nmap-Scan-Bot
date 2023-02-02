import pyrogram,os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import MessageEmpty
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong

BOT_TOKEN = "6181646722:AAF9l4MCuAn4zUkV1AStdfuGV2FNOUkWbAM"
API_HASH = "9d2c6cdf712fc6cd9e667567111a1cb8"
API_ID = int(9247680)

path = "nmap_bot/"

bot = Client(
	"nmap_bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN,
)

HELP = """
**Commands :

  >  /help
  >  /nmap
  >  /ping
  >  /run
**
"""

@bot.on_message(filters.command("help"))
async def help(bot, message):
	await message.reply_text(HELP)

@bot.on_message(filters.command("nmap"))
async def runnmap(bot, message):
	chat = message.chat.id
	query = query = message.text.split(None, 1)[1]
	if os.path.exists(f"{path}_nmap.txt"):
		os.remove(f"{path}_nmap.txt")
	else:
		pass
	try:
		if chat == int(-1001759398729):
			os.system(f"nmap {query} >> {path}_nmap.txt")
			o = open(f"{path}_nmap.txt", "r")
			await message.reply_text(o.read(), disable_web_page_preview=True)
		else:
			await message.reply_text("`Error...`")
	except MessageTooLong:
		await message.reply_document(f"{path}_nmap.txt", caption=f"**Nmap :** `{query}`")

@bot.on_message(filters.command("ping"))
async def ping(bot, message):
	chat = message.chat.id
	query = query = message.text.split(None, 1)[1]
	if os.path.exists(f"{path}ping.txt"):
		os.remove(f"{path}ping.txt")
	else:
		pass
	try:
		if chat == int(-1001759398729):
			os.system(f"ping -c 4 {query} >> {path}ping.txt")
			Z = open(f"{path}ping.txt", "r")
			await message.reply_text(Z.read(), disable_web_page_preview=True)
		else:
			await message.reply_text("`Error...`")
	except MessageTooLong:
		await message.reply_document(f"{path}ping.txt", caption=f"**Ping :** `{query}`")

@bot.on_message(filters.command("run") & filters.user(5262156299))
async def shell(bot, message):
	chat = message.chat.id
	query = query = message.text.split(None, 1)[1]
	if os.path.exists(f"{path}_run.txt"):
		os.remove(f"{path}_run.txt")
	else:
		pass
	try:
		try:
			if chat == int(-1001759398729):
				os.system(f"cd;{query} >> {path}_run.txt")
				S = open(f"{path}_run.txt", "r")
				await message.reply_text(S.read(), disable_web_page_preview=True)
			else:
				await message.reply_text("`Error...`")
		except MessageEmpty:
			await message.reply_text("`Message Empty Error`")
	except MessageTooLong:
		await message.reply_document(f"{path}_run.txt", caption=f"**Command :** `{query}`")

print ("Running...")
bot.run()
