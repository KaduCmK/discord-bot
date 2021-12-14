
import discord
from discord import FFmpegPCMAudio
from discord import client
from discord.ext import commands
from youtube_dl import YoutubeDL
import requests
from random import randint

token = 'OTIwMTUxMDE3ODY0MTgzODM4.YbgLag.S4sQcZuFbqVsTDE9i5bPshTVzRw'
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Logado como {0.user}'.format(client))


# gerenciamento de musica
# ===============================================================================================
def search(query):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        try:
            requests.get(query)
        except:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        else:
            info = ydl.extract_info(query, download=False)
    return (info, info['formats'][0]['url'])


@client.command()
async def brota(ctx):
    member_voice = ctx.author.voice.channel
    await member_voice.connect()


@client.command()
async def toca(ctx, *, query):
    member_voice = ctx.author.voice
    await ctx.send('Carregando...')
    if member_voice and member_voice.channel:
        if ctx.voice_client:
            client_voice = ctx.voice_client
            video, source = search(query)
            await ctx.send(f"Tocando: {video['title']}")
            client_voice.play(FFmpegPCMAudio(source))
            client_voice.is_playing()
        else:
            await member_voice.channel.connect()
            client_voice = ctx.voice_client
            video, source = search(query)
            await ctx.send(f"Tocando: {video['title']}")
            client_voice.play(FFmpegPCMAudio(source))
            client_voice.is_playing()


@client.command()
async def pausa(ctx):
    await ctx.voice_client.pause()
    await ctx.send('pausado')

@client.command()
async def continua(ctx):
    await ctx.voice_cliente.resume()
    await ctx.send('resumindo')

# ===============================================================================================


# Responder mensagens
# ===============================================================================================
@client.event
async def on_message(message):
    usuario = str(message.author).split('#')[0]
    mensagem = str(message.content)
    canal = str(message.channel.name)
    print(f'{usuario}: {mensagem} ({canal})')

    if message.author == client.user:
        return

    if mensagem.lower() == 'pode isso arnaldo?':
        await message.channel.send('a regra é clara, não pode')
        return

    if mensagem.lower() == 'galvão?':
        await message.channel.send('diga lá Tino!')
        return
    
    if mensagem.lower() == 'filho da puta':
        await message.channel.send('meu pau que te cutuca')
        return

    if mensagem.lower() == '!leyzin' or mensagem.lower() == '!ferpo' or mensagem.lower() == '!ferpon':
        await message.channel.send('meu rei')
        return

    if mensagem.lower() == '!angelo' or mensagem.lower() == '!kocta':
        await message.channel.send('MACETAVA')
        return

    if mensagem.lower() == '!edu' or mensagem.lower() == '!obee':
        await message.channel.send('meu führer')
        return

    if mensagem.startswith('!limpar'):
        qtd = int(mensagem.split(' ')[1])
        await message.channel.purge(limit=qtd+1)
        return
    
    await client.process_commands(message)
# ===============================================================================================


client.run(token)