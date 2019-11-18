from discord import Game
import aiohttp
import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord.utils import find
import datetime

client = commands.Bot(command_prefix=".")
Client = discord.Client()
client.remove_command('help')

@client.event
async def on_ready():
    jatek = discord.Game("Rainbow bot By.: FightMan01")
    await client.change_presence(activity=jatek)
    try:
        #Adatok bekérése
        rangid = "rang id-ja"
        szerverid = "szerver id-ja"
        #Szerver lekérése
        server2 = client.get_guild(id=int(szerverid))
        while True:
            #Rang lekérése
            role = discord.utils.get(server2.roles, id=int(rangid))
            try:
                #Rang frissítő rendszer
                colours = random.randint(0, 0xFFFFFF)
                await role.edit(colour=discord.Colour(colours), reason="Rainbow bot by: FightMan01")
                #5 másodperc várakozás. Lehet nagyobbra is rakni, de kisebbre nem érdemes, mert a bot API bant kaphat.
                await asyncio.sleep(5)
                #Rendszer vége, ez alatt a hiba kezelő rendszer van.
            except Exception as e:
                #Hiba kiiratása
                print(f"Hiba történt: {e}")
                #Itt is 5 másodperc várakozás, hogy hiba esetén se ugorjon egyből vissza, mert API bant kaphat a bot.
                await asyncio.sleep(5)
                #Egyszerűen csak folytatódik a rendszer.
                continue
    except:
        pass

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Rainbow bot", description="Készítette: FightMan01", color=0x00ff00, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

client.run("TOKEN")
