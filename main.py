import discord
import os
import requests
import json 
import random


client=discord.Client()
laugh=['cheer','laugh','make me happy','uplift my mood']
custom_jokes=['Q: What happened to the guy who sued over his missing luggage?\nA: He lost his case.','What’s the difference between a  poorly dressed man on a unicycle and a well-dressed man on a bicycle?\nAt-tire','My memory has gotten so bad it has actually caused me to lose my job. I’m still employed. I just can’t remember where.']


def get_chuck_jokes():
  #used the documentation to find these commands
  url = 'https://api.chucknorris.io/jokes/random'
  response = requests.get(url)
  json_data=json.loads(response.text)
  #print(response.text)
  jokes=json_data['value']
  # jokes=response.json()['contents']['jokes'][0]
  return jokes

def get_activity():
  url='http://www.boredapi.com/api/activity/'
  response = requests.get(url)
  json_data=json.loads(response.text)
  activity=json_data['activity']
  return activity


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  msg=message.content
  if msg.startswith("$hello"):
    await message.channel.send("HELLO!")

  if msg.startswith("$chuck_jokes"):
    joke=get_chuck_jokes()
    await message.channel.send(joke)
  
  if msg.startswith("$bored"):
    activity=get_activity()
    await message.channel.send(activity)
  
  if any(word in msg for word in laugh):
    await message.channel.send(random.choice(custom_jokes))
  

client.run(os.getenv('TOKEN'))
