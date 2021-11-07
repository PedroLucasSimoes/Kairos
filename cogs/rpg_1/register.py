import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from discord.ext.forms import Form, ReactionForm, ReactionMenu
import time
import os
import sqlite3

    

atributos = ["Nome", "Idade", "Pontos de Vida", "Sanidade", "Força", "Destreza", "Inteligência", "Vitalidade", "Resistência",
        "Corrida", "Escalar", "Furtividade", "Salto",
        "Detectar Mentiras", "Diplomacia", "Disfarce", "Mentir", "Interrogatório", "Lábia", "Liderança",
        "Armeiro", "Química", "Camuflagem", "Estratégia", "Falsificação", "Primeiros Socorros", "Medicina", "Rastreamento",
        "Sobrevivência", "Venefício", "Encontrar", "Dirigir",
        "Acrobacia", "Arremessar", "Briga", "Sacar Rápido", "Esquiva", "Bloqueio",
        "Espingarda", "Pistola", "Metralhadora", "Armas Elétricas", "Machado", "Facas", "Espadas", "Espadas Curtas", "Bastão", "Arco"]
    

class Register(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        try:
            global cur
            db = sqlite3.connect('E:\Desktop\coding\python\qwerty\db\\1962.db')
            cur = db.cursor()
        except Exception as e:
            print(f"An error ocurred while initializing the db. Error: {e}")
        else:
            print("DB Initialized")

        try:
            pass
        except Exception as e:
            print("deu ruim")
            print(e)
        else:
            pass

    def create(id, data):
        cur.execute("INSERT INTO 1962 VALUES ('"+data[0]+"', '"+data[1]+"', '"+data[2]+"', '"+data[3]+"', '"+data[4]+"', '"+data[5]+"', '"+data[6]+"', '"+data[7]+"', '"+data[8]+"', '"+data[9]+"', '"+data[10]+"', '"+data[11]+"', '"+data[12]+"', '"+data[13]+"', '"+data[14]+"', '"+data[15]+"', '"+data[16]+"', '"+data[17]+"', '"+data[18]+"', '"+data[19]+"', '"+data[20]+"', '"+data[21]+"', '"+data[22]+"', '"+data[23]+"', '"+data[24]+"', '"+data[25]+"', '"+data[26]+"', '"+data[27]+"', '"+data[28]+"', '"+data[29]+"', '"+data[30]+"', '"+data[31]+"', '"+data[32]+"', '"+data[33]+"', '"+data[34]+"', '"+data[35]+"', '"+data[36]+"', '"+data[37]+"', '"+data[38]+"', '"+data[39]+"', '"+data[40]+"', '"+data[41]+"', '"+data[42]+"', '"+data[43]+"', '"+data[44]+"', '"+data[45]+"', '"+data[46]+"', '"+data[47]+"')")
        
        pass

    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(1)
        print(f'Register Initialized')

    @commands.command(name="register")
    async def register(self, ctx):

        #Setting up the FORM
        form = Form(ctx, "Registro Geral de Personagem")
        
        form.add_cancelkeyword("cancelar")
        form.add_cancelkeyword("cancel")
        form.edit_and_delete(True)
        form.set_timeout(600)
        await form.set_color("0x4521F9")
        
        #for i in atributos:
        #    form.add_question(f"**Digite o(a):** __{i}__", i.lower())
        
        form.add_question("Nome", "nome")
        form.add_question("Idade", "idade") #Used while debugging. 
        form.add_question("CPF", "cpf")
        
        result = await form.start()

        await result.delete()
        if result:
            result = result.__dict__
            result = result.values()
            result = list(result)
            try:
                self.create(int(ctx.author.id), result)
            except Exception as e:
                print(e)
        else:
            print("Error receiving data")
        
        

def setup(bot):
    bot.add_cog(Register(bot))
    
