import random
import time
from pathlib import Path

import discord
from discord.ext import commands


# gerenciamento de musica
# ===============================================================================================
class MusicBot(commands.Bot):
    def __init__(self):
        self._cogs = [p.stem for p in Path('.').glob('.bot/cogs/*.py')]
        super().__init__(
            command_prefix=self.prefix, 
            case_insensitive=True, 
            intents=discord.Intents.all()
            )


    def setup(self):
        print('configurando...')

        for cog in self._cogs:
            self.load_extension(f'bot.cogs.{cog}')
            print(f" `{cog}` cog carregado.")
    
        print('configuração concluída')

    def run(self):
        self.setup()

        with open('data/token.0', 'r', encoding='utf-8') as f:
            TOKEN = f.read()

        print('rodando bot...')
        super().run(TOKEN, reconnect=True)

    async def shutdown(self):
        print('encerrando conexão...')
        await super().close()

    async def close(self):
        print('Encerrando por input do teclado...')
        await self.shutdown()

    async def on_connect(self):
        print(f'Conectado ao discord (latência: {self.latency*1000:,.0f} ms)')
    
    async def on_resumed(self):
        print('bot resumido')

    async def on_disconnect(self):
        print('bot desconectado')
    
    async def on_ready(self):
        self.client_id = (await self.application_info()).id
        print('bot pronto')

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or('--')(bot, msg)

    async def process_commands(self, msg):
        ctx = await self.get_context(msg, cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

    async def on_message(self, msg):
        if not msg.author.bot:
            await self.process_commands(msg)
            

# ===============================================================================================


# utilitarios
# ===============================================================================================
'''
@client.command()   # comando p trocar o tema do servidor - uso: !trocartema [temas separados por virgula]
async def trocartema(ctx, *, temas):
    lista = temas.split(', ')
    await ctx.send('sorteando entre os temas:')

    for i in range(len(lista)):
        await ctx.send(lista[i])
        time.sleep(1)
    
    sort = random.randrange(len(lista))
    time.sleep(1)
    await ctx.send('---------------------------')
    await ctx.send('tema escolhido: ' + lista[sort])
'''
# ===============================================================================================



# Responder mensagens
# ===============================================================================================
'''
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

    if mensagem.lower() == 'eu sou cria?':
        if usuario == 'KaduCmK':
            await message.channel.send('esse dai é cria de vdd')
        else:
            await message.channel.send('nada a ver isso dai')
        return

    if mensagem.lower() == '!kasama' or mensagem.lower() == '!boludo':
        await message.channel.send('pega a visao')
        await message.channel.send(file=discord.File('kasama.png'))
        
    
    await client.process_commands(message)
'''
# ===============================================================================================
