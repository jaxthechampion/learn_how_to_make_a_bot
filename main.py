from discord.ext import commands
import os
import discord
intents = discord.Intents.default()
intents.members = True

command_prefix = '>>'
bot = commands.Bot(command_prefix = command_prefix, intents=intents)

guild = bot.get_guild("919793000777908335")
@bot.event
async def on_ready():
    print('bot da san sang')
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
  await ctx.send(file=discord.File("./files/hungngau.jpg"))
@bot.command()
async def vanmau(ctx):
  await ctx.send(file=discord.File("./files/van_tan_gai.rtf"))
@bot.command()
async def mypfp(ctx):
  await ctx.send(file=discord.File("./files/mypfp.png"))
@bot.command()
async def bvhocvahanh(ctx):
  await ctx.send(file=discord.File("./files/BAI_VAN_HOC_VA_HANH.docx"))
@bot.command()
async def bvtuoitredatnuoc(ctx):
  await ctx.send(file=discord.File("./files/BAI_VAN_TUOI_TRE_VA_TUONG_LAI_AT_NUOC.docx"))
@bot.command(name='list')
async def _list(ctx, arg):
    pass

@commands.command()
async def upf(ctx, *stuff):
  msg  = ctx.message
  if str(msg.attachments) == "[]":
    await ctx.send("Bạn chưa gửi file nào!")
  else:
    split_v1 = str(msg.attachments).split("filename='")[1]
    filename = str(split_v1).split("' ")[0]
    await msg.attachments[0].save(fp="./files/{}".format(filename))

@bot.command()
async def somem(ctx):
  await ctx.send(guild.member)

'''import thư viện os để dùng biến môi trường (nếu up lên repo github mà không để token riêng thì sẽ bị reseta)'''
bot.run(os.getenv('bot_token'))
