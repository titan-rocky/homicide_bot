import discord



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

