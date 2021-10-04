import discord
from discord.ext import commands
import asyncio


class AutoResponse(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
		self.gamerec_ch=self.bot.get_channel(737955923158368277)
		self.map_ch=self.bot.get_channel(737955923158368277)


	@commands.Cog.listener()
	async def on_message(message):
		#game-records
		if message.channel==self.gamerec_ch:
			for i in ['new map!','new map !']:
				if message.content.lower().startswith(i):
					em1=discord.Partialemoji()
					await message.add_reaction(em1.from_str('<a:upvote:894641763417981029>'))
			else:
				await message.delete()	
		#created-maps
		elif message.channel=self.map_ch:
			pass


