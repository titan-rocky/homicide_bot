import discord
import discord.ext.commands
import asyncio
import tracemalloc
tracemalloc.start()
import os

import requests
import json

import csv
from alive import keep_alive
import disbsint


op_discord_id=['557914347490508806','709740580988780624']

bs_APIKEY=os.environ['BRAWL_API_KEY']

cl=commands.bot(command_prefix='belle ',description='Dedicated for HOMICIDE_CREW')


@cl.event
async def on_ready():
	print('I am Ready')
	await cl.change_presence(status=discord.Status.idle,activity=discord.Streaming(name="Shockers with Positive Feedback",platform='twitch',url='https://www.twitch.tv/titan_rocky',details='Shockers with Positive Feedback',assets={'large_image':'877557270177808394','large_text':'sdghsdh'}))
	#await cl.change_presence(activity=discord.Streaming(name="Black Flames",url='https://www.twitch.tv/titan_rocky')
	cl.loop.create_task(club_entry())
	cl.loop.create_task(role_update())

def header():
	bs_APIKEY=os.environ['BRAWL_API_KEY']
	m={'Accept':'application/json','authorization':f'Bearer {bs_APIKEY}'}
	return m

@cl.event
async def role_update():
	print('role_update() called')
	b=requests.get(r'https://api.brawlstars.com/v1/clubs/%23202U9UPLU/members',headers=header()) # %23 - js '#
	dic=b.json()
	if 'reason' in dic and dic['reason']=='accessDenied.invalidIp':
		 print('Access Denied , Invalid IP')
	else:
		lis=dic['items']
		file=open('abc.csv','w',newline='',encoding='UTF-32')
		e=csv.writer(file,delimiter=',',quotechar='\u01C0', quoting=csv.QUOTE_MINIMAL)
		head=['TAG','NAME','ROLE','TROPHIES']#;head=[i.encode() for i in head]
		e.writerow(head)
		for i in lis:
			data=[i['tag'],i['name'],i['role'],i['trophies']]#;data=[f'{i}'.encode() for i in data]
			e.writerow(data)
		file.close()

		roles={'member':699145204082671677,'senior':691477643387863131,'vicePresident':691475835835645955,'president':691476710524321833}

	await asyncio.sleep(60)

@cl.event
async def club_entry():
	print('club_entry() called')
	mo={}
	while 0:
		
		m={'Accept':'application/json','authorization':f'Bearer {bs_APIKEY}'}

		b=requests.get(r'https://api.brawlstars.com/v1/clubs/%23202U9UPLU/members',headers=m) # %23 - js '#'

		dic=b.json()

		if mo==dic:
			print('No Entries')
		elif len(mo)==0:
			pass
		else:
			print(mo['items'])
			cde=[i for i in mo['items'] if i not in dic['items']]
			print(cde)
			await cl.get_channel(877773803252486145).send(cde)

			a1=[len(dic['items']) if len(mo)!=0 else 0][0]
			a2=[len(mo['items']) if len(mo)!=0 else 0][0]
			count=a2-a1
			print(count)
			await cl.get_channel(877773803252486145).send(f'{count} Entries , Total : {a2} Members ')

			if count<-5:
				print('Alert')
				await cl.get_channel(691292302580121693).send('@everyone : Alert ! Many are Leaving the Club , Beware of mass Kickouts ! ')


		mo=dic

		await asyncio.sleep(60)




@cl.event
async def on_message(message):
	if message.author==bot.user:
		return

	bot.process_commands(message)

	# $hi command
	# $addit command - discord_brawl stars id integration
	# $help - help embed
		
@bot.command()
async def hi():
	print(f'$hi by {ctx.author.name}#{ctx.author.discriminator} id {ctx.author.id}')
	if str(ctx.author.id)=='557914347490508806':
		await ctx.channel.send('Hello m\'Boss')
	elif str(ctx.author.id)=='738652832340901939':
		await ctx.channel.send('A Warm Welcome , Lord Guardian')
	elif str(ctx.author.id)=='709740580988780624':
		await ctx.channel.send('Hello Guardian')	
	else:
		await message.channel.send(f'Hello ,{message.author.name} ')


@bot.command()
async def addit():
	print(f'$addid requested by {ctx.author.name}#{ctx.author.discriminator} id {ctx.author.id}')
	if str(ctx.author.id) in op_discord_id:
		b=ctx.message.content
		b=b.split(' ')
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
				msg=await cl.wait_for('ctx',check=check,timeout=30)
			except asyncio.TimeoutError:
				await ctx.channel.send(f'{ctx.author.mention} Your Request has been declined')
			else:
				disbsint.add_entry(b[0],b[1])
				print(f'added {b[0]}:{b[1]} disbs.csv')
				await ctx.channel.send(f'Added ID {b[0]} successfully !')
	else:
		await ctx.channel.send('You are not Authorized 😓')




keep_alive()
cl.run(os.environ['DISCORD_TOKEN'])
