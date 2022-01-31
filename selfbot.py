# This code is written by Shahzain completely, please do not take credits for it
### ================================ ###
#                Libs
### ================================ ###
import time
import httpx
import base64
import random
import string
from installibs import installAllLibs
from memberscraper import MemberScrapper
from itertools import cycle
import json as theJson
installAllLibs()
proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
### ================================ ###
#          Main Self Bot Class
### ================================ ###
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
class ShahzainSelfBot:
    def __init__(self, token):
        self.session = httpx.Client(
            proxies={"https://": f"http://{next(proxs)}"}, headers={"Accept": "*/*", "Accept-Language": "en-US", "Connection": "keep-alive", "Content-Type": "application/json", "DNT": "1", "Host": "discord.com", "Referer": "https://discord.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "TE": "trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0", "X-Track": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTk5OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="})
        # Note: If u are skidding this without adding sessions or proper headers ur token will get locked
        self.session.headers["X-Fingerprint"] = self.session.get(
            "https://discord.com/api/v9/experiments", timeout=30).json().get("fingerprint")
        self.session.headers["Origin"] = "https://discord.com"
        self.token = token
        self.session.headers['Authorization'] = token
    def scrape(self, guildId, channelId):
        scrapper = MemberScrapper(token=self.token)
        members = scrapper.get_members(guildId, channelId)
        memberslist = []
        with open("ids.json", "r") as file:
          data = theJson.load(file)
        total_scraped = 0
        for memberID in members:
          if memberID not in data:
            total_scraped += 1
            data.append(int(memberID))
            print(f"{total_scraped}/{len(members)} - {memberID}")
        with open("ids.json", "w") as file:
          theJson.dump(data, file)
        end = time.time()
    def banMember(self, guildId, memberId):
                status = self.session.put(
                    f'https://discord.com/api/v9/guilds/{guildId}/bans/{memberId}', json={"delete_message_days": 1}).status_code
                if status != 204:
                    print(f'{bcolors.FAIL}[>] Failed to ban {memberId}')
                else:
                    print(f'{bcolors.OKGREEN}[>] Banned {memberId}')

    def spamWebhook(self, webhook_url, content):
        while True:
            httpx.post(webhook_url, json={
                       "content": content, "username": "Shahzain SelfBot"})

    def deleteChannel(self, channelId):
        status = self.session.delete(
            f'https://discord.com/api/v9/channels/{channelId}').status_code
        if status != 200:
            print(f"{bcolors.FAIL}[>] Failed to delete {channelId}")
        else:
            print(f'{bcolors.OKGREEN}[>] Deleted {channelId}')

    def createChannel(self, guildId, channelName):
        req = self.session.post(f"https://discord.com/api/v9/guilds/{guildId}/channels", json={
                                "name": channelName, "permission_overwrites": [], "type": 0})
        if req.status_code != 201:
            print(f'{bcolors.FAIL}[>] Failed to create channel!')
        else:
            print(f'{bcolors.OKGREEN}[>] Created channel {req.json()["id"]}')

    def createRole(self, guildId, roleName):
        req = self.session.post(
            f'https://discord.com/api/v9/guilds/{guildId}/roles', json={"name": roleName})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to create role')
        else:
            print(f'{bcolors.OKGREEN}[>] Created role {req.json()["id"]}')

    def createGuilds(self, guildName):
        req = self.session.post('https://discord.com/api/v9/guilds', json={"channels": [
        ], "name": guildName, "guild_template_code": "2TffvPucqHkN", "icon": None, "system_channel_id": None})
        if req.status_code != 201:
            print(f'{bcolors.FAIL}[>] Failed to create guild!')
        else:
            print(f'{bcolors.OKGREEN}[>] Created guild {req.json()["id"]}')

    def setAvatar(self, avatarUrl):
        base64Encoded = base64.b64encode(httpx.get(avatarUrl).content).decode('ascii')
        req = self.session.patch('https://discord.com/api/v9/users/@me',
                                 json={"avatar": f"data:image/png;base64,{base64Encoded}"})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to change avatar')
        else:
            print(f'{bcolors.OKGREEN}[>] Changed avatar!')

    def setTheme(self, theme):
        req = self.session.patch(
            'https://discord.com/api/v9/users/@me/settings', json={"theme": theme})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to set theme')
        else:
            print(f'{bcolors.OKGREEN}[>] Set theme to {theme}')

    def blockUser(self, userId):
        req = self.session.put(
            f'https://discord.com/api/v9/users/@me/relationships/{userId}', json={"type": 2})
        if req.status_code != 204:
            print(f'{bcolors.FAIL}[>] Failed to block {userId}')
        else:
            print(f'{bcolors.OKGREEN}[>] Blocked {userId}')

    def deleteGuild(self, guildId):
        req = self.session.post(
            f'https://discord.com/api/v9/guilds/{guildId}/delete', json={})
        if req.status_code != 204:
            print(f'{bcolors.FAIL}[>] Failed to delete guild {guildId}')
        else:
            print(f'{bcolors.OKGREEN}[>] Deleted guild {guildId}')

    def changeBio(self, newBio):
        req = self.session.patch(
            'https://discord.com/api/v9/users/@me', json={"bio": newBio})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to change bio')
        else:
            print(f'{bcolors.OKGREEN}[>] Changed bio to {newBio}')

    def changeMsgDisplay(self, type):
        req = self.session.patch(
            f"https://discord.com/api/v9/users/@me/settings-proto/1", json={"settings": type})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to change Msg Display')
        else:
            print(f'{bcolors.OKGREEN}[>] Changed message display')

    def changeHypeSquad(self, type):
        req = self.session.post(
            'https://discord.com/api/v9/hypesquad/online', json={"house_id": type})
        if req.status_code != 204:
            print(f'{bcolors.FAIL}[>] Failed to change hypesquad')
        else:
            print(f'{bcolors.OKGREEN}[>] Changed hypesquad!')

    def changeLang(self, lang):
        req = self.session.patch(
            'https://discord.com/api/v9/users/@me/settings', json={"locale": lang})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to change language')
        else:
            print(f'{bcolors.OKGREEN}[>] Changed language')

    def changeDevSettings(self, type):
        req = self.session.patch(
            'https://discord.com/api/v9/users/@me/settings-proto/1', json={"settings": type})
        if req.status_code != 200:
            print(f"{bcolors.FAIL}[>] Failed to change dev settings")
        else:
            print(f'{bcolors.OKGREEN}[>] Changed dev settings')

    def disableToken(self):
        req = httpx.post('https://discord.com/api/v9/invites/pornhub',
                         json={}, headers={'Authorization': self.token})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to lock token')
        else:
            print(f'{bcolors.OKGREEN}[>] Token Locked')
            exit()

    def getChatId(self, userId):
        req = self.session.post(
            "https://discord.com/api/v9/users/@me/channels", json={"recipients": [userId]})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to create chat with {userId}')
        else:
            print(f'{bcolors.OKGREEN}[>] Created chat with {userId}')
            return req.json()['id']

    def sendDM(self, userId, message):
        channelId = self.getChatId(userId)
        req = self.session.post(f'https://discord.com/api/v9/channels/{channelId}/messages', json={
            "content": message,
            "tts": False,
            "nonce": self.getRandomNonce()
        })
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to send message to {userId}')
            print(req.json())
        else:
            print(f'{bcolors.OKGREEN}[>] Sent message, messageId: {req.json()["id"]}')

    def getRandomNonce(self):
        return "".join(random.choice(string.digits) for i in range(18))

    def joinServer(self, invite):
        req = self.session.post(
            f'https://discord.com/api/v9/invites/{invite}', json={})
        if req.status_code != 200:
            print(f"{bcolors.FAIL}[>] Failed to join server!")
        else:
            print(f'{bcolors.OKGREEN}[>] Joined server')

    def sendMsgInGuildChannel(self, channelId, msg):
        req = self.session.post(f'https://discord.com/api/v9/channels/{channelId}/messages', json={
            "content": msg,
            "tts": False,
            "nonce": self.getRandomNonce()
        })
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to send message in {channelId}')
            print(req.json())
        else:
            print(f'{bcolors.OKGREEN}[>] Sent message, messageId: {req.json()["id"]}')
    def deleteRole(self, guildId, roleId):
        req = self.session.delete(f'https://discord.com/api/v9/guilds/{guildId}/roles/{roleId}')
        if req.status_code != 204:
            print(f'{bcolors.FAIL}[>] Failed to delete {roleId}')
        else:
            print(f'{bcolors.OKGREEN}[>] Deleted {roleId}')
    def createWebhook(self, channelId):
        req = self.session.post(f'https://discord.com/api/v9/channels/{channelId}/webhooks', json={"name": "Shahzain-self-bot"})
        if req.status_code != 200:
            print(f'{bcolors.FAIL}[>] Failed to create channel webhook')
        else:
            print(f'{bcolors.OKGREEN}[>] Created webhook: https://discord.com/api/webhooks/{req.json()["id"]}{req.json()["token"]}')
            return f'https://discord.com/api/webhooks/{req.json()["id"]}{req.json()["token"]}'
    def leaveGuild(self, guildId):
        req = self.session.delete(f"https://discord.com/api/v9/users/@me/guilds/{guildId}")
        if req.status_code != 204:
            print(f'{bcolors.FAIL}[>] Failed to leave guild')
        else:
            print(f'{bcolors.OKGREEN}[>] Left guild {guildId}')
    def deleteEmoji(self, guildId, emojiId):
        req = self.session.delete(f'https://discord.com/api/v9/guilds/{guildId}/emojis/{emojiId}')
        if req.status_code != 204:
            print(f"{bcolors.FAIL}[>] Failed to delete emoji {emojiId}")
        else:
            print(f"{bcolors.OKGREEN}[>] Deleted emoji {emojiId}")