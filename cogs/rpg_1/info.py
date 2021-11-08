import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from discord.ext.forms import Form, ReactionForm, ReactionMenu
import sqlite3
import sys
sys.path.append("E:\\Desktop\\coding\\python\\Kairos\\utils")
from connection import connect

from nextcord.ext.commands.core import command
import pprint

db, cur = connect()


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        global db, cur
        db, cur = connect()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        pprint.pprint(data)

    @commands.command
    async def info(self, ctx):
        pass
        cur.execute("SELECT * FROM users WHERE id =?", (str(ctx.user.id,)))
        data = cur.fetchall()
        




def setup(bot):
    bot.add_cog(Info(bot))