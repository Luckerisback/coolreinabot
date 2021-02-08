import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
from config import setting


bot = commands.Bot(command_prefix=setting['prefix'])


@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.Ban(user)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('Reina is cute?'):
        await message.channel.send('Cute Reina!')
    if message.content.startswith('Say something to original Reina'):
        await  message.channel.send("I'm prettier then you! ")


@bot.command(pass_context=True)
async def alive(ctx):
    author = ctx.message.author
    await ctx.send(f'Пивом запивали!, {author.mention}!')


@bot.command(pass_context=True)
async def create_role(ctx):
    name_role = ' '.join(ctx.message.content.split(' ')[1:])
    server = ctx.message.server
    new_role = await bot.create.role(server)
    await bot.edite_role(server, new_role, name=name_role)


bot.run(setting['token'])
