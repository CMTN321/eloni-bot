import disnake
from disnake import *
from disnake.ext import commands
from disnake.ui import Select, View
import aiohttp
import os
import math
import random
from keys import *
# -- Importações talvez necessárias ;-; --
# -------------------------------------------------

# -- Variáveis --
 # Var para os commandos do Bot
bot = commands.Bot()

# -- Funções --
pass

# -- Código --
 # Evento do bot quando for iniciado
@bot.event
async def on_ready():
    # Var para saber quantos são os comandos sincronizados
    synced = len(bot.all_slash_commands)
    # Printando quanto foram sincronizados e uma mensagem bonitinha
    print(f'{synced} comandos sincronizados! =)')
    print(f'Bom dia {bot.user.name}! Tudo certo por aqui até então.')
    # Mudando o status e a atividade do bot
    await bot.change_presence(status = disnake.Status.online, activity = disnake.Game('Sendo refeita agora mesmo ;-;'))



 # Rodando o bot
bot.run(token)