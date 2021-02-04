import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
from config import setting


bot = commands.Bot(command_prefix=setting['prefix'])


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('Фото на рабочий стол с водопадами'):
        print('[command]: photo с водопадами')
        await message.channel.send('ссылка')


@bot.command(pass_context=True)
async def alive(ctx):
    author = ctx.message.author
    await ctx.send(f'Пивом запивали!, {author.mention}!')


bot.run(setting['token'])
