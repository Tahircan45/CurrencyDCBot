import discord
import os
import requests
import json

client=discord.Client()

def currency(unit):
  response=requests.get('http://data.fixer.io/api/latest?cbase=USD&access_key=35a3ad0f2f253d37131b68cd1b5953fc&&symbols=USD,TRY')
  json_data=json.loads(response.text)
  tr=float(json_data['rates']['TRY'])
  if(unit=="euro"):
    return tr
  usd=float(json_data['rates']['USD'])
  currency=tr/usd
  print(currency)
  currency=round(currency,6)
  return currency

@client.event
async def on_ready():
  print('Logged {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user :
    return
  if message.content.startswith('!sa'):
    await message.channel.send('Ve Aleyna Aleyküm Selam Mümin Kardeşim! ' + str(message.author.mention))
  if message.content.startswith('!dolar'):
    await message.channel.send(currency("dolar"))
  if message.content.startswith('!euro'):
    await message.channel.send(currency("euro"))
  if message.content.startswith('!commands'):
    await message.channel.send("Commands : \n > !sa\n > !dolar\n > !euro ")
client.run(os.getenv('TOKEN'))