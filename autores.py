import discord
from discord.ext import commands
import asyncio


class AutoResponse(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
		self.gamerec_chid=737955923158368277
		self.map_chid=769188270247510067
		self.meme_chid=816180444227436574


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
					await asyncio.sleep(0.8)
					await message.add_reaction(em2)
					await asyncio.sleep(0.8)
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
					await asyncio.sleep(0.8)
					await message.add_reaction(em2)
					break
			else:
				await message.delete()

		elif message.channel.id==self.meme_chid:
			print(message.attachments)
			if message.attachments:
					em1=self.bot.get_emoji(698824614964363264)
					em2=self.bot.get_emoji(739354948424302658)
					await message.add_reaction(em1)
					await asyncio.sleep(0.8)
					await message.add_reaction(em2)
			else:
				await message.delete()	

