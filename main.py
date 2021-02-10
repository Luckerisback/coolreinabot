import discord
from discord.ext import commands
from discord.ext.commands import Bot
from config import setting
from discord.utils import get
import generator
from generator import generate_sentence
from generator import train
from generator import gen_line
from generator import gen_tokens
from generator import gen_trigrams
from generator import unirand


bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await user.ban


@bot.command(pass_context=True)
async def on_zadornov(message):
    model = train(r'zadornov.txt')
    await message.channel.send(generate_sentence(model)),
       

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('Reina is cute?'):
        await message.channel.send('Cute Reina!')
    if message.content.startswith('Say something to original Reina'):
        model = train(r'zadornov.txt')
        await message.channel.send(generate_sentence(model))


@bot.command(pass_context=True)
async def alive(ctx):
    author = ctx.message.author
    await ctx.send(f'Пивом запивали!, {author.mention}!')


@bot.command(pass_context=True)
async def add_role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role) 
  
   
@bot.command(pass_context=True)
async def create_role(ctx):
    name_role = ' '.join(ctx.message.content.split(' ')[1:])
    guild = ctx.guild
    await guild.create_role(name=name_role)


bot.run(setting['token'])