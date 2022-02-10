import discord
from discord.ext import commands,tasks
import os
import requests
import urllib
import json
import youtube_dl
from keep_alive import keep_alive
from googleapi import google
from googlesearch import search
client=discord.Client()
my_secret = os.environ['token']
API_KEY = os.environ['token2']
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
sad_words=["sad","depressed","dukh","dard","pain","angry","annoyed","pissed","peeda"]

@client.event
async def on_message(message):
  msg=message.content
  if message.content.startswith('!test'):
    await message.channel.send('WE HAVE LIFTOFF')
  if any(word in msg for word in sad_words):
    data = requests.get('https://meme-api.herokuapp.com/gimme')
    json_data=json.loads(data.text)
    meme=json_data["preview"][1]
    await message.channel.send(meme)
  if 'yajush' in msg:
    await message.channel.send('https://cdn.discordapp.com/attachments/941091409509896283/941091918270562404/IMG_0124_jpg.JPG')
  if 'shobhit' in msg:
    await message.channel.send('https://cdn.discordapp.com/attachments/691757212925952101/941093511166574703/profile_picture.jpg')
  if 'harsh' in msg:
    await message.channel.send('https://cdn.discordapp.com/attachments/699548119448420374/941093328240390235/IMG_20220202_162307_648.jpg')
  if 'shiv' in msg:
    await message.channel.send('https://cdn.discordapp.com/attachments/834075135056805950/941096742944927764/IMG_20220128_025326_637.jpg')
  if 'what is' in msg:
    spl_word = 'what is'
    res = 'what is ' + msg.partition(spl_word)[2]
    for j in search(res, num=3, stop=3, pause=2):
        await message.channel.send(j)
        print(j)
  if message.content.startswith('!weather'):
    spl_word = '!weather'
    CITY =msg.partition(spl_word)[2]
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    data = response.json()
    damn = data['main']
    print(data)
    temperature = damn['temp']
    humidity = damn['humidity']
    pressure = damn['pressure']
    report = data['weather']
    await message.channel.send(f"{CITY:-^30}")
    await message.channel.send(f"Temperature: {round(temperature-273.15,2)}")
    await message.channel.send(f"Humidity: {humidity}")
    await message.channel.send(f"Pressure: {pressure}")
    await message.channel.send(f"Weather Report: {report[0]['description']}")
    

@client.event
async def on_ready():
  print("Logged in as {0.user}.format(client)")

keep_alive()
client.run(my_secret)
