import os
# Import discord library
import discord
import os

# Create instance of a client
client = discord.Client()

# Use client to register an event (on ready event)
@client.event
# event is created when the bot is ready to use
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
# event is created on recieving a message 
async def on_message(message):
  #if the message is from the user
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$help'):
    await message.channel.send('How can I help you')

# To run the bot
client.run(os.environ['TOKEN'])
