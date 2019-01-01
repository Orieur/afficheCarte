from discord.ext.commands import Bot

BOT_PREFIX = ("?")
TOKEN = "NTA3ODMxMDAyNjU2NDA3NTUy.Dwmt4A.9ByNjPjeAs1NUKbbCSrlgTlInUY"

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
	if message.content.startswith("?"):
		newMessage = 'https://www.cardgame.fr/assets/images/cards_medium/' + str(message.content)[1:].upper() + '.png'
		await client.send_message(message.channel, newMessage)
	
client.run(TOKEN)
