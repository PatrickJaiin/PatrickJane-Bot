import discord
from discord.ext import commands, tasks
import os
import requests
import urllib
import json
import youtube_dl
import datetime
from datetime import date, timedelta
from keep_alive import keep_alive
from googleapi import google
from googlesearch import search
from geopy.geocoders import Nominatim

client = discord.Client()
my_secret = os.environ['token']
API_KEY = os.environ['token2']
nasa_key = os.environ['nasa']
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
sad_words = [
    "sad", "depressed", "dukh", "dard", "pain", "angry", "annoyed", "pissed",
    "peeda"
]


@client.event
async def on_message(message):
    msg = message.content
    if message.content.startswith('!test'):
        await message.channel.send('WE HAVE LIFTOFF')
    if message.content.startswith('!help'):
        await message.channel.send('!weather cityyname')
        await message.channel.send('what is and question')

    if message.content.startswith('!setup'):
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/834075135056805950/940975384499990538/20220209_194955.jpg'
        )
    if message.content.startswith('!nasa'):
        nasalink = "https://api.nasa.gov/planetary/apod?api_key={}".format(
            nasa_key)
        responsenasa1 = requests.get(nasalink)
        datanasa1 = responsenasa1.json()
        await message.channel.send(datanasa1['url'])
        await message.channel.send(datanasa1['copyright'])
        await message.channel.send(datanasa1['explanation'])
    if message.content.startswith('!photo'):
        today = date.today()
        temp = today.replace(day=1) - timedelta(days=1)
        loc = Nominatim(user_agent="GetLoc")
        word = "!photo"
        city = msg.partition(word)[2]
        print(city)
        getLoc = loc.geocode(city)
        print(getLoc.address)
        lat = getLoc.latitude
        long = getLoc.longitude
        link = "https://api.nasa.gov/planetary/earth/assets?lon={}&lat={}&date=2021-01-10&&dim=0.1&api_key={}".format(
            long, lat, nasa_key)
        responsenasa = requests.get(link)
        datanasa = responsenasa.json()
        x = datanasa["url"]
        await message.channel.send(x)

    if any(word in msg for word in sad_words):
        data = requests.get('https://meme-api.herokuapp.com/gimme')
        json_data = json.loads(data.text)
        meme = json_data["preview"][1]
        await message.channel.send(meme)

    if 'vansh' and 'shiv' and 'nandini' and 'virat' in msg:
        await message.channel.send(
            'https://cdn.discordapp.com/attachments/817265444343906325/945024002949279774/WhatsApp_Image_2022-02-20_at_11.57.07_PM.jpeg'
        )
    else:
        if 'yajush' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/941091409509896283/941091918270562404/IMG_0124_jpg.JPG'
            )
        if 'shobhit' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/691757212925952101/941093511166574703/profile_picture.jpg'
            )
        if 'harsh' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/699548119448420374/941093328240390235/IMG_20220202_162307_648.jpg'
            )
        if 'shiv' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/834075135056805950/941096742944927764/IMG_20220128_025326_637.jpg'
            )
        if 'axshita' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/914470973099638814/993943703091675166/IMG-20220601-WA0148_Original.jpg'
            )
        if 'aravind' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/547833581456850954/941230860710051882/20220209_183037.jpg'
            )
        if 'surya' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/780430546874138640/941140499207708682/PXL_20210606_052638243.MP.jpg'
            )
        if 'kartik' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/498129314533867521/941249295103967272/Kartik_Anand_picture.jpg'
            )
        if 'aryan' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/770700178604425247/941250039320285215/C6B1A97E-A4A2-4D64-B44C-9F6AC19F72EA.jpg'
            )
        if 'manas' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/935614841668894820/941254383604236288/236376357_438696470614610_7176962335888262977_n.jpg'
            )
        if 'virat' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/830389609800269834/941256430160338964/54f63115-df31-42ee-9ab3-7724081126d4.png'
            )
        if 'aadit' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/861501982254039070/941259852284592128/Snapchat-717566903.jpg'
            )
        if 'arindam' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/690881018386841681/941283167149625364/20220210-0001.jpg'
            )
        if 'kshitiz' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/846000599140925470/941315850265329675/IMG_20190721_130929_097.jpg'
            )
        if 'shellss' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/940971808750972928/941321343301980190/IMG_20220210_184447.jpg'
            )
        if 'rishit' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/734433806899085414/941328974418686022/1234.jpg'
            )
        if 'nandini' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/817265444343906325/941371420481552394/EE6A7951-09BA-4EE7-8E05-68932B7C2F4E.jpg'
            )
        if 'pewpew' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/914470973099638814/993948867785674762/332497BD-9C79-4CE5-B56D-7A4393C0842A.jpg'
            )
        if 'vansh' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/817265444343906325/945024003184148590/WhatsApp_Image_2022-02-20_at_11.55.43_PM.jpeg'
            )
        if 'chaiitanyaa' in msg:
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/776765031449624586/945210710080757791/WhatsApp_Image_2022-02-21_at_12.19.39_PM.jpeg'
            )
    if 'what is' in msg:
        spl_word = 'what is'
        res = 'what is ' + msg.partition(spl_word)[2]
        for j in search(res, num=3, stop=3, pause=2):
            await message.channel.send(j)
            print(j)
    if message.content.startswith('!weather'):
        spl_word = '!weather'
        CITY = msg.partition(spl_word)[2]
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        response = requests.get(URL)
        data = response.json()
        print(data)
        damn = data['main']
        print(data)
        temperature = damn['temp']
        humidity = damn['humidity']
        pressure = damn['pressure']
        report = data['weather']
        await message.channel.send(f"{CITY:-^30}")
        await message.channel.send(f"Temperature: {round(temperature-273.15)}")
        await message.channel.send(f"Humidity: {humidity}")
        await message.channel.send(f"Pressure: {pressure}")
        await message.channel.send(
            f"Weather Report: {report[0]['description']}")


@client.event
async def on_ready():
    print("Logged in as {0.user}.format(client)")


keep_alive()
client.run(my_secret)
