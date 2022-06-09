from discord.ext import commands
import os
import discord

command_prefix = '<'
bot = commands.Bot(command_prefix = command_prefix)
@bot.event
async def on_ready():
    print('son gay')
#thêm process_commands 
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await bot.process_commands(message)

#chỗ này bình thường 
@bot.command()
async def batchedobaylen(ctx):
  await ctx.send('dabat')      
@bot.command()
async def nothing(ctx):
  await ctx.send('nothing happend  yet')
@bot.command()
async def noigidi(ctx):
  await ctx.send('anh thạch đẹp zai')
  
@bot.command()
async def hungdepzai(ctx):
  await ctx.send(file=discord.File("hungngau.jpg"))

'''import thư viện os để dùng biến môi trường (nếu up lên repo github mà không để token riêng thì sẽ bị reset)'''
bot.run(os.getenv('bot_token'))
