import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
		self.mod_role_id=724532819166101565

	def mod_check(self,ctx:discord.commands.Context):
		b=ctx.author.role
		if b==self.mod_role_id:
			return true
		else:
			await ctx.send('You are Not Authorized Mate <a:sorry_mate:894514353762631681>')
			return false


	@commands.Cog.Listener
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
			sad_aem=await cl.get_guild(887015707366277170).fetch_emoji(887024376917139506)
			await message.add_reaction(sad_aem)
		if any(i.lower()=='amaterasu' or i.lower()=='itachi' for i in message.content.split(' ')):
			if random.randint(0,4)==3:
				await message.channel.send('<a:amaterasu:887033967264550912>')

	@commands.commands
	@commands.check(self.mod_check)
	async def purge(self,ctx:commands.Context,limit:int,*aa):
		mb=await ctx.channel.purge(limit)
		finalmessage=awaitctx.send(f'{len(mb)} messages have been removed')
		await asyncio.sleep(5)
		await finalmessage.delete()


