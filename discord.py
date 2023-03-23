import discord
from discord.ext import commands
from gd import *
import asyncio

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def level(ctx, *, query):
    async with ctx.typing():
        gd_client = Client()
        try:
            level = await gd_client.search_levels(query)
            if level:
                embed = discord.Embed(title=level.name, description=level.description)
                embed.add_field(name='ID', value=level.id, inline=False)
                embed.add_field(name='Author', value=level.author.name, inline=True)
                embed.add_field(name='Downloads', value=level.downloads, inline=True)
                embed.add_field(name='Likes', value=level.likes, inline=True)
                embed.set_image(url=level.thumbnail)
                await ctx.send(embed=embed)
            else:
                await ctx.send('No se encontró el nivel.')
        except Exception as e:
            await ctx.send(f'Ocurrió un error: {e}')

client.run('DISCORD_TOKEN')
