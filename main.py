import disnake
from disnake import *
from disnake.ext import commands
from disnake.ui import Select, View
import aiohttp
import os
import math
import random
from keys import *
# -- Importações necessárias ;-; (talvez) --
# -------------------------------------------------

# -- Variáveis --
 # Variavel para as coisas do Bot
bot = commands.Bot()

# -- Funções --
pass

# -- Dicionários --
pass

# -- Classes --
pass

# -- Código --
 # Evento do bot quando for iniciado
@bot.event
async def on_ready():
    # Var para saber quantos são os comandos sincronizados
    synced = len(bot.all_slash_commands)
    # Limpando o terminal
    os.system('cls')
    # Printando quanto foram sincronizados e uma mensagem bonitinha
    print(bars)
    print(f'{synced} comandos sincronizados! =)')
    print(f'Bom dia {bot.user.name}! Tudo certo por aqui até então.')
    print(bars)
    # Mudando o status e a atividade do bot
    await bot.change_presence(status = disnake.Status.online, activity = disnake.Game('Sendo refeita agora mesmo ;-;'))

 # Comandos gerais
  # Comando echo, para repetição da mensagemn escrita no canal de texto escolhido
    # Definindo nome e descrição; Pegando a interação, a mensagem e o canal, e se n escolher o canal, é None
@bot.slash_command(name = 'echo', description = 'Reenvia sua mensagem como se fosse eu dizendo! (Meio estranho até ;-;)')
async def echo(inter, message: str, channel: disnake.TextChannel = None):
    # Se o canal não for escolhido, = ao que o comando foi enviado, se foi, = ao escolhido
    channel = (inter.channel if channel == None else channel)
    # Mandando a mensagem escolhida no canal escolhido
    await channel.send(content = message)
    # Respondendo a mensagem inicial que deu tudo certo, mostrando apenas para quem enviou por causa do ephemeral
    await inter.response.send_message('Sua mensagem foi enviada com sucesso! =)', ephemeral = True)



 # Comandos para o RPG e personagens
pass

 # Rodando o bot a partir do token do discord
bot.run(token)