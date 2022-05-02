import random
from keepalive import keepalive
import discord

journal_link = 'https://docs.google.com/document/d/174f4fFTwMTyGx-PiXQkqHwnFD_XFHyGkJMGAisLy_MI/edit'
takeshi_journal_link = 'https://docs.google.com/document/d/1kOTNzkU0G5joaz-TQK8V8623Qk3pQ9zTdNicgMKQNGs/edit'
reference_link = 'https://docs.google.com/document/d/1KE4VNmGDQJ3zAJiXoZuOS08734y73rDb6NEb-77sRyY/edit'
facts = ["The land of Ginru is lush and vast!",
         "Jin kinda smells like wet dog",
         "Ryuujin are said to watch over travelers",
         "The church of the Snail claims the world is a big snail",
         "Buying something abundant in one town and selling it where its rare is sure to net a profit",
         "You'd need to eat around 400 bananas for them to kill you with potassium poisoning",
         "Moru is technologically advanced, they even have self moving carriages!",
         "Sometimes the journey is better than the destination"]
client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!Kodama hello'):
        await message.channel.send('Hello {}!'.format(message.author.nick))
    if message.content.startswith('!Kodama journal'):
        await message.channel.send(f'Hiya the link to the journal is here {journal_link}')
    if message.content.startswith('!Kodama Takeshi journal'):
        await message.channel.send(f"Hiya here is the journal of Takeshi {takeshi_journal_link}")
    if message.content.startswith('!Kodama reference'):
        await message.channel.send(f"Hiya here is the reference sheet for Ryuutama {reference_link}")
    if "meow" or "Meow" in message.content:
        await message.channel.send("Meow!")
    if message.content.startswith("!Kodama fact"):
        await message.channel.send(facts[random.randint(0, len(facts)-1)])

keepalive()
client.run('TOKEN')