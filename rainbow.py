from discord import Game
import aiohttp
import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord.utils import find

client = commands.Bot(command_prefix=".")
Client = discord.Client()
client.remove_command('help')

@client.event
async def on_ready():
    try:
        server2 = client.get_server(id="szerver id")
        szszam = int(len(client.servers))
        while True:
            for server in client.servers:
                role = discord.utils.get(server2.roles, id="rang id")
                try:
                    i = random.randint(0,1)
                    colours = random.randint(0, 0xFFFFFF)
                    await client.edit_role(server=server2, role=role, colour=discord.Colour(colours))
                    await asyncio.sleep(5)
                    await client.change_presence(game=discord.Game(name="Rainbow bot By.: FightMan01"))
                except Exception as e:
                    print(e)
                    await client.change_presence(game=discord.Game(name="Rainbow bot By.: FightMan01"))
                    await asyncio.sleep(5)
                    continue
    except:
        pass

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Rainbow bot".format(ctx.message.server.name), description="Készítette: FightMan01", color=0x00ff00, timestamp=ctx.message.timestamp)
    await client.say(embed=embed)

client.run("TOKEN")
