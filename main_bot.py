import discord
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, long = 10):
    await ctx.send(gen_pass(long))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

bot.run('MTMxOTQ1MzMyMTQxNjkzNzQ4Mg.GtVX5g.3RBYP9iX8ZLTA046eIQxPsXxJYscla4FO5H6zw')