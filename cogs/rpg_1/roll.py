from logging import StringTemplateStyle
import traceback
import disnake
from disnake import user
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
import random as r

class Roll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db, self.cur = connect()
    
    def isValidAtr(self, atr):
        if atr in varHolder.atributos: return True
        else: return False

    def diceRolling(self, diceAmount: int, diceLimit: int):
        result = 0
        for i in range(1, diceAmount):
            result += r.randint(1, diceLimit)
        return result

    def rollCheck(self, atr, diceLimit: int = 6):
        self.result = self.diceRolling(3, diceLimit)
        if self.result in [3,4]:
            return True
        elif self.result in [17, 18]:
            return False
        else:
            if self.result < atr:
                return True
            else: False

    @commands.slash_command(name="roll", description="Rolagem de testes")
    async def roll (self, inter: disnake.ApplicationCommandInteraction,
    atributo: str = Param(desc="Atributo a ser rolado"),
    extra : int = Param(desc="Valor extra a ser adicionado", default=0),
    usúario : disnake.Member = Param(default=0)):
        
        if usúario == 0: userRolled: disnake.Member = inter.author

        if self.isValidAtr(atributo):
            try:
                self.cur.execute(f"SELECT {atributo} FROM users WHERE id = ?", (str(userRolled.id),))
                data = self.cur.fetchall()[0][0]
            except Exception as e:
                traceback.print_exc()
                embedVar = disnake.Embed(title="Ocorreu um erro", description="Se o erro persistir, contate Farrys.")
                await inter.response.send_message(embed=embedVar, ephemeral=True)
            else:
                if atributo != "Sanidade":
                    if self.rollCheck(int(data)):
                        await inter.response.send_message(f"Sucesso <- [{self.result}]")
                    else:
                        await inter.response.send_message(f"Falha <- [{self.result}]")
                else:
                    if self.rollCheck(int(data), 100):
                        await inter.response.send_message(f"Sucesso <- [{self.result}]")
                    else:
                        await inter.response.send_message(f"Falha <- [{self.result}]")


        else:
            embedVar = disnake.Embed(title="Atributo inválido.", description="Verifique se digitou o atributo corretamente.")
            await inter.response.send_message(embed=embedVar, ephemeral=True)

def setup(bot):
    bot.add_cog(Roll(bot))