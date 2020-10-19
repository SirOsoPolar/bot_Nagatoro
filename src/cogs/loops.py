import discord 
from discord.ext import commands,tasks
import os
from itertools import cycle

status = cycle(['ヘ(^_^ヘ)',' (ノ^_^)ノ'])
class Loops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.change_status.start()     
    @tasks.loop(seconds=60)
    async def change_status(self):
        print("Otro minuto")
             
def setup(bot):
    bot.add_cog(Loops(bot))    