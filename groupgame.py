import requests, random, threading, ctypes, os, random

ctypes.windll.kernel32.SetConsoleTitleW('SC Group Finder by Esmée M. Veilleux')
os.system('color A0') # sets background
thread_count = int(input('How many threads do you want? (500 is good for playing, best to not go over 1k or it will lag) : '))

proxies = []
proxy_file = open('proxies.ini', 'r').readlines()
for lines in proxy_file:
    proxies.append(lines)
class Group:

    def __init__(self,groupID):
        self.groupID = groupID
        self.universal_id = ''

    def group(self):
        proxy = random.choice(proxies).strip()
        proxydict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }
        # group = requests.get(f'https://groups.roblox.com/v1/groups/{self.groupID}', headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
        group = requests.get(f'https://groups.roblox.com/v1/groups/{self.groupID}', proxies=proxydict)
        if groups.reply== "HTTP/1.1 429 \r\n":
            time.sleep(int(10))

        if group.status_code == 200:
            return group.json()

    def games(self):
        # games = requests.get(f'https://games.roblox.com/v2/groups/{self.groupID}/games?accessFilter=All&sortOrder=Asc&limit=100', headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
        proxy = random.choice(proxies).strip()
        proxydict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }
        games = requests.get(f'https://games.roblox.com/v2/groups/{self.groupID}/games?accessFilter=All&sortOrder=Asc&limit=100', proxies=proxydict)
        if games.reply== "HTTP/1.1 429 \r\n":
            time.sleep(int(10))
        if games.status_code == 200:
            return games.json()

    def get_universal_id(self,placeID):
        # a = requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={placeID}', headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
        proxy = random.choice(proxies).strip()
        proxydict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }
        a = requests.get(f'https://api.roblox.com/universes/get-universe-containing-place?placeid={placeID}', proxies=proxydict)
        if a.reply== "HTTP/1.1 429 \r\n":
            time.sleep(int(10))
        self.universal_id = a.json()['UniverseId']

    def get_favorites(self):
        # a = requests.get(f'https://games.roblox.com/v1/games/{self.universal_id}/favorites/count', headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
        proxy = random.choice(proxies).strip()
        proxydict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }
        a = requests.get(f'https://games.roblox.com/v1/games/{self.universal_id}/favorites/count', proxies=proxydict)
        if a.reply== "HTTP/1.1 429 \r\n":
            time.sleep(int(10))
        return a.json()

    def get_votes(self):
        # a = requests.get(f'https://games.roblox.com/v1/games/votes?universeIds={self.universal_id}', headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
        proxy = random.choice(proxies).strip()
        proxydict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }
        a = requests.get(f'https://games.roblox.com/v1/games/votes?universeIds={self.universal_id}', proxies=proxydict)
        if a.reply == "HTTP/1.1 429 \r\n":
            time.sleep(int(10))
        return a.json()

    def get_visits(self):
        # a = requests.get(f'https://games.roblox.com/v1/games?universeIds={self.universal_id}', headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
        proxy = random.choice(proxies).strip()
        proxydict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }
        a = requests.get(f'https://games.roblox.com/v1/games?universeIds={self.universal_id}', proxies=proxydict)
        if a.reply== "HTTP/1.1 429 \r\n":
            time.sleep(int(10))
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
                    with threading.Lock():
                        with open('games.txt','a+',encoding='UTF-8') as f:
                            f.write('G-ID:{} | GAME:{} | {} | FAV:{} | LIKE:{} | DISLIKE:{} | VISITS:{}\n'.format(b['id'],x['rootPlace']['id'],x['name'],e['favoritesCount'],g['data'][0]['upVotes'],g['data'][0]['downVotes'],z['data'][0]['visits']))
                            f.flush()
        except:
            pass
for x in range(thread_count):
    threading.Thread(target=group).start()