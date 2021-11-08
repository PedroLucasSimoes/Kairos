import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from discord.ext.forms import Form, ReactionForm, ReactionMenu
import sys
import sqlite3
import traceback
sys.path.append("E:\\Desktop\\coding\\python\\Kairos\\utils")
from connection import connect

    

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
        global db, cur
        db, cur = connect()
        
        #id = 16
        #variable = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48"]
        #cur.execute("INSERT INTO users VALUES ('"+str(id)+"'  ,'"+variable[0]+"', '"+variable[1]+"', '"+variable[2]+"', '"+variable[3]+"', '"+variable[4]+"', '"+variable[5]+"', '"+variable[6]+"', '"+variable[7]+"', '"+variable[8]+"', '"+variable[9]+"', '"+variable[10]+"', '"+variable[11]+"', '"+variable[12]+"', '"+variable[13]+"', '"+variable[14]+"', '"+variable[15]+"', '"+variable[16]+"', '"+variable[17]+"', '"+variable[18]+"', '"+variable[19]+"', '"+variable[20]+"', '"+variable[21]+"', '"+variable[22]+"', '"+variable[23]+"', '"+variable[24]+"', '"+variable[25]+"', '"+variable[26]+"', '"+variable[27]+"', '"+variable[28]+"', '"+variable[29]+"', '"+variable[30]+"', '"+variable[31]+"', '"+variable[32]+"', '"+variable[33]+"', '"+variable[34]+"', '"+variable[35]+"', '"+variable[36]+"', '"+variable[37]+"', '"+variable[38]+"', '"+variable[39]+"', '"+variable[40]+"', '"+variable[41]+"', '"+variable[42]+"', '"+variable[43]+"', '"+variable[44]+"', '"+variable[45]+"', '"+variable[46]+"', '"+variable[47]+"', '"+variable[2]+"', '"+variable[3]+"')")
        #db.commit()

    

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Register Initialized')

    def create(self, id, data):
        cur.execute("INSERT INTO users VALUES ('"+str(id)+"'  ,'"+data[0]+"', '"+data[1]+"', '"+data[2]+"', '"+data[3]+"', '"+data[4]+"', '"+data[5]+"', '"+data[6]+"', '"+data[7]+"', '"+data[8]+"', '"+data[9]+"', '"+data[10]+"', '"+data[11]+"', '"+data[12]+"', '"+data[13]+"', '"+data[14]+"', '"+data[15]+"', '"+data[16]+"', '"+data[17]+"', '"+data[18]+"', '"+data[19]+"', '"+data[20]+"', '"+data[21]+"', '"+data[22]+"', '"+data[23]+"', '"+data[24]+"', '"+data[25]+"', '"+data[26]+"', '"+data[27]+"', '"+data[28]+"', '"+data[29]+"', '"+data[30]+"', '"+data[31]+"', '"+data[32]+"', '"+data[33]+"', '"+data[34]+"', '"+data[35]+"', '"+data[36]+"', '"+data[37]+"', '"+data[38]+"', '"+data[39]+"', '"+data[40]+"', '"+data[41]+"', '"+data[42]+"', '"+data[43]+"', '"+data[44]+"', '"+data[45]+"', '"+data[46]+"', '"+data[47]+"')")
        db.commit()
        
        #cur.execute("INSERT INTO users VALUES ('"+str(id)+"'  ,'"+variable[0]+"', '"+variable[1]+"', '"+variable[2]+"', '"+variable[3]+"', '"+variable[4]+"', '"+variable[5]+"', '"+variable[6]+"', '"+variable[7]+"', '"+variable[8]+"', '"+variable[9]+"', '"+variable[10]+"', '"+variable[11]+"', '"+variable[12]+"', '"+variable[13]+"', '"+variable[14]+"', '"+variable[15]+"', '"+variable[16]+"', '"+variable[17]+"', '"+variable[18]+"', '"+variable[19]+"', '"+variable[20]+"', '"+variable[21]+"', '"+variable[22]+"', '"+variable[23]+"', '"+variable[24]+"', '"+variable[25]+"', '"+variable[26]+"', '"+variable[27]+"', '"+variable[28]+"', '"+variable[29]+"', '"+variable[30]+"', '"+variable[31]+"', '"+variable[32]+"', '"+variable[33]+"', '"+variable[34]+"', '"+variable[35]+"', '"+variable[36]+"', '"+variable[37]+"', '"+variable[38]+"', '"+variable[39]+"', '"+variable[40]+"', '"+variable[41]+"', '"+variable[42]+"', '"+variable[43]+"', '"+variable[44]+"', '"+variable[45]+"', '"+variable[46]+"', '"+variable[47]+"')")


    @commands.command(name="register", description="Use este comando para registrar seus dados no sistema.")
    async def register(self, ctx):

        #Setting up the FORM
        form = Form(ctx, "Registro Geral de Personagem")
        
        form.add_cancelkeyword("cancelar"); form.add_cancelkeyword("cancel")
        
        form.edit_and_delete(True)
        form.set_timeout(600)
        await form.set_color("0x4521F9")
        
        for i in atributos:
            form.add_question(f"**Digite o(a):** __{i}__", i.lower())
        
        #form.add_question("Nome", "nome")
        #form.add_question("Idade", "idade") #Used while debugging. 
        #form.add_question("CPF", "cpf")
        
        result = await form.start()

        if result:
            result = result.__dict__
            result = result.values()
            result = list(result)
            try:
                print(int(ctx.author.id))
                print(result)
                self.create(ctx.author.id, result)

            except Exception as e:
                print(e)
                traceback.print_exc()
        else:
            print("Error receiving data")
        
        

def setup(bot):
    bot.add_cog(Register(bot))
    
