TIMEZONE = 'America/Chicago'
COMMAND_PERMISSION_ROLES = ['DM', 'Lead DM', 'temp dm', 'Techno Wiz (Our Claptrap)', 'Tech Dudes', 'Technomancer']
DB_GUILD_CHANNEL_MAPPING = {
    'sw5e': {
        'guild': 'Leviathan Project (WM)',
        'cp_tracker_channel': 'cp-tracker',
        'bot-channel': 'bot-channel',
        'valid_channel_category_ids': [
            797985544440119296, # Leviathan RP
            853860884883570719, # Holonet RP
            797987844122738728, # Tatooine RP
            840797936190357504, # Zeltros RP
            841143606274293792, # Kashyyyk RP
            860658786791325706, # Convor RP
            886293422997135460, # Korriban RP
            960199367023820830, # The Guardian RP
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
    'Mists of Asira': {
        'guild': 'Last Hope Campaign!',
        'cp_tracker_channel': 'chat-point-tracker',
        'bot-channel': 'bot-channel',
        'valid_channel_category_ids': [
            763950173079863297, # Roleplay Channels
        ],
        'valid_channel_ids': [],
    },
    'starbreak': {
        'guild': 'StarBreak',
        'cp_tracker_channel': 'cp-tracker',
        'bot-channel': 'bot-channel',
        'valid_channel_category_ids': [
            903023805214101544, # Internet RP
            903026947674734613, # New Orleans RP
        ],
        'valid_channel_ids': [],
    },
}
GUILD_DB_MAPPING = {
    'Leviathan Project (WM)': 'sw5e',
    'Last Hope Campaign!': 'lasthope',
    'StarBreak': 'starbreak',
}
SW5E_DOWNTIME = {
    'bountyhunting': {
        '40-': 'You fail to catch your target.',
        '41-70': 'You fail to catch your target, but stumble across a lesser bounty, earning 500 cr.',
        '71-100': 'You catch your target, resulting in a 1,000 cr bounty.',
        '101-110': 'You catch a high-value target, resulting in a 2,500 cr bounty.',
        '111+': 'You catch a kingpin, resulting in a 10,000 cr bounty and a nickname.',
    },
    'buyingenhanced': {
        '40-': 'A seller asking five times the item’s value, or a shady seller asking two and a half times the item’s value.',
        '41-70': 'A seller asking twice the item’s value, or a shady seller asking the full item’s value.',
        '71-100': 'A seller asking the full item’s value.',
        '101-110': 'A shady seller asking half the item’s value, no questions asked.',
        '111+': 'A seller asking half the item’s value, and a favor.',
    },
    'carousing': {
        '40-': 'You make a hostile contact.',
        '41-70': 'You make no new contacts.',
        '71-100': 'You make an allied contact.',
        '101-110': 'You make two allied contacts.',
        '111+': 'You make three allied contacts.',
    },
    'crafting': {
        '40-': 'You inefficiently craft the item, expending twice the requisite raw materials.',
        '41-70': 'You inefficiently craft the item, expending one and a half times the requisite raw materials.',
        '71-100': 'You craft the item with no significant issue.',
        '101-110': 'You efficiently craft the item, using only half the requisite materials. If the item required a rare material, you also used a reduced amount of that material.',
        '111+': 'You expertly craft the item, using only one-quarter the requisite materials. If the item required a rare material, you also used a reduced amount of that material.',
    },
    'crime': {
        '40-': 'The robbery fails, but you escape.',
        '41-70': 'You earn 500 cr by robbing a struggling merchant.',
        '71-100': 'You earn 1,000 cr by robbing a prosperous figure.',
        '101-110': 'You earn 2,500 cr by robbing a noble.',
        '111+': 'You earn 10,000 cr by robbing one of the richest figures in town.',
    },
    'espionage': {
        '40-': 'You fail to find any useful information with which to blackmail, and your face is clearly identified.',
        '41-70': 'You find no useful information.',
        '71-100': 'You find information with which to blackmail one person.',
        '101-110': 'You find information with which to blackmail two people.',
        '111+': 'You find information with which to blackmail three people.',
    },
    'gambling': {
        '40-': 'You lose your entire stake.',
        '41-70': 'You lose half your stake.',
        '71-100': 'You break even. Not bad.',
        '101-110': 'You win an amount equal to your stake.',
        '111+': 'You win an amount equal to three times your stake.',
    },
    'mercenary': {
        '40-': 'The character finds a job, but fails to complete it successfully and goes unpaid.',
        '41-70': 'You complete a relatively simple job, earning 250 cr.',
        '71-100': 'You complete a moderately difficult job, earning 500 cr.',
        '101-110': 'You complete an exceptionally difficult task, earning 1,250 cr.',
        '111+': 'You complete an insanely difficult task, earning 5,000 cr and a favor from your employer.',
    },
    'pitfighting': {
        '40-': 'You lose all of your bouts.',
        '41-70': 'You win some of your bouts, earning 250 cr.',
        '71-100': 'You win half of your bouts, earning 500 cr.',
        '101-110': 'You win most of your bouts, earning 1,500 cr.',
        '111+': 'You go undefeated, earning 5,000 cr and a title recognized by the people of this town.',
    },
    'racing': {
        '40-': 'You lose all of your races.',
        '41-70': 'You win some of your races, earning 500 cr.',
        '71-100': 'You win half of your races, earning 1,000 cr.',
        '101-110': 'You win most of your races, earning 2,500 cr.',
        '111+': 'You go undefeated, earning 10,000 cr and a title recognized by the people of this town.',
    },
    'research': {
        '40-': 'You learn nothing.',
        '41-70': 'You learn one piece of lore.',
        '71-100': 'You learn two pieces of lore.',
        '101-110': 'You learn three pieces of lore.',
        '111+': 'You learn five pieces of lore, as well as the relative location of an item worth at least 5,000 cr.',
    },
    'sellingenhanced': {
        '40-': 'A buyer offering one-quarter of the item’s value, or a shady buyer offering half the item’s value.',
        '41-70': 'A buyer offering half the item’s value, or a shady buyer offering the full item’s value.',
        '71-100': 'A buyer offering the full item’s value.',
        '101-110': 'A shady buyer offering one and a half times the item’s value, no questions asked.',
        '111+': 'A buyer offering one and a half times the item’s value, but they also want a favor.',
    },
    'training': {
        '40-': 'Your training falters, advancing only half a workweek towards completion.',
        '41-70': 'Your training is adequate, advancing one workweek towards completion.',
        '71-100': 'Your training has a breakthrough, advancing two workweeks towards completion.',
        '101-110': 'Your training is excellent, advancing three workweeks towards completion.',
        '111+': 'Your training is masterful, advancing four workweeks towards completion.',
    },
    'work': {
        '40-': 'You earn enough to support a poor lifestyle for the week, with 10 cr left over.',
        '41-70': 'You earn enough to support a modest lifestyle for the week, with 50 cr left over.',
        '71-100': 'You earn enough to support a comfortable lifestyle for the week, with 100 cr left over.',
        '101-110': 'You earn enough to support a wealthy lifestyle for the week, with 200 cr left over.',
        '111+': 'You somehow earn enough to support an aristocratic lifestyle for the week, with 500 cr left over.',
    },
}
SW5E_FAILURE_DOWNTIME = {
    'crime': 'You are caught and jailed.',
    'espionage': 'You are caught and jailed.',
    'mercenary': 'You fail to find a job.',
    'pitfighting': 'You lose all of your bouts and suffer 1 level of exhaustion.',
    'racing': 'You lose all of your races and crash your vehicle, requiring at least 1000 credits in repairs to fix.',
}
# INVALID_TIMEZONE_MESSAGE = '''
# Your timezone setting must be a valid TZ Database Name.
# Please see the following page and choose your timezone: https://kevinnovak.github.io/Time-Zone-Picker/
# (It should look something like Europe/London)
# '''
