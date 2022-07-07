import discord
from discord.ext import commands
import asyncio


class AutoResponse(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
		self.gamerec_chid=737955923158368277
		self.map_chid=769188270247510067
		self.meme_chid=816180444227436574
		self.art_chid=992054563064533075
		self.selfrole_chid==994495593856651334
		self.homi_roledict=={'bs':992616272640618526,'coc':992616363971596370,'cr':992616443361378304,'mc':992616012841222144}


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
		elif message.channel.id==self.art_chid:
			if message.attachments:
					em1=self.bot.get_emoji(992071130196217856)
					em2=self.bot.get_emoji(992071541317718076)
					em3=self.bot.get_emoji(992071620057374760)
					await message.add_reaction(em1)
					await asyncio.sleep(0.8)
					await message.add_reaction(em2)
					await asyncio.sleep(0.8)
					await message.add_reaction(em3)
			else:
				await message.delete()	
			
	@commands.Cog.listener()
	async def on_raw_reaction_add(self,payload):
		role_emote={994510214109859860:'bs',994510217716961380:'coc',994510643677900810:'cr',994510207390580757:'mc'}
		if payload.channel_id==self.selfrole_chid:
			for i in role_emote:
				if payload.emoji.id==i:
					payload.member.add_role(homi_roledict[role_emote[i]])

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self,payload):
		role_emote={994510214109859860:'bs',994510217716961380:'coc',994510643677900810:'cr',994510207390580757:'mc'}
		if payload.channel_id==self.selfrole_chid:
			for i in role_emote:
				if payload.emoji.id==i:
					payload.member.remove_role(homi_roledict[role_emote[i]])

	


