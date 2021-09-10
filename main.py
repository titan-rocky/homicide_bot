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

cl=discord.client.Client()


@cl.event
async def on_ready():
	print('I am Ready')
	await cl.change_presence(status=discord.Status.idle,activity=discord.Streaming(name="Black Flames",platform='twitch',url='https://www.twitch.tv/titan_rocky',details='The Black Flames',assets={'large_image':'877557270177808394','large_text':'sdghsdh'}))
	#await cl.change_presence(activity=discord.Streaming(name="Black Flames",url='https://www.twitch.tv/titan_rocky')
	cl.loop.create_task(club_entry())
	cl.loop.create_task(role_update())



@cl.event
async def on_message(message):

	if message.content.startswith('$hi'):
		print(f'$hi by {message.author.name}#{message.author.discriminator} id {message.author.id}')
		if str(message.author.id)=='557914347490508806':
			await message.channel.send('Hello m\'Boss')
		elif str(message.author.id)=='7386528323409019396':
			await message.channel.send('Hello Guardian')
		elif str(message.author.id)=='709740580988780624':
			await message.channel.send('Hello Guardian')	
		else:
			await message.channel.send(f'Hello ,{message.author.name} ')

	if message.content.startswith('$addid'):
    	print(f'$addid requested by {message.author.name}#{message.author.discriminator} id {message.author.id}')
		if message.author.id in op_discord_id:
			b=message.content
			b=b.lstrip('$addid ').strip()
			if len(b)>2:
				await message.channel.send(f'{message.author.mention} , you can add only one entry')
			elif len(b)!=2:
				await message.channel.send(f'{message.author.mention} , Please give any entry')
			elif len(b)==2:

				def check(m):
					return m.content=='confirm' and m.channel==message.channel

				try:
					msg=cl.wait_for('message',check=check,timeout=30)
				except asyncio.TimeoutError:
					await message.channel.send(f'{message.author.mention} Your Request has been declined')
				else:
					print(f'added {b[0]}:{b[1]} disbs.csv')
					disbsint.add_entry(b[0],b[1])







def header():
	bs_APIKEY=os.environ['BRAWL_API_KEY']
	m={'Accept':'application/json','authorization':f'Bearer {bs_APIKEY}'}
	return m



@cl.event
async def role_update():
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


@cl.event
async def club_entry():

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




keep_alive()
cl.run(os.environ['DISCORD_TOKEN'])
