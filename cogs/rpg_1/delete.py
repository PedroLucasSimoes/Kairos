from logging import StringTemplateStyle
import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions, Param
from discord.ext.forms import Form, ReactionForm, ReactionMenu
import sqlite3
import sys
import time
sys.path.append("E:\\Desktop\\coding\\python\\Kairos\\utils")
from connection import connect
import varHolder

from disnake.ext.commands.core import command
from pprint import pprint

class Delete(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.db, self.cur = connect()



def setup(bot):
    bot.add_cog(Delete(bot))