#!/home/sheps/webscraper/.venv/bin/python
import discord
import webscraper
import os


bot_token = os.environ["DISCORD_TOKEN"]


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(1214656130882609152)
    links = webscraper.top3()
    await channel.send(links)
    await client.close()



client.run(bot_token)

