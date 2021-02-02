import discord
import os
from discord.ext import commands
from config import setting


bot = commands.Bot(command_prefix=setting['prefix'])


@bot.command(pass_context=True)
async def елимясомужики(ctx):
    author = ctx.message.author

    await ctx.send(f'Пивом запивали!, {author.mention}!')


bot.run(setting['token'])
