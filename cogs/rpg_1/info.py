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

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        global db, cur
        db, cur = connect()
        
        #cur.execute("SELECT * FROM users")
        #data = cur.fetchall()
        #pprint(data)

    def getColor(self, value : int):
        return disnake.Colour(value=value)

    def getEmbed(self, data):
        embedVar =  disnake.Embed(title=f"{data[1]}", description=f"{data[2]} anos", colour=self.getColor(0x4521F9))
        embedVar.add_field(name="Vida", value=f"{data[3]}/{data[49]}", inline=True)
        embedVar.add_field(name="Sanidade", value=f"{data[4]}/{data[50]}", inline=True)
        return embedVar

    def createPage(self, data, embed: disnake.Embed, start: int, finish: int):
        
        for i in varHolder.atributos[start:finish]:
            print(f"{i}:{str(int(data[varHolder.atributos.index(i)]) + 1)}")
            embed.add_field(name=i, value=str(int(data[varHolder.atributos.index(i)]) + 1), inline=True)
        return embed


    @commands.slash_command(name="info")
    async def info(self, inter, 
    página: int = Param(desc="Selecione a página", min_value=0, max_value=4)
    ):
        try:
            cur.execute("SELECT * FROM users WHERE id =?", (str(inter.author.id),))
            data = cur.fetchall()[0]
        except:
            embedVar = disnake.Embed(title="Dados não encontrados", description="Caso ache que isso seja um erro, entre em contato com Farrys.")
            await inter.response.send_message(embed=embedVar)
        
        #pprint(data)

        embedVar = self.getEmbed(data)
        if página == 1:
            self.createPage(data, embedVar, 4, 20)
        elif página == 2:
            self.createPage(data, embedVar, 20, 38)
        elif página == 3:
            self.createPage(data, embedVar, 40,  48) 
        if página in [1, 2, 3]:
            await inter.response.send_message(embed=embedVar, ephemeral=True)
        else:
            await inter.response.send_message("Esta página não existe.", ephemeral=True)

    @info.autocomplete("página")
    async def info_autocomp(self, inter, string : str):
        pages = [1, 2, 3]
        string = str(string).lower()
        return [page for page in pages if string in str(page).lower()]


def setup(bot):
    bot.add_cog(Info(bot))