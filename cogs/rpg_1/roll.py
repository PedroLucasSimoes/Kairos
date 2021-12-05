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
    
    def isValidAtr(self, atr : str):
        print(f"titled:{atr.title()}")
        if atr.title() in varHolder.atributos: return True
        else: return False

    def diceRolling(self, extra, diceAmount: int, diceLimit: int):
        result = 0
        resultList = []
        for i in range(0, diceAmount):
            d6 = r.randint(1, diceLimit)
            result += d6
            resultList.append(d6)
        result += extra
        return result, resultList

    def rollCheck(self, extra, atr, diceLimit: int = 6):
        self.result, self.resultList = self.diceRolling(extra, 3, diceLimit)
        if self.result in [3,4]:
            return True
        elif self.result in [17, 18]:
            return False
        else:
            if self.result < atr:
                return True
            else: False

    async def answeringInter(self, inter: disnake.ApplicationCommandInteraction, data : int, hasExtra: bool, extra = 0, diceLimit : int = 6):
        if not hasExtra:
            if self.rollCheck(extra, data, diceLimit):
                await inter.response.send_message(f"Sucesso <- {self.result}{self.resultList}")
            else:
                await inter.response.send_message(f"Falha <- {self.result}{self.resultList}")
        elif hasExtra:
            if self.rollCheck(extra, data):
                await inter.response.send_message(f"Sucesso <- {self.result} = {self.resultList} + {extra}")
            else:
                await inter.response.send_message(f"Falha <- {self.result} = {self.resultList} + {extra}")

    @commands.slash_command(name="roll", description="Rolagem de testes")
    async def roll (self, inter: disnake.ApplicationCommandInteraction,
    atributo: str = Param(desc="Atributo a ser rolado"),
    extra : int = Param(desc="Valor extra a ser adicionado", default=0),
    usúario : disnake.Member = Param(default=0)):
        
        
        if usúario == 0:
            self.userRolled: disnake.Member = inter.author
        else:
            pass
        print(atributo)
        

        if self.isValidAtr(atributo):
            atributo = atributo.strip().replace(" ", "_")
            print(f"after:{atributo}")
            try:
                self.cur.execute(f"SELECT {atributo} FROM users WHERE id = ?", (str(self.userRolled.id),))
                data = self.cur.fetchall()[0][0]
                pprint(data)
            except Exception as e:
                traceback.print_exc()
                embedVar = disnake.Embed(title="Ocorreu um erro", description="Se o erro persistir, contate Farrys.")
                await inter.response.send_message(embed=embedVar, ephemeral=True)
            else:
                if atributo != "Sanidade":
                    if extra == 0:
                        await self.answeringInter(inter, int(data), hasExtra= False)
                    else:
                        await self.answeringInter(inter, int(data), hasExtra= True, extra= extra)
                else:
                    if extra == 0:
                        await self.answeringInter(inter, int(data), hasExtra= False, diceLimit= 100)
                    else:
                        await self.answeringInter(inter, int(data), hasExtra= True, extra= extra, diceLimit=100)

        else:
            embedVar = disnake.Embed(title="Atributo inválido.", description="Verifique se digitou o atributo corretamente.")
            await inter.response.send_message(embed=embedVar, ephemeral=True)

def setup(bot):
    bot.add_cog(Roll(bot))