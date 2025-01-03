import discord
import random
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hola, ¿Como estas crack?')

    if message.content.startswith('$password'):
        await message.channel.send(gen_pass(15))
    
    if message.content.startswith('$flip'):
        await message.channel.send(flip_coin())
    
    if message.content.startswith('$emoji'):
        await message.channel.send(get_emoji())

    

client.run('TOKEN')
