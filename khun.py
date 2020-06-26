import discord
import random

from discord import Member as DiscordMember
from discord.ext import commands

bot = commands.Bot(command_prefix = "khun ")

@bot.event
async def on_ready():
  await bot.change_presence(status = discord.Status.idle, activity = discord.Game("You will meet your doom"))
  print("Bot is ready.")

@bot.event
async def on_member_join(member):
  print(f"{member} has joined the server!")

@bot.event
async def on_member_remove(member):
  print(f"{member} has left the server. :(")

@bot.command(aliases=["commands"])
async def helpcommand(ctx):
  await ctx.send(f"This is a bot based on the Korean webtoon series **'Tower of God 신의탑'** written by SIU! This bot is run by **Khun A.A.** and his lighthouses. Enter the commands to send a request to access and communicate through the database.\n\n__Here are some commands that you can try:__\n`khun ping` - replies with bot latency\n`khun askguide` - ask a guide about your path (8ball)\n`khun slap @mentionuser` - serve a mighty old whack around the cheeks\n`khun kiss @mentionuser` - show some love by plopping your coronavirus + hot sauce covered lips on someone's face\n`khun hug @mentionuser` - nothing beats a warm embrace\n`khun coinflip` - some things are too difficult to decide\n`khun bubblewrap` - need some stres relief? look no further")

@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")
  await ctx.send(f"`{round(bot.latency * 1000)}ms`")

@bot.command(aliases=["askguide", "8ball"])
async def _8ball(ctx, *,question):
  guides = ["Hwaryun","Evan","the FUG Elders"]
  responses = ["100%","Just google it.","I'm not a shaman, get lost.",'You can count on it.',"Go for it!","I can't tell.","Sure.","Do whatever you want with your life.","Give me some money first.","I don't think that's a good idea","It will be difficult","Pray for a miracle","Believe in yourself"]
  await ctx.send(f"Now asking {random.choice(guides)}...\nQuestion: {question}\nAnswer: {random.choice(responses)}")

@bot.command(aliases=["slap"])
async def slap_member(ctx,target: DiscordMember):
  slaps = ["out of the inner tower", "silly as rachel", "and the surrounding shinsu senseless","so hard that shockwaves were sent through the tower", "so hard that a shinsu black hole sphere was created", "so hard that the adminstrator had a seizure","square on the ass"]
  await ctx.send(f"**{ctx.author.display_name}** just slapped {target.mention} {random.choice(slaps)}!")

@bot.command(aliases=["kiss"])
async def kiss_member(ctx,target: DiscordMember):
  await ctx.send(f"**{ctx.author.display_name}** just pecked {target.mention} on the cheek! ~~no bromo~~")

@bot.command(aliases=["hug"])
async def hug_member(ctx,target: DiscordMember):
  hugs = ["a big warm hug!","a soft bear hug.","a tight embrace."]
  await ctx.send(f"**{ctx.author.display_name}** just gave {target.mention} {random.choice(hugs)}")

@bot.command()
async def coinflip(ctx):
  comwords = ["Pick", "Choose", "Go for"]
  ab = ["heads","tails"]
  await ctx.send(f"{random.choice(comwords)} {random.choice(ab)}.")

@bot.command()
async def bubblewrap(ctx):
  await ctx.send(f"**Here is your virtual bubble wrap!**\n||pop||||POP||||pop||||POP||||pop||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||pop||||POP||||pop||||POP||||pop||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||||POP||||pop||")

@bot.command(aliases=["purge"])
async def clear(ctx,amount=10):
  await ctx.channel.purge(limit=amount)

@bot.command(aliases=["purgeall"])
async def clearall(ctx,amount=all):
  await ctx.channel.purge()

bot.run("Njk3NTIyMzk5MDU0MjY2Mzc5.Xo4gaA.9EGUtGXUrb_slzEZBHZgzbkJgBI")