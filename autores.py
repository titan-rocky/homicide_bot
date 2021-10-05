import discord
from discord.ext import commands
import asyncio


class AutoResponse(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
		self.gamerec_chid=737955923158368277
		self.map_chid=769188270247510067


	@commands.Cog.listener()
	async def on_message(self,message):
		#game-records
		if message.channel.id==self.gamerec_chid:
			for i in ['record!','record !']:
				if message.content.lower().startswith(i):
					em1=self.bot.get_emoji(894654840184127518)
					em2=self.bot.get_emoji(894641763417981029)
					em3=self.bot.get_emoji(894641763640307732)
					await message.add_reaction(em1)
					await message.add_reaction(em2)
					await message.add_reaction(em3)
					break
			else:
				await message.delete()	
		#created-maps
		elif message.channel.id==self.map_chid:
			for i in ['new map!','new map !']:
				if message.content.lower().startswith(i):
					em1=self.bot.get_emoji(894641763417981029)
					em2=self.bot.get_emoji(894641763640307732)
					await message.add_reaction(em1)
					await message.add_reaction(em2)
					break
			else:
				await message.delete()	

