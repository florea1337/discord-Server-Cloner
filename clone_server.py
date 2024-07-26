# clone_server.py

import requests
import json

token = 'your user token'
new_guild_id = 'your server ID'

headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
}

with open('channels.json') as f:
    channels = json.load(f)

with open('roles.json') as f:
    roles = json.load(f)

# Create a mapping from old category ID to new category ID
category_mapping = {}

def create_role(guild_id, role):
    data = {
        'name': role['name'],
        'permissions': role['permissions'],
        'color': role['color'],
        'hoist': role['hoist'],
        'mentionable': role['mentionable']
    }
    response = requests.post(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers, json=data)
    return response.json()

def create_channel(guild_id, channel, parent_id=None):
    data = {
        'name': channel['name'],
        'type': channel['type'],
        'topic': channel.get('topic'),
        'nsfw': channel.get('nsfw'),
        'position': channel['position']
    }
    if parent_id:
        data['parent_id'] = parent_id
    response = requests.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json=data)
    return response.json()

# First, create categories
for channel in channels:
    if channel['type'] == 4:  # Category channel type
        new_category = create_channel(new_guild_id, channel)
        category_mapping[channel['id']] = new_category['id']

# Then, create other channels under their respective categories
for channel in channels:
    if channel['type'] != 4:  # Non-category channels
        parent_id = category_mapping.get(channel['parent_id'])
        create_channel(new_guild_id, channel, parent_id=parent_id)

# Create roles
for role in roles:
    if role['name'] != '@everyone':
        create_role(new_guild_id, role)

print('Server cloned successfully!')
