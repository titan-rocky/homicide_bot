import discord
from discord import Webhook,RequestsWebhookAdapter
from discord.ext import commands,tasks
import asyncio
import tracemalloc
tracemalloc.start()
import os
import random
import requests
import json
from datetime import datetime
import csv
from alive import keep_alive
import disbsint
import pytz

#important variables
op_discord_id=['557914347490508806','709740580988780624']

def check_op(id):
	op_discord_id=[557914347490508806,709740580988780624]
	for i in op_discord_id:
		if not i==id:
			return False
		else:
			return True


bs_APIKEY=os.environ['BRAWL_API_KEY']

homicrew_channels={'general':691292302580121693}

inn=discord.Intents.all()
cl=commands.Bot(command_prefix='belle ',description='Dedicated for HOMICIDE_CREW',intents=inn,case_insensitive=True)


@tasks.loop(seconds=60)
async def gud_mor():
	indtime=datetime.now(pytz.timezone('Asia/Calcutta'))
	b=indtime.strftime('%H:%M:%S')
	if b.startswith('23:30'):
		await cl.get_channel(homicrew_channels['general']).send('Good Night Everyone <a:sleepsandy:887379970769436732>')
	elif b.startswith('06:00'):
		await cl.get_channel(homicrew_channels['general']).send('Good Morning Everyone <a:bibigg:887380758795288577>')



@cl.event
async def on_ready():
	print('I am Ready')
	await cl.change_presence(status=discord.Status.idle,activity=discord.Game(name="Shockers with Positive Feedback",assets={'large_image_url':'https://cdn.discordapp.com/attachments/737942309173329985/886997742252081212/PicsArt_09-11-10.29.55.jpg','large_text':'sdghsdh'}))
	gud_mor.start()
	#(status=discord.Status.idle,activity=discord.Streaming(name="Leagen Returns",platform='twitch',url='https://www.twitch.tv/titan_rocky',details='Leagen Returns',assets={'large_image':'877557270177808394','large_text':'sdghsdh'}))
	#await cl.change_presence(activity=discord.Streaming(name="Black Flames",url='https://www.twitch.tv/titan_rocky')
	
	#await cl.change_presence(status=discord.Status.idle,activity=discord.Streaming(name="Shockers with Positive Feedback",platform='twitch',url='https://www.twitch.tv/titan_rocky',details='Shockers with Positive Feedback',assets={'large_image':'https://cdn.discordapp.com/attachments/737942309173329985/886997742252081212/PicsArt_09-11-10.29.55.jpg','large_text':'sdghsdh'}))

	#cl.loop.create_task(club_entry())     brawl api remains.py
	#cl.loop.create_task(role_update())


@cl.event
async def on_message(message):
	if message.author==cl.user:
		return
	if cl.user.mentioned_in(message):
		look_aem=await cl.get_guild(887015707366277170).fetch_emoji(887016423854059520)
		await message.add_reaction(look_aem)

	bad_word=['sunni','fuck','fak','junni','poinda','Pointhe','Pointha','kudhi','kuthi','Tavethiya','nigga','sex','penis','vagina','pp']
	words=message.content.split(' ')
	for i in words:
		for j in bad_word:
			if i.lower()==j.lower() or j.lower() in i.lower():
				await message.delete()
				await message.channel.send(f'{message.author.mention} Dont use Explicit words Here , you pile of poop 💩 !')
	sad_words=['sad','depressed','die','sorrow','unhappy','not feeling well']
	if any (i in message.content.split(' ') for i in sad_words):
		sad_aem=await cl.get_guild(887015707366277170).fetch_emoji(887024376917139506)
		await message.add_reaction(sad_aem)
	if any(i.lower()=='amaterasu' or i.lower()=='itachi' for i in message.content.split(' ')):
		if random.randint(0,4)==3:
			await message.channel.send('<a:amaterasu:887033967264550912>')

	if isinstance(message.channel,discord.channel.DMChannel) and message.author != cl.user:
		await message.channel.send('This is a DM , commands only work on HOMICIDE_CREW server')
		return
	else:
		await cl.process_commands(message)

	# $hi command
	# $addit command - discord_brawl stars id integration
	# $help - help embed

@cl.event
async def on_message_delete(message):
	col=[0x99b898,0xfecea8,0xff847c,0xea485f]
	dd=discord.Embed(color=random.choice(col),title="Message Deletion")
	dd.add_field(name=f'Message :',value=f' {message.content}')
	bnow=datetime.now(pytz.timezone('Asia/Calcutta'))
	btimestamp=bnow.strftime('%d %B,%Y - %H:%M ')
	dd.set_footer(text=f'sent by {message.author.name}#{message.author.discriminator} on {btimestamp}')
	await cl.get_channel(750581748546535556).send(embed=dd)


