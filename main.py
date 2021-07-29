#This bot was coded by AcidFilms#2911
import discord
import os
import keep_alive

from discord.ext import commands
from discord.ext import tasks

client = commands.Bot(command_prefix="-", case_insensitive=True)
client.remove_command("help")


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    change_status.start()
    await client.change_presence(activity=discord.Game(name='AddedMc | -help'))

@tasks.loop(seconds=10)
async def change_status():
  print("PingPong")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("This command doesn't exist! \nUse `-help` to see all commands.")

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! 🏓  | {round(client.latency * 1000)}ms')

@client.command()
async def ore(ctx):
    embed=discord.Embed(title="Thanks for submiting a ore!", description="Your ore will be reviewed soon.", color=0xFFFFFF)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/776502380556189706/870294540156801044/unknown.png")
    embed.set_footer(text=f"Ore submitted by {ctx.author.name}",
	icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

@client.command()
async def food(ctx):
    embed=discord.Embed(title="Thanks for submiting a food!", description="Your food will be reviewed soon.", color=0xFFFFFF)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/776502380556189706/870295000557158481/unknown.png?width=519&height=519")
    embed.set_footer(text=f"Food submitted by {ctx.author.name}",
	icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

@client.command()
async def devtools(ctx):
    yourID = 672498629864325140
    if ctx.message.author.id == yourID:
        embed=discord.Embed(title="Developer Infomation", description=f"`5` commands loaded and `0` cogs. \n I'm in {len(client.guilds)} servers!", color=0x2ecc71)
        embed.set_footer(text="Bot created by AcidFilms#2911")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="**Insufficient Permission**", description="You do **Not** have permission to run this command.", color=0x000000)
        embed.set_footer(text=f"Caused by {ctx.author.name}",
	icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@client.command()
async def help(ctx):
        embed=discord.Embed(title="AddedMC | Help", description="Here is all the command sin the AddedMC bot!.", color=0xFFFFFF)
        embed.add_field(name="Help", value="he command you just ran!")
        embed.add_field(name="Ore", value="To suggest a ore do `-ore {ore name}`.")
        embed.add_field(name="Food", value="To suggest a food do `-ore {food name}`.")
        embed.add_field(name="Ping", value="To find the ping of the bot.")
        embed.set_footer(text=f"Requested by {ctx.author.name}",
	    icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)



keep_alive.keep_alive()

client.run(os.getenv('TOKEN'))
