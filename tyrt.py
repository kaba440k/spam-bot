import discord
from discord.ext import commands
import random


client = commands.Bot( command_prefix= '!')



@client.event
async def on_ready():
    print('Бот запустился')




@client.event
async def on_message(message):
    channel = client.get_channel(#"id_channel")
    msg = await client.wait_for('message')
    response = (msg.content)
    await channel.send(response)



    
client.run(#"token")
