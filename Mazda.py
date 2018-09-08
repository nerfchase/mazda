import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "=")

@client.event 
async def on_ready():
    print("Ey boss, Mazda is good to go!")

@client.command()
async def ping(ctx):
    """ Pings the bot """
    await ctx.send(f'{ctx.author.mention} Pong! :ping_pong:')



chat_filter = ["NIGGER", "NIGGA", "MOIST", "CUNT", "CHINK", "BEANER", "FORTNITE", "NIGGERS", "NIGGAS", "CUNTS", "CHINKS", "BEANERS"]
bypass_list = []

@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} that is a naughty word!')
                except discord.errors.NotFound:
                    return
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='User')
    await member.add_roles(role)

@client.event
async def on_reaction_add(reaction, user):
    pass
    
        
client.run("NDU3NTk4NjgyODgwMDE2Mzk1.Dgb1wQ.cFFVJiOuangBMWLsycaOY_6CIGE")
