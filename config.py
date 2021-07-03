TIMEZONE = 'America/Chicago'
DB_GUILD_CHANNEL_MAPPING = {
    'sw5e': {
        'guild': 'Star Wars WM',
        'cp_tracker_channel': 'cp-tracker',
        'valid_channel_category_ids': [
            797985544440119296, # Leviathan RP
            853860884883570719, # Holonet RP
            797987844122738728, # Tatooine RP
            840797936190357504, # Zeltros RP
            841143606274293792, # Kashyyyk RP
            860658786791325706, # Convor RP
        ],
        'valid_channel_ids': [
            836079866733395979, # New Republic IC Chat
            836079921368924167, # Empire IC Chat
            836080001149435944, # Mandalorian IC Chat
            836080033067171841, # Bounty Hunter IC Chat
            836080057763102721, # Sith IC Chat
            836080113422565396, # Jedi IC Chat
            836080170259185694, # Guardian IC Chat
            836080233072951346, # Medical Insitution IC Chat
            836080873329262632, # Ranger Corp IC Chat
            836081290637344788, # Droid Federation IC Chat
        ],
    },
    'lasthope': {
        'guild': 'Last Hope Campaign!',
        'cp_tracker_channel': 'chat-point-tracker',
        'valid_channel_category_ids': [
            763950173079863297,
        ],
        'valid_channel_ids': [],
    },
}
GUILD_DB_MAPPING = {
    'Star Wars WM': 'sw5e',
    'Last Hope Campaign!': 'lasthope',
}
# INVALID_TIMEZONE_MESSAGE = '''
# Your timezone setting must be a valid TZ Database Name.
# Please see the following page and choose your timezone: https://kevinnovak.github.io/Time-Zone-Picker/
# (It should look something like Europe/London)
# '''
