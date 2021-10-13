import os
import discord
import requests



client = discord.Client()
api_url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
    'x-rapidapi-key': "666a00f4c3msh6efa5ebe0b5b296p1ed7bajsned0fb1c344f7",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }
def get_quote():

  response = requests.request("GET", api_url, headers)

  
  return response.text


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$hello"):
    await message.channel.send(get_quote())






client.run(os.environ['Token'])