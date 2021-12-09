from decouple import config
from discord.ext import commands
import metodos



bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f"{bot.user.name} logged")

@bot.command()
async def add(ctx, arg):
    metodos.add_members(ctx.message.mentions)
    await send(ctx.channel, content = metodos.show_list("Grupo", metodos.group(ctx.guild.id)))

@bot.command()
async def remove(ctx, arg):
    metodos.remove_members(ctx.message.mentions)
    await send(ctx.channel, content = metodos.show_list("Grupo", metodos.group(ctx.guild.id)))        

@bot.command()
async def group(ctx):
    await send(ctx.channel, metodos.show_list("Grupo", metodos.group(ctx.guild.id)))

@bot.command(name = "remove-all")
async def remove_all(ctx):
    metodos.remove_all(ctx.guild.id)
    await send(ctx.channel, metodos.show_list("Grupo", metodos.group(ctx.guild.id)))        

@bot.command()
async def randomize(ctx):  
    await send(ctx.channel, metodos.randomize(ctx.guild.id))


async def send(channel, content):
    await channel.send(content = content)


bot.run(config('DISCORD_TOKEN'))