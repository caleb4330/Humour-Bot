import os
import discord
import requests
import json 

client = discord.Client()
api_url = "https://dad-jokes.p.rapidapi.com/random/joke"


def get_joke():
  url = "https://icanhazdadjoke.com"
  headers = {"Accept": "application/json"}
  response = requests.get(url,headers = headers)
  parsed_data = json.loads(response.text)

  joke = parsed_data['joke']

  
  return joke


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$Tell me a joke"):
    await message.channel.send(get_joke())






client.run(os.environ['Token'])