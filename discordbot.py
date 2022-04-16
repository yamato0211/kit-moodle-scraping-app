import discord
from scraping import scraping_data
from key import TOKEN


client = discord.Client()
todos = []


@client.event
async def on_ready():
    print("ログインしました!")


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'moodle':
        await message.channel.send("少々お待ちください")
        todos = scraping_data()
        for todo in todos:
            await message.channel.send(todo)

client.run(TOKEN)
