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

class Modify(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db, self.cur = connect()

    def isValidAtr(self, atr):
        if atr in varHolder.atributos:
            return True
        else:
            return False

    @commands.slash_command(name="modify")
    async def info(self, inter: disnake.ApplicationCommandInteraction, 
    atributo: str = Param(desc="Atributo a ser modificado."),
    valor: str = Param(desc="Novo valor para o atributo")):

        if self.isValidAtr(atributo):
            try:
                self.cur.execute(f"SELECT {atributo} FROM users WHERE id=?", (str(inter.author.id),))
                data = self.cur.fetchall()[0]
            except:
                embedVar = disnake.Embed(title="Dados não encontrados", description="Caso ache que isso seja um erro, entre em contato com Farrys.",  colour=disnake.Colour(value=0x4521F9))
                await inter.response.send_message(embed=embedVar, ephemeral=True)
            else:
                op = list(valor)[0]
                if op in ["+", "-"]:
                    if op == "+":
                        self.valFinal = str( int(valor.replace("+", "")) + int(data[0]) )
                    elif op == "-":
                        print(f"Valor: {valor} Data: {data[0]}")
                        self.valFinal = str(int(data[0]) - int(valor.replace("-", "")) )
                        print(f"Valor Final: {self.valFinal}")
                else:
                    self.valFinal = valor
        
                try:
                    self.cur.execute(f"UPDATE users SET {atributo} = {self.valFinal} WHERE id = ?", (str(inter.author.id),))
                    self.db.commit()
                except:
                    embedVar = disnake.Embed(title="Ocorreu um erro", description="Se o erro persistir, contate Farrys.")
                    await inter.response.send_message(embed=embedVar, ephemeral=True)
                else:
                    embedVar = disnake.Embed(title=f"Modificando o atributo {atributo}", description=f"Valor Antigo: {data[0]} / Valor Novo: {self.valFinal}")
                    await inter.response.send_message(embed=embedVar, ephemeral=True)
        else:
            embedVar = disnake.Embed(title="Atributo inválido.", description="Verifique se digitou o atributo corretamente.")
            await inter.response.send_message(embed=embedVar, ephemeral=True)

    @info.autocomplete("atributo")
    async def modify_autocomp(self, inter, string : str):
        self.atrToAutocomp = ["Vida", "Sanidade", "Força", "Escalar", "Furtividade", "Salto"]
        return [atr for atr in self.atrToAutocomp if string in atr.capitalize()]

def setup(bot):
    bot.add_cog(Modify(bot))