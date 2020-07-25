#Importok...
import discord
import asyncio
from discord.ext import commands
import datetime
import threading
import json
import random

#Alap dolgok....
client = commands.Bot(command_prefix=".")
client.remove_command('help')

#Adatbázis betöltése
with open("szinek.json") as f:
    szinek = json.load(f)

@client.event
async def on_ready():
    #Játék beállítása
    jatek = discord.Game("Rainbow bot By.: FightMan01")
    await client.change_presence(activity=jatek)
    print("[INFO] ~> Szerverek betöltése...")
    #For ciklus a szálak indítására
    for x in szinek:
        print(f"[INFO] ~> {x} regisztrálva!")
        #Szál készítése a szervernek
        th = threading.Thread(target = lambda: színváltó(x))
        #Szál elindítása
        th.start()
        #Állapot beállítása
        szinek[x]["fuss"] = True
    print("[INFO] ~> Szerverek betöltve, színváltás elindul!")

def színváltó(guildid):
    #Egy kis "hack" az asynchronous folyamat futtatására (a threading natívan nem támogatja)
    #Új loop készítése a szálnak.
    loop = asyncio.new_event_loop()
    #Színváltás futtatása ebben a loopban.
    loop.run_until_complete(rain(guildid))

async def rain(guildid):
    #Egy while loop
    while True:
        try:
            #A threadnek nincs leállító parancsa, azért ezt ilyen módon lehet kiküszöbölni.
            #Ez általában KeyError lesz a delete miatt, de ritka esetben ennek az eredménye lehet False is. 
            #Ezért alakalmaztam ezt a megoldást.
            if szinek[str(guildid)]["fuss"] == True:
                try:
                    #Itt már az előző verziókból ismert dolgok.
                    #Először a "színsorsoló". Ez választ egy színt.
                    colours = random.randint(0, 0xFFFFFF)
                    #Guild object lekérése
                    guild = client.get_guild(int(guildid))
                    #Rang ID lekérése
                    rangid = szinek[str(guildid)]["id"]
                    #Role object lekérése
                    role = discord.utils.get(guild.roles, id=int(rangid))
                    #A bothoz köthető asynchronous dolgok csak a fő loopban tudnak futni.
                    #Ezért így kell lehívnunk a rang szerkesztése dolgot.
                    client.loop.create_task(role.edit(colour=discord.Colour(colours), reason="Rainbow bot by: FightMan01"))
                    #5 másodperc várakozás (alacsonyabbra nem érdemes rakni!)
                    await asyncio.sleep(5)
                except:
                    #Hiba esetén (no perms stb...) is várunk 5 másodpercet, ezt sem érdemes kisebbre rakni.
                    await asyncio.sleep(5)
                    #A ciklus folytatása
                    continue
            else:
                break
        except:
            break

#Beállító parancs (alapból: .rainbow [be/ki] [rang])
@client.command()
async def rainbow(ctx, state, *, role:discord.Role=None):
    if ctx.author.bot:
        return
    #Az állapotát érdemes kisbetűssé konvertálni.
    state = state.lower()
    #Egy kis "wrapper", hogy angolul is meg lehessen adni.
    if state == "on":
        state = "be"
    if state == "off":
        state = "ki"
    #Ellenőrizzük, hogy nem adtak-e meg hülyeséget.
    if not (state == "be" or state == "ki"):
        return await ctx.send(":x: A beállítás csak `be` és `ki` lehet.")
    if state == "be":
        #Ha bekapcsolni szeretnénk...
        if not role:
            #Ha nincs rang megadva, adjunk vissza hibát.
            return await ctx.send(":x: Kérlek add meg a rangot!\nHasználat: **.rainbow [be/ki] [@rang]**")
        #Adatbázis előkészítése, adatok rögzítése
        szinek[str(ctx.guild.id)] = {}
        szinek[str(ctx.guild.id)]["id"] = str(role.id)
        szinek[str(ctx.guild.id)]["fuss"] = True
        #Szál készítése ennek a szervernek is...
        th = threading.Thread(target = lambda: színváltó(str(ctx.guild.id)))
        #Szál elindítása
        th.start()
        await ctx.send(":white_check_mark: A színváltás elkezdődött!")
    else:
        #Egyéb esetben (ki)...
        #Folyamat megszakítása (ha éppen most akarna színt váltani)
        szinek[str(ctx.guild.id)]["fuss"] = False
        #Szerver törlése az adatbázisból.
        del szinek[str(ctx.guild.id)]
        await ctx.send(":white_check_mark: Sikeres törlés!")
    #A változtatások fájlba írása.
    with open("szinek.json", "w") as f2:
        json.dump(szinek, f2)

client.run("TOKEN")
