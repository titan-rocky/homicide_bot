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


token=os.environ['DISCORD_TOKEN']

cl=discord.client.Client()


@cl.event
async def on_ready():
	print('I am Ready')
	await cl.change_presence(status=discord.Status.idle,activity=discord.Streaming(name="Black Flames",platform='twitch',url='https://www.twitch.tv/titan_rocky',details='The Black Flames',assets={'large_image':'877557270177808394','large_text':'sdghsdh'}))
	#await cl.change_presence(activity=discord.Streaming(name="Black Flames",url='https://www.twitch.tv/titan_rocky')
	cl.loop.create_task(club_entry())
	cl.loop.create_task(role_update())




@cl.event
async def role_update():
	m={'Accept':'application/json','authorization':'Bearer m20'}

	b=requests.get(r'https://api.brawlstars.com/v1/clubs/%23202U9UPLU/members',headers=m) # %23 - js '#'

	dic=b.json()
	print(dic)
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
		
		m={'Accept':'application/json','authorization':'Bearer m20'}

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
cl.run(token)
