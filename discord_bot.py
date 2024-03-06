import discord
import webscraper
from bot_token import bot_token

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(1214656130882609152)
    links = webscraper.top3()
    await channel.send(links)



client.run(bot_token)
