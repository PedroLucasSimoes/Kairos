import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from discord.ext.forms import Form, ReactionForm, ReactionMenu
import time
import os
import sqlite3

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(Info(bot))