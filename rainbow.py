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
        server2 = client.get_server(id="416227463471824896")
        szszam = int(len(client.servers))
        #colours = ['FF0000', 'FF0F00','#FF1F00','#FF2E00','#FF3D00','#FF4D00','#FF5C00','#FF6B00','#FF7A00','#FF8A00','#FF9900','#FFA800','#FFB800','#FFC700','#FFD600','#FFE500','#FFF500','#FAFF00','#EBFF00','#DBFF00','#CCFF00','#BDFF00','#ADFF00','#9EFF00','#8FFF00','#80FF00','#70FF00','#61FF00','#52FF00','#42FF00','#33FF00','#24FF00','#14FF00','#05FF00','#00FF0A','#00FF19','#00FF29','#00FF38','#00FF47','#00FF57','#00FF66','#00FF75','#00FF85','#00FF94','#00FFA3','#00FFB3','#00FFC2','#00FFD1','#00FFE0','#00FFF0','#00FFFF','#00F0FF','#00E0FF','#00D1FF','#00C2FF','#00B2FF','#00A3FF','#0094FF','#0085FF','#0075FF','#0066FF','#0057FF','#0047FF','#0038FF','#0029FF','#0019FF','#000AFF','#0500FF','#1400FF','#2400FF','#3300FF','#4200FF','#5200FF','#6100FF','#7000FF','#8000FF','#8F00FF','#9E00FF','#AD00FF','#BD00FF','#CC00FF','#DB00FF','#EB00FF','#FA00FF','#FF00F5','#FF00E6','#FF00D6','#FF00C7','#FF00B8','#FF00A8','#FF0099','#FF008A','#FF007A','#FF006B','#FF005C','#FF004D','#FF003D','#FF002E','#FF001F','#FF000F']
        #colours = [0xFF0000, 0x00FF00, 0x0000FF0, 0x00a0b0, 0x008080, 0xfaebd7, 0xde5462, 0xde5462 ,0x81899b, 0xFF0F00, 0xFF1F00, 0xFF2E00]
        while True:
            for server in client.servers:
                statuses = ["{} szerver | .help".format(str(len(client.servers))), "{} szerver | .multicolor".format(str(len(client.servers)))]
                role = discord.utils.get(server2.roles, id="587684101562302475")
                try:
                    i = random.randint(0,1)
                    colours = random.randint(0, 0xFFFFFF)
                    await client.edit_role(server=server2, role=role, colour=discord.Colour(colours))
                    await asyncio.sleep(5)
                    await client.change_presence(game=discord.Game(name=random.choice(statuses)))
                    print("Megy!")
                except Exception as e:
                    print(e)
                    await client.change_presence(game=discord.Game(name=random.choice(statuses)))
                    await asyncio.sleep(5)
                    continue
    except:
        pass

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Rainbow bot".format(ctx.message.server.name), description="Készítette: FightMan01", color=0x00ff00, timestamp=ctx.message.timestamp)
    await client.say(embed=embed)

client.run("NjEyNjA3MjI3OTk1NDg4MjU2.XVk0_A.5MeSjfMD4r-yFha6CVe74ONYNQQ")
