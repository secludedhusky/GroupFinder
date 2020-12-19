import requests
import threading
import time
import random
import ctypes

threads = 250
group_ids = [*range(6000000, 7800000)]
random.shuffle(group_ids)
popped_groups = group_ids

results = open('results.txt', 'w')
results.close()

proxies = []
proxy_file = open('proxies.txt', 'r').readlines()
for lines in proxy_file:
    proxies.append(lines)

invalid = 0
hits = 0

i = 0
def groupthingy():
    global invalid
    global hits
    while i < len(group_ids):
        proxy = random.choice(proxies).strip()
        proxydict = {
        "http": f"http://{proxy}",
        "https": f"https://{proxy}",
        }
        current_group = popped_groups.pop()
        ctypes.windll.kernel32.SetConsoleTitleW(f"Group Finder | Invalid: {invalid} | Hits: {hits} | CPM: {cpm} | Elapsed Time: {formatted_time}")
        try:
            group = requests.get(f'https://groups.roblox.com/v1/groups/{current_group}', proxies=proxydict)
            json = group.json()
            if '"isLocked":true' not in group.text:
                if json['owner'] == None:
                    if json['publicEntryAllowed'] == True:
                        print(f"Group: {current_group} is claimable!")
                        hits += 1
                        results = open('results.txt', 'a')
                        results.write(f"Group: {current_group} is claimable!\n")
                        results.close()
                    else:
                        print(f"Group: {current_group} is locked.")
                        invalid += 1
                else:
                    print(f"Group: {current_group} has a owner.")
                    invalid += 1
            else:
                print("Group is locked.")
                invalid += 1
        except Exception:
            print("Fatal Error")
            invalid += 1
            pass

cpm = 0
def cpm_runner():
    global cpm
    while True:
        old_results = invalid + hits
        time.sleep(2)
        new_results = invalid + hits
        cpm = (new_results - old_results) * 30
cpmthread = threading.Thread(target=cpm_runner)
cpmthread.start()

starttime = time.time()
def time_runner():
    global starttime
    global elapsed_time
    global formatted_time
    while True:
        elapsed_time = time.time() - starttime
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
timethread = threading.Thread(target=time_runner)
timethread.start()

groupthreads = []
for gk in range(threads):
    lt = threading.Thread(target=groupthingy)
    groupthreads.append(lt)
    lt.start()
    time.sleep(0.1)