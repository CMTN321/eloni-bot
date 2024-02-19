import disnake
from disnake.ext import commands
from disnake.ui import Select, View
from disnake import Webhook
import math as m
import random as r
import os
from datetime import datetime
from colorama import Back, Fore, Style
import platform
import aiohttp
import dotenv

# -- Vars --
time_now = datetime.now()
time_format_1 = ' %a, %B, %#d, %Y, %I:%M %p '
time_format_2 = ' %x : %X '
bars = ('--------------------------------------------------')
dotenv.load_dotenv('.env')

# -- Dicionários --
actions = {
    1: "FNaF World",
    2: "Pokémon: Let's Go, Pikachu!",
    3: "Brawl Stars",
    4: "Fortnite",
    5: "Stardew Valley",
    6: "Candies 'n Curses",
    7: "Roblox",
    8: "Rocket League",
    9: "Terraria",
    10: "Minecraft",
    11: "Clash Royale",
    12: "Valorant",}

raças = {
    'elfo' : 'destreza',
    'oni' : 'força',
    'tiefling' : 'constituição',
    'humano' : 'nada',
    'kitsune' : 'vigor/inteligência',
    'dragonborn' : 'defesa'}

classes = {
    'inventor' : 'sorte',
    'rúnico' : 'inteligência',
    'mercenário' : 'força',
    'nada' : 'nada',
    'aventureiro' : 'defesa/destreza'}

# -- Classes --
 # -- Personagens --
class Personagem:
    def __init__(self, name: str, race: str, clas: str, age: int, level: int, xp: int, memid: int, username: str, paramstats: list = None):
        if paramstats == None:
            stats = [5, 5, 5, 5, 5, 1, 5]
        self.stats = stats
        self.newstats = renewstat(stats)
        self.name = name
        self.race = race
        self.clas = clas
        self.age = age
        self.level = level
        self.xp = xp
        self.mxp = mxp(self.level) 
        self.memid = memid
        self.username = username

 # -- Start New Character --
    def start(self):
        with open(fr'rpgchars\{self.name}.txt', 'w+') as f:
            f.writelines(f'5 5 5 5 5 1 5\n')
            f.writelines(f'{self.race}\n')
            f.writelines(f'{self.clas}\n')
            f.writelines(f'{self.age}\n')
            f.writelines(f'{self.level}\n')
            f.writelines(f'{self.xp}\n')
            f.writelines(f'{self.username} - {self.memid}')
        limit = limitcheck(self.memid)
        if limit == 'Não existe':
            with open(fr'ids.txt', 'a') as f:
                f.writelines(f'{self.memid} 1\n')
        else:
            idconta(self.memid, True)

