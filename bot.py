import os
import json
import discord
from discord.ext import commands
from server_comms import *
from dotenv import find_dotenv, load_dotenv

payload = {
    "token": "token",
    "username": "anon",
    "password": "anon"
}

load_dotenv(find_dotenv())

server_token = os.getenv("SECRET")
token = os.getenv("DISCORD-TOKEN")
prefix = os.getenv("DISCORD-PREFIX")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
@commands.is_owner()
async def passwords(ctx):
    passwords = json.loads(getPasswords(payload, server_token))
    embed=discord.Embed(title="Passwords")

    for username, password in passwords.items():
        embed.add_field(name=f"🔑 {username}", value=f"🔒 ||{password}||", inline=True)
    embed.set_footer(text="Password Manager | 🚲")
    await ctx.send(embed=embed, reference=ctx.message)

@bot.command()
@commands.is_owner()
async def addPassword(ctx, username, password):
    result = addPasswordToServer(payload,server_token,username,password)
    await ctx.send(result, reference=ctx.message)

@bot.command()
@commands.is_owner()
async def removePassword(ctx, username):
    result = removePasswordFromServer(payload,server_token,username)
    await ctx.send(result, reference=ctx.message)

bot.run(token=token)