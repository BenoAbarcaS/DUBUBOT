from discord.ext import commands
from bs4 import BeautifulSoup
from discord import Embed
import requests
import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$',intents=intents)

userID01=1
userID02=2
token=3

@client.event
async def on_ready():
    print(f'Logeado bot {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('apex'):
        await message.channel.send('https://i.imgur.com/dBMk7fv.png')

    if message.content.lower().startswith('hola'):
        await message.channel.send('Pa mi tu cola https://tenor.com/view/clash-royale-gif-5535732')

    if message.author.id == userID02:
        randnumber = random.randrange(100)
        if randnumber < 1:
            await message.channel.send('https://cdn.discordapp.com/attachments/689228011119050812/1021824061413806120/calla-boca-shorts.mp4')
        if randnumber > 1 and randnumber < 4:
            await message.channel.send('https://cdn.discordapp.com/attachments/689228011119050812/1015517281322799155/unknown.png')

    if message.author.id == userID01:
        if message.content.lower().startswith('$dns'):
            embed = discord.Embed(title="Viernes de limpiar Cache", description="@everyone Recordatorio de limpiar el cache de los dominios. El codigo a insertar en consola es: ipconfig /flushdns")
            embed.set_author(name='DUBUBOT',  icon_url='https://i.imgur.com/ddWxFA5.jpg')
            embed.set_image(url='https://i.imgur.com/nc5OHqc.gif')
            embed.set_thumbnail(url="https://i.imgur.com/gpYFrW5.gif")
            embed.set_footer(text='DUBUBOT',icon_url='https://i.imgur.com/ddWxFA5.jpg')
            await message.channel.send(embed=embed)
    
    if message.content.lower().startswith('$dubu'):
        num = str(random.randrange(264))
        file = discord.File('./dahyun/a (' + num + ').jpg', filename='' + num + ').jpg')
        await message.channel.send(file=file)

    if message.content.lower().startswith('$mal'):    
        num = str(random.randrange(52619))         
        await message.channel.send('Tendras que ver: https://myanimelist.net/anime/' + num)

    if message.content.lower().startswith('$apex'): 
        url="https://apexlegendsstatus.com/current-map"  
        html_text=requests.get(url).text
        soup = BeautifulSoup(html_text,'html.parser')
        maparanked = soup.find(class_ = 'col-lg-8 brranked').text.strip()
        if (maparanked.startswith('Battle Royale: Broken Moon')):
            fileranked = discord.File('./multimedia/apex/brokeenmoon1701.png', filename='brokeenmoon1701.png')
        mapacasual2 = soup.find(class_ = 'col-lg-8 olympus').text.strip()
        if (mapacasual2.startswith('Battle Royale: Broken Moon')):
            file = discord.File('./multimedia/apex/casualbrokenmoon.png', filename='casualbrokenmoon.png')
        elif (mapacasual2.startswith('Battle Royale: Olympus')):
            file = discord.File('./multimedia/apex/casualolympus.png', filename='casualolympus.png')
        elif (mapacasual2.startswith("Battle Royale: World's Edge")):
            file = discord.File('./multimedia/apex/casualworldedge.png', filename='casualworldedge.png')
        await message.channel.send(file=file)
        await message.channel.send(file=fileranked)

client.run(token)