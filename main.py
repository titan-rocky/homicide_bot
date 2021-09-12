import discord
from discord import Webhook,RequestsWebhookAdapter
from discord.ext import commands
import asyncio
import tracemalloc
tracemalloc.start()
import os
import random
import requests
import json
import datetime
import csv
from alive import keep_alive
import disbsint
import datetime

#important variables
op_discord_id=['557914347490508806','709740580988780624']
bs_APIKEY=os.environ['BRAWL_API_KEY']

inn=discord.Intents.all()
cl=commands.Bot(command_prefix='belle ',description='Dedicated for HOMICIDE_CREW',intents=inn)


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
	if message.author==cl.user:
		return
	bad_word=['junni','poinda','Pointhe','kudhi','kuthi','Tavethiya','nigga']
	words=message.content.split(' ')

	if isinstance(message.channel,discord.channel.DMChannel) and message.author != cl.user:
		await message.channel.send('This is a DM , commands only work on HOMICIDE_CREW server')
		return
	else:
		await cl.process_commands(message)

	# $hi command
	# $addit command - discord_brawl stars id integration
	# $help - help embed

@cl.event
async def on_member_join(member):
	now=datetime.datetime.now()
	col=[0x99b898,0xfecea8,0xff847c,0xea485f]
	url1=os.environ['memberlog_webhook_url']

	if not member.bot:
		ch=cl.get_channel(691292302580121693)  #homicide crew general chat id
		cdx=now.strftime('%d %B,%Y')
		e=discord.Embed(title='HOMICIDE:skull_crossbones:CREW',color=random.choice(col),url='https://cdn.discordapp.com/attachments/737942309173329985/737973140361183232/JPEG_20200323_145525_cropped.jpg',description='You Have joined our Discord Server ó‿ó')
		e.set_author(name='New member')
		e.add_field(name=f'Welcome to our Family ! \n{member.name}#{member.discriminator}',value='There are many features in this server, pl. do check them out \n\n*Please do read #welcome-ó‿ó for more information .*',inline=True)
		e.set_footer(text=f'Joined on {cdx} | For queries , contact the admin privately.')
		e.set_image(url='https://cdn.discordapp.com/attachments/737942309173329985/742612222429102140/Homologo.png')
		e.set_thumbnail(url='https://cdn.discordapp.com/attachments/737942309173329985/886442415219687454/maxresdefault.jpg')
		await ch.send(embed=e)
		await member.add_roles(member.guild.get_role(743120386404778058),member.guild.get_role(886455823189037106))
	else:
		return


@cl.event
async def on_command(ctx):
	url1=os.environ['commandlog_webhook_url']
	webhook = Webhook.from_url(f'{url1}',adapter=RequestsWebhookAdapter())
	col=[0xf8b195,0xf67280,0xc06c84,0x6c5b7b,0x355c7d]
	con=ctx.message.content
	con=con.lstrip(f'{cl.command_prefix}{ctx.command.name}').split(' ')
	con2=''
	for i in range (len(con)):
		if con[i]:
			con2=con2+f'arg{i+1} : {con[i]}'+'\n'
	dd=discord.Embed(color=random.choice(col),title="Command Logs",desc='ss')

	if con2:
		dd.add_field(name=f'Command : {ctx.command.name}',value=f'Arguments : \n{con2}')
	else:
		dd.add_field(name=f'Command : {ctx.command.name}',value=f'Arguments : none')
	bnow=datetime.datetime.now()
	btimestamp=bnow.strftime('%d %B,%Y - %H:%M ')
	dd.set_footer(text=f'invoked by {ctx.author.name}#{ctx.author.discriminator} on {btimestamp}')
	webhook.send(embed=dd)
	    
@cl.command()
async def hi(ctx):
	print(f'$hi by {ctx.author.name}#{ctx.author.discriminator} id {ctx.author.id}')
	if str(ctx.author.id)=='557914347490508806':
		await ctx.channel.send('A Warm Welcome, *Hon\'ble* **Lord Chief**')
	elif str(ctx.author.id)=='738652832340901939':
		await ctx.channel.send('A Warm Welcome , **The Guardian** of the **General chat**')
	elif str(ctx.author.id)=='709740580988780624':
		await ctx.channel.send('Hello, **Mod 😈**')	
	else:
		await ctx.send(f'A Warm Welcome , *Hon\'ble* **{ctx.author.name}** ')


@cl.command()
async def addid(ctx):
	print(f'$addid requested by {ctx.author.name}#{ctx.author.discriminator} id {ctx.author.id}')
	if str(ctx.author.id) in op_discord_id:
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
				msg=await cl.wait_for('message',check=check,timeout=30)
			except asyncio.TimeoutError:
				await ctx.channel.send(f'{ctx.author.mention} Your Request has been declined')
			else:
				disbsint.add_entry(b[0],b[1])
				print(f'added {b[0]}:{b[1]} disbs.csv')
				await ctx.channel.send(f'Added ID {b[0]} successfully !')
	else:
		await ctx.channel.send('You are not Authorized 😓')


@cl.command()
async def tip(ctx):
	col=[0xf8b195,0xf67280,0xc06c84,0x6c5b7b,0x355c7d]
	tiplist=[
	'**Shelly in BrawlBall :** \nwith super activated,  while shooting the ball towards walls near goal box , use your super to break walls and it goes into goal box. GOAL!!! the enemies will leave , thinking that walls will prevent the goal',
	'**Mortis in BrawlBall :** \n\nuse the walls to do Bouncing Dodge so that ball crosses the enemy without giving to them , then use the attack to pass through them and take the ball . This Makes you  Pass the enemy easily',
	'**General :** \nUse the Aimbot only when the enemy is at a distance of half of your brawler range',
	'**General :** \nUse aimed attacks for enemies at large distances and use the aimbot for quick attacks to deal fast damage',
	'**Long Range Brawlers :** \nTarget  the enemies at a place where he will be present after you attack . It will be helpful if you calculate . You are a Genius . aren\'t you ?',
	'**General :** \nDont underestimate any brawlers . auto-aim attacks can change Dusk to Dawn . Beware !!',
	'**Dynamike Mains :** \nNever ever think of using auto-aim for Dynamike . It will affect you badly !! . Seriously!',
	'**General :** \nUse aimed attacks for enemies at large distances and use the aimbot for quick attacks to deal fast damage',
	'**Leon Mains :** \nEnemy Leon\'s clone will receive twice of your brawler\'s damage  . Find it by attacking once , don\'t waste your Ammo .  Or else leon will use his 3 ammo and kill you . You dont need it nah ? Be patient.\nNote: This is only for leon\'s clone at larger distances , if you check when leon is near you , You will be FIRED!!',
	'**Advice :** \nUse the Ammos wisely . Patience is the key !',
	'**Advice :** \nHave almost full patience in brawl ball . Use supers , gadgets and ammos very wisely . they are NOT INFINITE . Enemies change the ball\'s fate to our goals within fraction of seconds . So dont miss the ball and blame the teammates . All the best !'
	]
	l=random.randint(0,len(col)-1)
	e=discord.Embed(title='A Tip from this poor lad',desc='',color=col[l])
	e.set_author(name='ModerBellator , The AutoModerator of Homicide Crew')
	e.add_field(name="============-&-============", value=random.choice(tiplist))
	e.set_thumbnail(url='https://cdn.discordapp.com/attachments/692403681294811167/886114248709775411/PicsArt_09-11-10.30.19.jpg')
	e.set_footer(text=f'Requested By {ctx.author.display_name} ')
	await ctx.send(embed=e)

keep_alive()
cl.run(os.environ['DISCORD_TOKEN'])
