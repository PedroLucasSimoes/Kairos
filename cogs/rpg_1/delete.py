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
        self.db, self.cur = connect("1962")

    @commands.slash_command(name="delete", description="Deleta todos seus dados")
    async def delete(self, inter: disnake.ApplicationCommandInteraction):

        try:
            self.cur.execute(f"DELETE FROM users WHERE id = ?", (str(inter.author.id),))
            self.db.commit()
        except:
            embedVar = disnake.Embed(title="Dados não encontrados", description="Caso ache que isso seja um erro, entre em contato com Farrys.",  colour=disnake.Colour(value=0x4521F9))
            await inter.response.send_message(embed=embedVar, ephemeral=True)
        else:
            embedVar = disnake.Embed(title="Dados apagados com sucesso.", description="Essa ação é irreversível, espero que tenha noção do que fez.")


def setup(bot):
    bot.add_cog(Delete(bot))