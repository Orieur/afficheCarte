from discord.ext.commands import Bot
import os

BOT_PREFIX = ("?")
access_token= os.environ["ACCESS_TOKEN"]


client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
	if message.content.startswith("?"):
		newMessage = 'https://www.cardgame.fr/assets/images/cards_medium/' + str(message.content)[1:].upper() + '.png'
		await client.send_message(message.channel, newMessage)
	
client.run(TOKEN)
