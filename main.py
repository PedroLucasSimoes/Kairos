from logging import PlaceHolder
#from discord_components.interaction import Interaction
import disnake
from disnake.ext import commands
from disnake.ext.commands import has_permissions, Param
from discord.ext.forms import Form, ReactionForm, ReactionMenu

import sys

from disnake.utils import get
sys.path.append("E:\\Desktop\\coding\\python\\Kairos\\utils")

#utils
import connection
import varHolder

import os
import json
import importlib
import random as r


prefix = "?"
bot = commands.Bot(command_prefix=prefix, test_guilds=[845277114559365160], sync_commands=True, reload=True)#Criação do objeto bot

utils = [connection]


#Simplesmente não funcionou. Não consegui achar o problema.
#async def getCogs(rpg, type):
#	if type == False:
#		for filename in os.listdir(f"./cogs/rpg_{rpg}"):
#			if filename.endswith(".py"):
#				bot.load_extension(f"cogs.rpg_{rpg}.{filename[:-3]}")
#				print(f"{filename} Initialized")
#	elif type == True:
#		for filename in os.listdir(f"./cogs/rpg_{rpg}"):
#			if filename.endswith(".py"):
#				bot.reload_extension(f"cogs.rpg_{rpg}.{filename[:-3]}")
#				print(f"{filename} Initialized")



	
@bot.event #Evento "on_ready", é executado quando o bot está devidamente inicializado.
async def on_ready():
	global server
	print(f'We have logged in as {bot.user}')
	for filename in os.listdir("./cogs/rpg_1"):
		if filename.endswith(".py"):
			bot.load_extension(f"cogs.rpg_1.{filename[:-3]}")
			print(f"{filename} Initialized")
		server = "1962"


class Dropdown(disnake.ui.Select):
	def __init__(self):
		selectOptions = [
			disnake.SelectOption(label="1962", description="RPG da Manu. Preciso falar mais?"),
			disnake.SelectOption(label="Ceia de Sangue", description="RPG do Fabricio. Preciso falar mais?"),
			disnake.SelectOption(label="embed", description="vai chamar um embed. ou deveria.")
		]
		super().__init__(placeholder="RPG's", min_values=1, max_values=1, options=selectOptions)

	async def callback(self, interaction: disnake.Interaction):
		global server
		server = self.values[0]

		if self.values[0] == "1962":
			for filename in os.listdir("./cogs/rpg_1"):
				if filename.endswith(".py"):
					bot.load_extension(f"cogs.rpg_1.{filename[:-3]}")
					print(f"{filename} Initialized \n\n")
			await interaction.response.send_message("Todos os arquivos de 1962 foram inicializados.", ephemeral=True)
		elif self.values[0] == "Ceia de Sangue":
			for filename in os.listdir("./cogs/rpg_2"):
				if filename.endswith(".py"):
					bot.load_extension(f"cogs.rpg_2.{filename[:-3]}")
					print(f"{filename} Initialized \n\n")
			await interaction.response.send_message("Todos os arquivos de Ceia de Sangue foram inicializados.", ephemeral=True)
		elif self.values[0] == "embed":
			embedVar = disnake.Embed(title="Embed lol", description="Um embed. Preciso falar mais?")
			await interaction.response.send_message(embed=embedVar, ephemeral=True)
		else:
			print("Initalizing Error.")

class DropdownView(disnake.ui.View):
	def __init__(self):
		super().__init__()
		self.add_item(Dropdown())



@bot.slash_command(name="login")
async def login(inter: disnake.ApplicationCommandInteraction,
 server: str = Param(desc="Digite o servidor")
 ):
	view = DropdownView()
	await inter.response.send_message("Selecione o RPG", view=view, ephemeral=True)

@login.autocomplete("server")
async def server_autocomp(inter : disnake.ApplicationCommandInteraction, string : str ):
	string = string.lower()
	return [serv for serv in varHolder.servers if string in serv.lower()]

def isMe(ctx):
	if ctx.author.id == 525733920633913344:
		return True
	else:
		return False

@bot.command(name= "reload", hidden=True)
@commands.check(isMe)
async def reload(ctx):
	await ctx.message.delete()
	for i in utils:
		importlib.reload(i)

	connection.closeConn()

	if server == "1962":
		for filename in os.listdir("./cogs/rpg_1"):
			if filename.endswith(".py"):
				bot.reload_extension(f"cogs.rpg_1.{filename[:-3]}")
				print(f"{filename} Reloaded \n")
	elif server == "Ceia de Sangue":
		for filename in os.listdir("./cogs/rpg_2"):
			if filename.endswith(".py"):
				bot.reload_extension(f"cogs.rpg_2.{filename[:-3]}")
				print(f"{filename} Reloaded \n")
	


with open("token.json") as file:
	data = json.load(file)["token"]

bot.run(data)

