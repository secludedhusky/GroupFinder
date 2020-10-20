import requests,random,threading,ctypes,os
from discord_webhook import DiscordWebhook, DiscordEmbed
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/645798299328315432/9iXGxJykOXwagFfJUjfYj4DdodjHGPRxGbOfs9eeYXBkPewwZ3aynCm2kgSnzLtpRbep')


ctypes.windll.kernel32.SetConsoleTitleW('SC Group Finder by Esmée M. Veilleux')
os.system('color A0') # sets background

class Group:
    def __init__(self,groupID):
        self.groupID = groupID
        self.universal_id = ''

    def group(self):
        group = requests.get(f'https://groups.roblox.com/v1/groups/{self.groupID}')
        if group.status_code == 200:
            return group.json()

    def games(self):
        games = requests.get(f'https://games.roblox.com/v2/groups/{self.groupID}/games?accessFilter=All&sortOrder=Asc&limit=100')
        if games.status_code == 200:
            return games.json()

    def get_universal_id(self,placeID):
        a = requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={placeID}')
        self.universal_id = a.json()['UniverseId']

    def get_favorites(self):
        a = requests.get(f'https://games.roblox.com/v1/games/{self.universal_id}/favorites/count')
        return a.json()

    def get_votes(self):
        a = requests.get(f'https://games.roblox.com/v1/games/votes?universeIds={self.universal_id}')
        return a.json()

    def get_visits(self):
        a = requests.get(f'https://games.roblox.com/v1/games?universeIds={self.universal_id}')
        return a.json()


duplicated_groups = []

def group():
    while True:
        try:
            random_group_id = random.randint(1,4952886)

            if random_group_id not in duplicated_groups:
                duplicated_groups.append(random_group_id)
            else:
                continue

            a = Group(random_group_id)
            b = a.group()

            if 'isLocked' in b:
                continue
            else:
                if b['owner'] != None or b['publicEntryAllowed'] != True:
                    continue
                else:
                    c = a.games()
                    for x in c['data']:
                        d = a.get_universal_id(x['rootPlace']['id'])
                        e = a.get_favorites()
                        g = a.get_votes()
                        z = a.get_visits()

                        print('G-ID:{} | ID:{} | {} | FAV:{} | LIKE:{} | DISLIKE:{} | VISITS:{}'.format(b['id'],x['rootPlace']['id'],x['name'],e['favoritesCount'],g['data'][0]['upVotes'],g['data'][0]['downVotes'],z['data'][0]['visits']))
                        embed = DiscordEmbed(title='Jamie Groups', description='Mit einundzwanzig trage ich Windeln.', color=800080)
                        embed.add_embed_field(name='G-ID', value=b['id'])
                        embed.add_embed_field(name='GAME', value=x['rootPlace']['id'])
                        embed.add_embed_field(name='NAME', value=x['name'])
                        embed.add_embed_field(name='FAVORITES', value=e['favoritesCount'])
                        embed.add_embed_field(name='LIKES', value=g['data'][0]['upVotes'])
                        embed.add_embed_field(name='DISLIKES', value=g['data'][0]['downVotes'])
                        embed.add_embed_field(name='VISITS', value=z['data'][0]['visits'])
                        webhook.add_embed(embed)
                        webhook.execute()
                    with threading.Lock():
                        with open('games.txt','a+',encoding='UTF-8') as f:
                            f.write('G-ID:{} | GAME:{} | {} | FAV:{} | LIKE:{} | DISLIKE:{} | VISITS:{}\n'.format(b['id'],x['rootPlace']['id'],x['name'],e['favoritesCount'],g['data'][0]['upVotes'],g['data'][0]['downVotes'],z['data'][0]['visits']))
                            f.flush()
        except:
            pass
for x in range(30):
    threading.Thread(target=group).start()

