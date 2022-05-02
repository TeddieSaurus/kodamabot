import os
import random
from keepalive import keepalive
import discord
my_secret = os.environ['TOKEN']


journal_link = 'https://docs.google.com/document/d/174f4fFTwMTyGx-PiXQkqHwnFD_XFHyGkJMGAisLy_MI/edit'
takeshi_journal_link = 'https://docs.google.com/document/d/1kOTNzkU0G5joaz-TQK8V8623Qk3pQ9zTdNicgMKQNGs/edit'
reference_link = 'https://docs.google.com/document/d/1KE4VNmGDQJ3zAJiXoZuOS08734y73rDb6NEb-77sRyY/edit'

global facts

f = open("facts.txt", "r")
facts = f.readlines()
f.close()


client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    global facts
    msg_content = message.content.lower()
    print(message.author)
    print(message.author)
    if message.author == client.user:
        return
    if msg_content.startswith('!kodama hello'.lower()):
        await message.channel.send('Hello {}!'.format(message.author.name))
    if msg_content.startswith('!kodama journal'.lower()):
        await message.channel.send(f'Hiya the link to the journal is here {journal_link}')
    if msg_content.startswith('!kodama takeshi journal'.lower()):
        await message.channel.send(f"Hiya here is the journal of Takeshi {takeshi_journal_link}")
    if msg_content.startswith('!kodama reference'.lower()):
        await message.channel.send(f"Hiya here is the reference sheet for Ryuutama {reference_link}")
    if msg_content.startswith("!kodama fact".lower()):
        await message.channel.send(facts[random.randint(0, len(facts)-1)])
    if msg_content.startswith("!kodama add fact".lower()):
        with open("facts.txt", "a") as file:
            print(msg_content)
            file.write(msg_content[16:] + f" --Author: {message.author.name}" + "\n")
        with open("facts.txt", "r") as file:
            facts = file.readlines()
        await message.channel.send("Fact added!")


keepalive()
client.run(my_secret)
