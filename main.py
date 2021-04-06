import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client=discord.Client()

def currency(unit):
  response=requests.get('http://data.fixer.io/api/latest?cbase=USD&access_key=35a3ad0f2f253d37131b68cd1b5953fc&&symbols=USD,TRY')
  json_data=json.loads(response.text)
  tr=float(json_data['rates']['TRY'])
  if(unit=="euro"):
    return tr
  usd=float(json_data['rates']['USD'])
  currency=tr/usd
  currency=round(currency,6)
  return "Yarım dolar :"+str(currency/2)

def coinflip():
  flip=random.randint(1,100)
  if(flip==50):
    return "Dik Geldi :D"
  elif(flip>50):
    return "tura"
  else:
    return "yazı"
def genRand(mess):
  x=mess.split(' ',1)
  range=int(x[1])
  return random.randint(0,range)

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
    await message.channel.send("Commands : \n > !sa\n > !dolar\n > !euro \n > !coinflip [ Yazı-%49,5 | Tura-%49,5 | Dik-%1 ] \n > !random sayıgir [örnek komut: '!random 100']")
  if message.content.startswith('!coinflip'):
    await message.channel.send(coinflip())
  if message.content.startswith('!random'):
    mess=str(message.content)
    await message.channel.send(genRand(mess))
keep_alive()
client.run(os.getenv('TOKEN'))