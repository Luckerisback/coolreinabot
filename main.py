import discord
import os
from discord.ext import commands
from config import setting


bot = commands.Bot(command_prefix=setting['prefix'])


@bot.command(pass_context=True)
async def елимясомужики(ctx):
    author = ctx.message.author

    await ctx.send(f'Пивом запивали!, {author.mention}!')
    
    
@bot.command(pass_context=True)
async def image(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(colour=0xff9900, title='Random pictures')
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)

bot.run(setting['token'])
