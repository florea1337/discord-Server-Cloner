# fetch_server_data.py

import requests
import json

token = 'your user token'
guild_id = 'target server ID'

headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
}

def fetch_guild_data(guild_id):
    response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=headers)
    return response.json()

def fetch_channels(guild_id):
    response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers)
    return response.json()

def fetch_roles(guild_id):
    response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers)
    return response.json()

guild_data = fetch_guild_data(guild_id)
channels = fetch_channels(guild_id)
roles = fetch_roles(guild_id)

with open('guild_data.json', 'w') as f:
    json.dump(guild_data, f, indent=4)

with open('channels.json', 'w') as f:
    json.dump(channels, f, indent=4)

with open('roles.json', 'w') as f:
    json.dump(roles, f, indent=4)

print('Data fetched successfully!')
