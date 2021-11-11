import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions
from discord.ext.forms import Form, ReactionForm, ReactionMenu
import sqlite3
import sys
sys.path.append("E:\\Desktop\\coding\\python\\Kairos\\utils")
from connection import connect

from disnake.ext.commands.core import command
from pprint import pprint

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        global db, cur
        db, cur = connect()
        
        #cur.execute("SELECT * FROM users")
        #data = cur.fetchall()
        #pprint(data)

    @commands.command(name="info")
    async def info(self, ctx):
        cur.execute("SELECT * FROM users WHERE id =?", (str(ctx.author.id),))
        print(cur.fetchall())
        data = cur.fetchall()
        pprint(data)

        embedVar =  
        




def setup(bot):
    bot.add_cog(Info(bot))