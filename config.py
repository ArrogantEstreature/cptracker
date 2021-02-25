TIMEZONE = 'America/Chicago'
DB_GUILD_CHANNEL_MAPPING = {
    'sw5e': {
        'guild': 'Star Wars WM',
        'cp_tracker_channel': 'cp-tracker',
        'valid_channels': [
            'hangar-bay',
            'training-rooms',
            'comms-room',
            'conference-room',
            'meditation-chamber',
            'mess-hall',
            'personal-quarters',
            'medbay',
            'mos-eisley',
        ],
    },
    'lasthope': {
        'guild': 'Last Hope Campaign!',
        'cp_tracker_channel': 'chat-point-tracker',
        'valid_channels': [
            'miserable-mug',
            'around-town',
            'outside-town',
        ],
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
