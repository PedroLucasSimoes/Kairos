from logging import PlaceHolder
#from discord_components.interaction import Interaction
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from discord.ext.forms import Form, ReactionForm, ReactionMenu

import sys
import os
import json
import random as r


prefix = "?"
bot = commands.Bot(command_prefix=prefix)#Criação do objeto bot
	
@bot.event #Evento "on_ready", é executado quando o bot está devidamente inicializado.
async def on_ready():
	global server
	print(f'We have logged in as {bot.user}')
	for filename in os.listdir("./cogs/rpg_1"):
			if filename.endswith(".py"):
				bot.load_extension(f"cogs.rpg_1.{filename[:-3]}")
				print(f"{filename} Initialized")
			server = "1962"


class Dropdown(nextcord.ui.Select):
	def __init__(self):
		selectOptions = [
			nextcord.SelectOption(label="1962", description="RPG da Manu. Preciso falar mais?"),
			nextcord.SelectOption(label="Ceia de Sangue", description="RPG do Fabricio. Preciso falar mais?"),
			nextcord.SelectOption(label="embed", description="vai chamar um embed. ou deveria.")
		]
		super().__init__(placeholder="RPG's", min_values=1, max_values=1, options=selectOptions)

	async def callback(self, interaction: nextcord.Interaction):
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
			embedVar = nextcord.Embed(title="Embed lol", description="Um embed. Preciso falar mais?")
			await interaction.response.send_message(embed=embedVar, ephemeral=True)
		else:
			print("Initalizing Error.")

class DropdownView(nextcord.ui.View):
	def __init__(self):
		super().__init__()
		self.add_item(Dropdown())

@bot.command(name="Login", hidden=True)
async def login(ctx):
	view = DropdownView()
	await ctx.send("Selecione o RPG", view=view)

def isMe(ctx):
	if ctx.author.id == 525733920633913344:
		return True
	else:
		return False

@bot.command(name= "reload", hidden=True)
@commands.check(isMe)
async def reload(ctx):
	if server == "1962":
		for filename in os.listdir("./cogs/rpg_1"):
			if filename.endswith(".py"):
				bot.reload_extension(f"cogs.rpg_1.{filename[:-3]}")
				print(f"{filename} Reloaded \n\n")
	elif server == "Ceia de Sangue":
		for filename in os.listdir("./cogs/rpg_2"):
			if filename.endswith(".py"):
				bot.reload_extension(f"cogs.rpg_2.{filename[:-3]}")
				print(f"{filename} Reloaded \n\n")


with open("token.json") as file:
	data = json.load(file)["token"]

bot.run(data)

