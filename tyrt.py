import discord
from discord.ext import commands
import random


client = commands.Bot( command_prefix= '!')



@client.event
async def on_ready():
    print('Бот запустился')




@client.event
async def on_message(message):
    channel = client.get_channel(739229743412674724)
    msg = await client.wait_for('message')
    response = (msg.content)
    await channel.send(response)



    
client.run("ODEzNTA3Nzk3MDkzOTc0MDM2.YDQULQ.CS6kYTuwB7mHqGsunCAi62JTqxc")