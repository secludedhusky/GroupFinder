import requests,random,threading,ctypes,os

ctypes.windll.kernel32.SetConsoleTitleW('SC Group Finder by Esmée M. Veilleux')
os.system('color A0') # sets background

class Group:
    def __init__(self,groupID):
        self.groupID = groupID
        self.universal_id = ''

duplicated_groups = []

def group():
    while True:
        try:
            print('G-ID:{} | ID:{} | {} | FAV:{} | LIKE:{} | DISLIKE:{} | VISITS:{}'.format(random.randint(1,4952886),random.randint(1,444952886),"Untitled's Place",random.randint(1,2886),random.randint(1,2886),random.randint(1,2886),random.randint(1,642886)))
        except:
            pass
for x in range(30):
    threading.Thread(target=group).start()

