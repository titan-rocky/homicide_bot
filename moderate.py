import discord
from discord.ext import commands
import asyncio
import disbsint
import random

class Moderation(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
		self.mod_role_id=724532819166101565

	def check_mod_roles(self,ctx):
		b=ctx.author.roles;b=[i.id for i in b]
		if self.mod_role_id in b:
			return True
		elif ctx.author.id==ctx.guild.owner_id:
			return True
		else:
			return False



	@commands.Cog.listener()
	async def on_message(self,message:discord.Message):
		bad_word=['sunni','fuck','fak','junni','poinda','Pointhe','Pointha','kudhi','kuthi','Tavethiya','nigga','sex','penis','vagina','pp']
		words=message.content.split(' ')
		for i in words:
			for j in bad_word:
				if i.lower()==j.lower():
					await message.delete()
					await message.channel.send(f'{message.author.mention} Dont use Explicit words Here , you pile of poop 💩 !')
		sad_words=['sadly','disappointed','sad','depressed','die','sorrow','unhappy','not feeling well']
		if any (i in message.content.split(' ') for i in sad_words):
			sad_aem=await self.bot.get_guild(887015707366277170).fetch_emoji(887024376917139506)
			await message.add_reaction(sad_aem)
		if any(i.lower()=='amaterasu' or i.lower()=='itachi' for i in message.content.split(' ')):
			if random.randint(0,4)==3:
				await message.channel.send('<a:amaterasu:887033967264550912>')


	@commands.command()
	async def purge(self,ctx:commands.Context,limit:int,*aa,description='Bulk Delete Messages'):
		'''To Delete Bulk Messages'''
		print(limit)
		if self.check_mod_roles(ctx):
			mb=await ctx.channel.purge(limit=limit+1)
			finalmessage=await ctx.send(f'{len(mb)} messages have been removed <a:success:894520030404948009>')
			await asyncio.sleep(5)
			await finalmessage.delete()
		else:
			await ctx.send(f'You dont have Permissions to Moderate Mate !')
			await ctx.send('<a:sorry_mate:894514353762631681>')

	@commands.command()
	async def addid(self,ctx,description='Discord-BS integration'):
		print(f'$addid requested by {ctx.author.name}#{ctx.author.discriminator} id {ctx.author.id}')
		if self.check_mod_roles(ctx):
			b=ctx.message.content
			b=b.lstrip('belle addid ').split(' ')
			print(b)
			if len(b)>2:
				await ctx.channel.send(f'{ctx.author.mention} , you can add only one entry')
			elif len(b)!=2:
				await ctx.channel.send(f'{ctx.author.mention} , Please give any entry')
			elif len(b)==2:
				await ctx.channel.send(f'{ctx.author.mention} , Please Confirm your request by typing \'confirm\' (case sensitive)')
				def check(m):
					return m.content=='confirm' and m.channel==ctx.channel

				try:
					msg=await self.bot.wait_for('message',check=check,timeout=30)
				except asyncio.TimeoutError:
					await ctx.channel.send(f'{ctx.author.mention} Your Request has been declined')
				else:
					disbsint.add_entry(b[0],b[1])
					print(f'added {b[0]}:{b[1]} disbs.csv')
					await ctx.channel.send(f'Added ID {b[0]} successfully !')
		else:
			await ctx.send(f'You dont have Permissions to Moderate Mate !')
			await ctx.send('<a:sorry_mate:894514353762631681>')

	

			


