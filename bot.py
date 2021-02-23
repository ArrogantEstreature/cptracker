# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import discord
import datetime
import pytz
from discord.ext import tasks, commands
import pymongo
from pymongo import MongoClient

TIMEZONE = 'America/Chicago'
GUILD_NAME = 'Star Wars WM'
VALID_CHANNELS = [
    'hangar-bay',
    'training-rooms',
    'comms-room',
    'conference-room',
    'meditation-chamber',
    'mess-hall',
    'personal-quarter',
    'medbay',
]
# INVALID_TIMEZONE_MESSAGE = '''
# Your timezone setting must be a valid TZ Database Name.
# Please see the following page and choose your timezone: https://kevinnovak.github.io/Time-Zone-Picker/
# (It should look something like Europe/London)
# '''

token = open('token.txt', 'r').read()
bot = commands.Bot(command_prefix='!')
cluster = MongoClient('mongodb+srv://bachang:{0}@cluster0.pry4u.mongodb.net/test'.format(open('password.txt', 'r').read()))
database = cluster['sw5e']
cpdata = database['cpdata']
# timezone = database['timezone']
daily_word_count = database['daily_word_count']


class WordCountCPUpdater(commands.Cog):
    def __init__(self, bot_instance):
        self.bot = bot_instance
        self.max_daily_cp = 5
        self.word_count_per_cp = 75
        self.date = datetime.datetime.now(pytz.timezone(TIMEZONE)).date()
        self.update_word_count_cp.start()

    @tasks.loop(seconds=10.0)
    async def update_word_count_cp(self):
        # Don't run any commands if the bot is not logged in yet
        if not self.bot.is_ready():
            return
        date_now = datetime.datetime.now(pytz.timezone(TIMEZONE)).date()
        if self.date < date_now:
            datestr = self.date.strftime('%d/%m/%Y')
            for post in daily_word_count.find():
                userid = post['_id']
                word_count = post['word_count']
                cp_gained = word_cp if ((word_cp := word_count // self.word_count_per_cp) <= self.max_daily_cp) else self.max_daily_cp

                # Update CP
                _update_cp(userid, cp_gained)

                # Reset word count
                daily_word_count.update_one({'_id': userid}, {'$set': {'word_count': 0}})

                # Notify members
                user = await bot.fetch_user(userid)
                channel = discord.utils.get(bot.get_all_channels(), guild__name=GUILD_NAME, name=VALID_CHANNELS[0])
                await channel.send('{0} earned {1} CP for writing {2} words on {3}'.format(user.name, cp_gained, word_count, datestr))
            self.date = date_now


def _update_cp(user_id, val):
    if cpdata.find_one({'_id': user_id}):
        cpdata.update_one({'_id': user_id}, {'$inc': {'cp': val}})
    else:
        post = {'_id': user_id, 'cp': val}
        cpdata.insert_one(post)


def _get_word_count(context):
    return res['word_count'] if (res := daily_word_count.find_one({'_id': context.author.id})) else 0


def _get_cp(context):
    return res['cp'] if (res := cpdata.find_one({'_id': context.author.id})) else 0


# def get_timezone(context):
#     return res['tz'] if (res := timezone.find_one({'_id': context.author.id})) else None


# def is_valid_timezone(tz):
#     """
#     Check if the timezone string is valid
#     @param tz:
#     @return:
#     """
#     if not tz:
#         return False
#
#     timezones = [x.lower() for x in pytz.all_timezones]
#     return tz.lower() in timezones


async def update_word_count(message):
    # Don't update word count if message was not sent in a valid channel
    if message.channel.name not in VALID_CHANNELS:
        return
    num_words = len(str(message.content).split())
    # Need to handle when users edit and delete their messages
    if daily_word_count.find_one({'_id': message.author.id}):
        daily_word_count.update_one({'_id': message.author.id}, {'$inc': {'word_count': num_words}})
    else:
        post = {'_id': message.author.id, 'word_count': num_words}
        daily_word_count.insert_one(post)


@bot.event
async def on_ready():
    print('{0} has connected to Discord!'.format(bot.user))


@bot.event
async def on_message(message):
    # Don't run any commands if the bot is not logged in yet
    if not bot.is_ready():
        return
    # Ignore if the message was sent by the bot itself
    if message.author.bot:
        return
    await update_word_count(message)
    await bot.process_commands(message)


@bot.command(name='checkwords', aliases=['checkword'])
async def checkwords(context):
    print('hi')
    word_count = _get_word_count(context)
    await context.send('{0}, so far you have typed {1} words today.'.format(context.author.mention, word_count))


@bot.command(name='checkcp', aliases=['checkCP'])
async def checkcp(context):
    cp = _get_cp(context)
    await context.send('{0}, you currently have {1} CP.'.format(context.author.mention, cp))


@bot.command(name='updatecp', aliases=['updateCP'])
async def updatecp(context, val, reason=''):
    user_id = context.author.id
    _update_cp(user_id, int(val))
    remaining_cp = cpdata.find_one({'_id': user_id})['cp']
    await context.send('''
**User**: {0}
**Reason**: {1}
**CP**: {2}
**CP Remaining**: {3}
    '''.format(context.author.mention, reason, val, remaining_cp))


# @bot.command(name='checktimezone', aliases=['checktz'])
# async def checktimezone(context):
#     tz = get_timezone(context)
#     await context.send('{0}, your timezone is currently set as {1}.'.format(context.author.mention, tz))


# @bot.command(name='settimezone', aliases=['settz'])
# async def settimezone(context, tz):
#     if not is_valid_timezone(tz):
#         await context.send(INVALID_TIMEZONE_MESSAGE)
#         return
#     else:
#         tz_offset = datetime.datetime.now(pytz.timezone(tz)).strftime('%z')
#         if timezone.find_one({'_id': context.author.id}):
#             timezone.update_one({'_id': context.author.id}, {'$set': {'tz': tz_offset}})
#         else:
#             post = {'_id': context.author.id, 'tz': tz}
#             timezone.insert_one(post)
#         await context.send('{0}, your timezone has been successfully updated to {1} ({2}).'.format(context.author.mention, tz, tz_offset))


# Press the green button in the gutter to run the script.
bot.add_cog(WordCountCPUpdater(bot))
bot.run(token)