class Menu1(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None
    
    @disnake.ui.button(label = '◀️', style = disnake.ButtonStyle.blurple)
    async def butonesq(self, button: disnake.Button, interaction: disnake.Interaction):
        await interaction.response.send_message(f'{interaction.author.mention} você clicou em mim')

# Functions
 # -- Max Xp --
def mxp(level: int) -> int:
    level = int(level)
    mxp1 = 100
    for i in range(level - 1):
        mxp1 += (10/100) * mxp1
        mxp1 = m.trunc(mxp1)
    return mxp1


 # -- Status Renew --
def renewstat(startstats: list) -> dict:
    pv = 2 * (int(startstats[0]))
    stamina = 2 * (int(startstats[1]))
    defesa = 1 * (int(startstats[2]))
    força = 1 * (int(startstats[3]))
    destreza = 1 * (int(startstats[4]))
    sorte = 1 * (int(startstats[5]))
    inteligência = 1 * (int(startstats[6]))
    mp = 5 * (int(startstats[6]))
    sttsp = {'pv' : pv, 'stamina' : stamina, 'defesa' : defesa, 'força' : força, 'destreza' : destreza, 'sorte' : sorte, 'inteligência' : inteligência, 'mp' : mp}
    return sttsp

 # -- Sorte no número dos dados --
def mod(d: int, sorte: int) -> int:
    if d == 100:
        if sorte <= 10:
            r = (2 * sorte)
        else:
            r = sorte
    elif d == 20:
        r = (sorte / m.ceil(sorte / 10 + 4))
        if r <= 1:
            r = 1
        else:
            r = m.trunc(r)
    return r

 # -- Capitalize --
def cap(word: str) -> str:
    word = (((word.strip()).lower()).title())
    return word

 # -- Names Check --
def limitcheck(iddiscord: int) -> bool:
    with open(fr'ids.txt', 'r') as f:
        ids = f.readlines()
        id = str(iddiscord)
    for i in ids:
        try:
            index = i.index(id)
            splited = i.split()
            id2 = splited[0]
            num = int(splited[1])
            if num == 3 and id != myid:
                return True
            elif num < 3:
                return False
        except ValueError:
            pass
    return 'Não existe'

def idconta(id: int, choice: bool):
    with open(fr'ids.txt', 'r') as f:
        ids = f.readlines()
        id = str(id)
    with open(fr'ids.txt', 'w+') as f:
        f.write('')
        for i in ids:
            splited = i.split()
            idtext = int(splited[0])
            num = int(splited[1])
            try:
                index = i.index(id)
                if choice:
                    f.writelines(f'{idtext} {num + 1}\n')
                else:
                    if num - 1 == 0:
                        pass
                    else:
                        f.writelines(f'{idtext} {num - 1}\n')
            except ValueError:
                f.writelines(f'{idtext} {num}\n')

# -- Code --
bot = commands.Bot()

@bot.event
async def on_ready():
    prefix_start = (Back.BLACK + Fore.GREEN + time_now.strftime(time_format_2) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(prefix_start + "Logged in as: " + Fore.YELLOW + bot.user.name)
    print(prefix_start + "client ID: " + Fore.YELLOW + str(bot.user.id))
    print(prefix_start + "Discord Version: " + Fore.YELLOW + disnake.__version__)
    print(prefix_start + "Python Version: " + Fore.YELLOW + str(platform.python_version()))
    synced = bot.all_slash_commands
    print(prefix_start + "Synced: " + Fore.YELLOW + str(len(synced)) + " Slash Commands")
    print("Bot Chan Online! (E Eloni endoidando =)")
    random_number_action = r.randint(1, len(actions))
    random_action = actions[random_number_action]
    await bot.change_presence(activity = disnake.Activity(type = disnake.ActivityType.playing, name = random_action))

@bot.slash_command(name = 'personagem',description = 'Crie um personagem')
async def personagem(inter, name: str):
    name = cap(name)
    if os.path.exists(fr'p.p\rpg\rpgchars\{name}.txt') or name == 'Ids':
        await inter.response.send_message(f"O personagem {cap(name)} já existe! ;-;", ephemeral = True)
    else:
        limite = limitcheck(inter.user.id)
        if limite == False or limite == 'Não existe':
            perg = Personagem(name, 'Humano', 'Nada', 10, 1, 0, inter.user.id, inter.user.name)
            perg.start()
            with open(fr'ids.txt', 'r') as f:
                ids = f.readlines()
                id = str(inter.user.id)
            for i in ids:
                try:
                    index = i.index(id)
                    splited = i.split()
                    num = int(splited[1])
                except ValueError:
                    pass
            await inter.response.send_message(f"O personagem {cap(name)} foi criado! =) ({num}/3)", ephemeral = True)
        elif limite == True:
            await inter.response.send_message(f"O limite de personagens para o seu ID foi atingido! (3/3)", ephemeral = True)

@bot.slash_command(name = 'remove', description = 'Remove algum personagem da existência, ou para os mais íntimos, R é usado')
async def remove(inter, name: str):
    name = cap(name)
    if os.path.exists(fr'p.p\rpg\rpgchars\{name}.txt'):
        with open(fr'p.p\rpg\rpgchars\{name}.txt', 'r') as f:
            lines = f.readlines()
            id = int(lines[6].split()[2])
        if id == inter.user.id or inter.user.id == int(myid):
            idconta(id, False)
            os.unlink(fr'p.p\rpg\rpgchars\{name}.txt')
            await inter.response.send_message(f"O personagem {name} foi removido! Saudades ;-;", ephemeral = True)
        else:
            await inter.response.send_message(f"O personagem {name} não está sobre o seu domínio! ;-;")
    else:
        await inter.response.send_message(f"O personagem {name} não existe! =(", ephemeral = True)

@bot.slash_command(name = 'status', description = 'Veja os status de seu personagem')
async def status(inter, name: str):
    name = cap(name)
    if os.path.exists(fr'p.p\rpg\rpgchars\{name}.txt'):
        with open(fr'p.p\rpg\rpgchars\{name}.txt', 'r') as f:
            pers = f.readlines()
            stts1 = (pers[0]).split()
        stts = renewstat(stts1)
        embedVar = disnake.Embed(title = f'Status de {name}!', description = 'Status gerais do personagem selecionado', color = 0xC71585)
        embedVar.add_field(name = 'Constituição: ', value = stts1[0], inline = False)
        embedVar.add_field(name = 'Pontos de Vida: ', value = stts['pv'], inline = False)
        embedVar.add_field(name = 'Pontos de Mana: ', value = stts['mp'], inline = False)
        embedVar.add_field(name = 'Vigor: ', value = stts1[1], inline = False)
        embedVar.add_field(name = 'Stamina: ', value = stts['stamina'], inline = False)
        embedVar.add_field(name = 'Defesa: ', value = stts['defesa'], inline = False)
        embedVar.add_field(name = 'Força: ', value = stts['força'], inline = False)
        embedVar.add_field(name = 'Destreza: ', value = stts['destreza'], inline = False)
        embedVar.add_field(name = 'Sorte: ', value = stts['sorte'], inline = False)
        embedVar.add_field(name = 'Inteligência: ', value = stts['inteligência'], inline = False)
        await inter.response.send_message(embed = embedVar, ephemeral = True)
    else:
        await inter.response.send_message(f"O personagem {name} não existe! =(", ephemeral = True)

@bot.slash_command(name = 'info', description = 'Mostra algumas informações sobre o personagem')
async def info(inter, name: str):
    name = cap(name)
    if os.path.exists(fr'p.p\rpg\rpgchars\{name}.txt'):
        with open(fr'p.p\rpg\rpgchars\{name}.txt', 'r') as f:
            pers = f.readlines()
            stts = (pers[0]).split()
            race = pers[1]
            classe = pers[2]
            age = int(pers[3])
            level = int(pers[4])
            xp = int((pers[5])[:-1])
        stts = renewstat(stts)
        maxxp = mxp(level)
        embedVar = disnake.Embed(title = f'Info de {name}!', description = f'Informações gerais sobre {name}!', color = 0xC71585)
        embedVar.add_field(name = 'Nome: ', value = name, inline = False)
        embedVar.add_field(name = 'Classe: ', value = classe, inline = False)
        embedVar.add_field(name = 'Raça: ', value = race, inline = False)
        embedVar.add_field(name = 'Idade: ', value = age, inline = False)
        embedVar.add_field(name = 'level: ', value = level, inline = False)
        embedVar.add_field(name = 'Xp: ', value = f'{xp}/{maxxp}', inline = False)
        embedVar.add_field(name = 'Sorte nos dados: ', value = f'Em um D20: + {mod(20, stts["sorte"])}; Em um D100: + {mod(100, stts["sorte"])}', inline = False)
        await inter.response.send_message(embed = embedVar, ephemeral = True, view = Menu1())
    else:
        await inter.response.send_message(f"O personagem {name} não existe! =(", ephemeral = True)

@bot.slash_command(name = 'message', description = 'Send a message from a webhook')
async def message(inter, type: str = commands.Param(choices = ['send', 'edit', 'remove']), name: str = None, message: str = None):
    name = cap(name)
    if os.path.exists(fr'p.p\rpg\rpgchars\{name}.txt'):
        if type == 'send':
            with open(fr'p.p\rpg\rpgchars\{name}.txt', 'r+') as f:
                lines = f.readlines()
                id = int(lines[6].split()[2])
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(webhookid, session = session)
                    try: 
                        avatar = lines[7]
                        if id == inter.user.id or inter.user.id == int(myid):
                            obj = await webhook.send(message, username = name, avatar_url = avatar, wait = True)
                            messageid = (obj.id)
                            x = 0
                            f.write('')
                            for i in lines:
                                x += 1
                                if x == 8:
                                    f.writelines(str(messageid))
                                else:
                                    f.writelines(i)
                        else:
                            await inter.response.send_message(f"O personagem {name} não está sobre o seu domínio! ;-;")
                    except IndexError:
                        if id == inter.user.id or inter.user.id == int(myid):
                            obj = await webhook.send(message, username = name)
                            messageid = (obj.id)
                    await inter.response.send_message(f"A mensagem foi enviada =)", ephemeral = True)
        elif type == 'edit':
            pass
    else:
        await inter.response.send_message(f"O personagem {name} não existe! =(", ephemeral = True)

# -- Rodando o client --
bot.run(token)