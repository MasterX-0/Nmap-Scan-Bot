import pyrogram,os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters

BOT_TOKEN = "6181646722:AAHawj5TkcTjv9cgWIvyftbVUQba1pPZqHM"
API_HASH = "9d2c6cdf712fc6cd9e667567111a1cb8"
API_ID = int(9247680)

path = "/root/Simple-Shell-Bot"

bot = Client(
	"shell_bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN,
)

@bot.on_message(filters.command("run"))
async def runshell(bot, message):
	chat = message.chat.id
	query = query = message.text.split(None, 1)[1]
	if chat == int(-1001759398729):
		m = await message.reply_text("Running... ✨️🌿")
		os.system(f"{query} >> {path}config.txt")
		o = open(""+path+"config.txt", "r")
		await message.reply_text(o.read())
		os.system("rm -rf "+path+"config.txt")
	else:
		await message.reply_text("`Error...`")

print ("running")
bot.run()
