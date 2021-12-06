from logging import StringTemplateStyle
import traceback
import disnake
from disnake import user
from disnake.colour import Colour
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
            else: return False

    async def answeringInter(self, inter: disnake.ApplicationCommandInteraction, data : int, hasExtra: bool, extra = 0, diceLimit : int = 6):
        self.Purple = disnake.Colour(0x4521F9)
        if not hasExtra:
            if self.rollCheck(extra, data, diceLimit):
                embedVar = disnake.Embed(title=f"Teste de {self.atrOld}", description=f"Sucesso <- {self.result} = {self.resultList}", colour=self.Purple)
            else:
                embedVar = disnake.Embed(title=f"Teste de {self.atrOld}", description=f"Falha <- {self.result} = {self.resultList}", colour=self.Purple)
        elif hasExtra:
            if self.rollCheck(extra, data):
                embedVar = disnake.Embed(title=f"Teste de {self.atrOld}", description=f"Sucesso <- {self.result} = {self.resultList} + {extra}", colour=self.Purple)
            else:
                embedVar = disnake.Embed(title=f"Teste de {self.atrOld}", description=f"Falha <- {self.result} = {self.resultList} + {extra}", colour=self.Purple)
        embedVar.set_author(name= self.userRolled.name,icon_url= self.userRolled.avatar.url)
        await inter.response.send_message(embed=embedVar, delete_after=600)

    @commands.slash_command(name="roll", description="Rolagem de testes")
    async def roll (self, inter: disnake.ApplicationCommandInteraction,
    atributo: str = Param(desc="Atributo a ser rolado"),
    extra : int = Param(desc="Valor extra a ser adicionado", default=0),
    usúario : disnake.Member = Param(default=0)):
        
        
        if usúario == 0:
            self.userRolled: disnake.Member = inter.author
        else:
            self.userRolled : disnake.Member = usúario
        

        if self.isValidAtr(atributo):
            self.atrNew, self.atrOld = atributo.strip().replace(" ", "_"), atributo
            try:
                self.cur.execute(f"SELECT {self.atrNew} FROM users WHERE id = ?", (str(self.userRolled.id),))
                data = self.cur.fetchall()[0][0]
            except IndexError:
                embedVar = disnake.Embed(title=f"O usúario {self.userRolled.name} não está cadastrado.", description="Caso ache que isso seja um erro, contate Farrys.")
                embedVar.set_author(name=self.userRolled.name, icon_url=self.userRolled.avatar.url)
                await inter.response.send_message(embed=embedVar)
            except Exception as e:
                traceback.print_exc()
                embedVar = disnake.Embed(title="Ocorreu um erro", description="Se o erro persistir, contate Farrys.")
                await inter.response.send_message(embed=embedVar, ephemeral=True)
            else:
                if self.atrOld != "Sanidade":
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

    @roll.autocomplete("atributo")
    async def roll_autocomp(self, inter, string : str):
        string = string.title()
        return [atr for atr in varHolder.rollToAutocomp if string in atr.title()]

def setup(bot):
    bot.add_cog(Roll(bot))