@cl.event
async def on_member_join(member):
	now=datetime.now(pytz.timezone('Asia/Calcutta'))
	col=[0x99b898,0xfecea8,0xff847c,0xea485f]
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


		indtime=datetime.now(pytz.timezone('Asia/Calcutta'))

		ch2=cl.get_channel(889112863103418378)
		e2=discord.Embed(title='New Member of our Family',color=0xF8B195,description='👨‍👦‍👦 Thanks for joining mate')
		origin=member.created_at
		e2.set_author(name=f'{member.name} #{member.discriminator}')
		e2.set_thumbnail(url=member.avatar_url)
		mob=datetime.now(pytz.timezone('Asia/Calcutta'))
		dat=origin.strftime('%d %b, %Y')
		tim=origin.strftime('%H:%M')
		jointime=mob.strftime('%d %b, %Y - %I:%M %p')
		e2.add_field(name=f'Good To see you here',value=f'Joined on {jointime}\n',inline=True)
		e2.set_footer(text=f'Account Created on {dat} at {tim}')
		await ch2.send(embed=e2)
	else:
		return


@cl.event
async def on_member_remove(member):
	col=0xF67280
	ch2=cl.get_channel(889112863103418378)
	e2=discord.Embed(title='A Member has Left our Family',color=col,description='a state of depression and sorrow')
	mob=datetime.now(pytz.timezone('Asia/Calcutta'))
	dat=mob.strftime('%d %b, %Y - %I:%M %p')
	e2.set_author(name=f'{member.name} #{member.discriminator}')
	e2.add_field(name=f'Its sad to see you leave this server',value=f'Left on {dat}\n',inline=True)
	e2.set_thumbnail(url=member.avatar_url)

	e2.set_footer(text=f'Poor Club !',icon_url='https://media.discordapp.net/attachments/737942309173329985/889123885834981416/322-3224005_unemployment-clip-art.png')
	await ch2.send(embed=e2)

@cl.event
async def on_command(ctx):
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
	bnow=datetime.now(pytz.timezone('Asia/Calcutta'))
	btimestamp=bnow.strftime('%d %B,%Y - %H:%M ')
	dd.set_footer(text=f'invoked by {ctx.author.name}#{ctx.author.discriminator} on {btimestamp}')
	await cl.get_channel(750581846143664169).send(embed=dd)
	    
@cl.command()
async def hi(ctx):
	print(f'$hi by {ctx.author.name}#{ctx.author.discriminator} id {ctx.author.id}')
	if str(ctx.author.id)=='557914347490508806':
		await ctx.channel.send('A Warm Welcome, *Hon\'ble* **Lord Chief**')
	elif str(ctx.author.id)=='738652832340901939':
		await ctx.channel.send('A Warm Welcome , **The Guardian** of the **General chat**')
	elif str(ctx.author.id)=='763356911235497984':
		await ctx.channel.send('A Warm Welcome , **Lady Boss**')
	elif str(ctx.author.id)=='709740580988780624':
		await ctx.channel.send('Hello, **Mod 😈**')	
	else:
		await ctx.send(f'A Warm Welcome , *Hon\'ble* **{ctx.author.display_name}** ')


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
async def purge(ctx,*args):
	print(args)
	try:
		b=[int(i) for i in args]
	except ValueError:
		await ctx.send('Please Provide a Valid integer <100')
		b=[]

	if len(b)!=1:
		await ctx.send('Only One Argument limit(int) required')
	else:
		if isinstance(b[0],int):
			if check_op(ctx.author.id):
				await ctx.channel.purge(limit=b[0])
			else:
				await ctx.send('You are Not Authorized !')


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


@cl.command()
async def joke(ctx):
	key=os.environ['joke_api_key']
	url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"
	querystring = {"format":"json","blacklistFlags":"nsfw,religious,political,racist,sexist,explicit","safe-mode":"true"}
	headers = {
	    'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com",
	    'x-rapidapi-key': f'{key}'
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	answer=response.json()


	if answer['error']=='true':
		mb=discord.Embed(title='A Joke said by a father , to his Emotionless Son',col=0x30D5C8,description=f'Error')
		mb.add_field(name=f'A Problem has been Occured',value=f'Please report it to the Admin.\nThe Problem will be solved soon')
	else:
		cat=answer['category']
		mb=discord.Embed(title='A Joke said by a father , to his Emotionless Son',col=0x40e0d0,description=f'Category : {cat}')
		
		if 'setup' in answer and 'delivery' in answer:
			setup=answer['setup']
			delivery=answer['delivery']
			mb.add_field(name=f'Father : \n{setup}',value=f'**Son : ?**\n**Father : **||{delivery}||\n\n*Click on it to reveal*')
		elif 'setup' in answer and 'punchline' in answer:
			setup=answer['setup']
			punch=answer['punchline']
			mb.add_field(name=f'Father : \n{setup}',value=f'**Son : ?**\n**Father : **||{punch}||\n\n*Click on it to reveal*')
		elif 'joke' in answer:
			jok=answer['joke']
			mb.add_field(name=f'Joke : \n',value=f'{jok}')



	mb.set_author(name='Someone called me for jokes ༼ つ ◕_◕ ༽つ ')
	mb.set_footer(text='Thanks to Joke API | Website : https://v2.jokeapi.dev/')
	await ctx.send(embed=mb)










keep_alive()
cl.run(os.environ['DISCORD_TOKEN'])
