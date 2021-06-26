from chat import Message
from station import Station
from api import Rest
import json

with open("config.json") as json_file:
    config = json.load(json_file)
    json_file.close()

wlan = Station(config['wlan_ssid'], config['wlan_pass'])

chat = Message(config['tg_chat_id'], config['tg_bot_id'])

Rest(chat, wlan)
