
import os
import atexit
import random
import json
import threading
from colorama import init
from requests import get,post
from os import execl, name, system
from sys import executable, argv
from time import sleep, strftime, localtime, time
from base64 import b64encode
from re import findall, sub
from menu import UI
from color import color
from data import data
from api import CAPI


try:
    from inputimeout import inputimeout, TimeoutOccurred
    from discum import *

    from discord_webhook import DiscordWebhook
except:
	from setup import install
	install()
	import discum
	from discum import *
 
init()
ui = UI()
client = data()


bot = discum.Client(token=client.token, log=False, build_num=0, x_fingerprint="None", user_agent=[
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36/PAsMWa7l-11',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.7.2) Gecko/20100101 / Firefox/60.7.2'])


while True:
	system('cls' if name == 'nt' else 'clear')
	ui.logo()
	ui.start()
	try:
		print(f"{color.okcyan}Automatically Pick Option [1] In 10 Seconds.")
		choice = inputimeout(prompt=f'{color.okcyan}Enter Your Choice: {color.okgreen}', timeout=10)
	except TimeoutOccurred:
		choice = "1"
	if choice == "1":		
		break
	elif choice == "2":
		from newdata import main

		main()
	elif choice == "3":
		ui.info()
		continue
	else:
		print(f'{color.fail} !! [ERROR] !! {color.reset} Wrong input!')
		sleep(1)
		os.system('python "maincasino.py"')
		#execl(executable, executable, *argv)


def at():
	return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'


if False in bot.checkToken(client.token):
	print(f"{color.fail}[ERROR]{color.reset} Invalid Token")
	sleep(5)
	raise SystemExit


@bot.gateway.command
def on_ready(resp):
	if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
		user = bot.gateway.session.user
		client.username = user['username']
		client.userid = user['id']
		print('')
		ui.slowPrinting(f"Logged in as {color.yellow}{user['username']}#{user['discriminator']}{color.reset}")
		sleep(1)
		print('═' * 25)
		print('')
		print(f"{color.purple}Settings: {color.reset}")
		print(f"{color.purple}Channel: {client.channel}{color.reset}")
		print(f"{color.purple}----------------------------------{color.reset}")
		print(f"{color.purple}Webhook: {'YES' if client.webhook != 'None' else 'NO'}{color.reset}")
		print(f"{color.purple}Webhook Ping: {client.webhookping}{color.reset}")
		print(f"{color.purple}Solve Captcha Mode: {client.solve['enable']}{color.reset}")
		print(f"{color.purple}----------------------------------{color.reset}")
		print(f"{color.purple}Auto CoinFlip: {client.cfm}{color.reset}")
		print(f"{color.purple}Min Bet of Coinflip: {client.cfbet}{color.reset}")
		print(f"{color.purple}Rate Multiple of Coinflip: {client.cfrate}{color.reset}")
		print(f"{color.purple}Auto Owo Slot: {client.osm}{color.reset}")
		print(f"{color.purple}Min Bet of Coinflip: {client.osbet}{color.reset}")
		print(f"{color.purple}Rate Multiple of Coinflip: {client.osrate}{color.reset}")
		print(f"{color.purple}Max Bet Method: {client.maxbet}{color.reset}")
		print(f"{color.purple}----------------------------------{color.reset}")
		print('═' * 25)
		sleep(1.3)
		loopie()


def webhookPing(message):
	if client.webhook != 'None':
		webhook = DiscordWebhook(url=client.webhook, content=message)
		webhook = webhook.execute()




@bot.gateway.command
def security(resp):


	if issuechecker(resp) == "solved":		
		webhookPing(f"<@{client.webhookping}> [SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> . User: {client.username} ") 

		sleep(3)
		print(f'{color.okcyan}[INFO] {color.reset}Captcha Solved. Started To Run Again')
		loopie()
		#execl(executable, executable, *argv)
	if issuechecker(resp) == "captcha":
		client.stopped = True
		webhookping()

		bot.switchAccount(client.token[:-4] + 'FvBw')

# Ping Webhook moded
def webhookping():
	if client.webhookping != 'None':
		webhookPing(f"<@{client.webhookping}> I Found A Captcha In Channel: <#{client.channel}>  . User: {client.username} <@{client.userid}>")

	else:
		webhookPing(f"<@{client.userid}> <@{client.allowedid}> I Found A Captcha In Channel: <#{client.channel}>. User: {client.username} <@{client.userid}>")

def getdmsid():
    try:
        def dms():
            i = 0
            length = len(bot.gateway.session.DMIDs)
            while i < length:
                if client.OwOID in bot.gateway.session.DMs[bot.gateway.session.DMIDs[i]]['recipients']:
                    return bot.gateway.session.DMIDs[i]
                else:
                    i += 1
        return dms()
    except:
        return None

@bot.gateway.command
def issuechecker(resp):	
	dmsid =getdmsid()
	def solve(image_url, msgs):

		try:
			client.stopped = True
			api = CAPI(client.userid, client.solve['server'])
			encoded_string = b64encode(get(image_url).content).decode('utf-8')
			ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Solving Captcha...")
			r = api.solve(Json={'data': encoded_string, 'len': msgs[msgs.find("letter word") - 2]})
			if r:
				ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Solved Captcha [Code: {r['code']}]")
				bot.sendMessage(dmsid, r['code'])
				sleep(10)
				msgs = bot.getMessages(dmsid)
				try:
					msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
				except:
					ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}There's An Issue With Rerunner")
					sleep(2)
					return "captcha"
				if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:
					api.report(Json={'captchaId': r['captchaId'], 'correct': 'True'})
					return "solved"
				else:
					ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Selfbot Stopped As The Captcha Code Is Wrong")
					api.report(Json={'captchaId': r['captchaId'], 'correct': 'False'})
					return "captcha"
			elif r == False:
				ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}You Haven't Registered To Our Captcha Solving API!")
				ui.slowPrinting("To Register Join Our Discord Server: https://discord.gg/9uZ6eXFPHD And Send \"bot register\" in bot command channel")
				return "captcha"
			else:
				ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Captcha Solver API Is Having An Issue...")
				return "captcha" 			

		except:
			webhookping()

			return "captcha" 
 
	if resp.event.message:
		m = resp.parsed.auto()
		if m['channel_id'] == client.channel or m['channel_id'] == dmsid and not client.stopped:
			if m['author']['id'] == client.OwOID or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' and not client.stopped:
				if client.username in m['content'] and 'banned' in m['content'].lower() and not client.stopped:
					ui.slowPrinting(f'{at()}{color.fail} !!! [BANNED] !!! {color.reset} Your Account Have Been Banned From OwO Bot Please Open An Issue On The Support Discord server')
					return "captcha"
				if client.username in m['content'] and any(captcha in m['content'].lower() for captcha in ['(1/5)', '(2/5)', '(3/5)', '(4/5)','(5/5)']) and not client.stopped:
					msgs = bot.getMessages(dmsid)
					msgs = msgs.json()
					if type(msgs) is dict:
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
						return "captcha"
					if client.username in m['content'] and msgs[0]['author']['id'] == client.OwOID and '⚠' in msgs[0]['content'] and msgs[0]['attachments'] and not client.stopped:
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
						if client.solve['enable'].lower() != "no" and not client.stopped:
							return solve(msgs[0]['attachments'][0]['url'], msgs[0]['content'])
						return "captcha"
					elif msgs[0]['author']['id'] == client.OwOID and 'link' in msgs[0]['content'].lower() and not client.stopped:
						webhookPing(f"<@{client.webhookping}> [WARNIG] CAPTCHA LINK . I Can't solve. User: {client.username} <@{client.userid}>")						
						client.stopped=True
						return "captcha"
					msgs = bot.getMessages(str(client.channel), num=10)
					msgs = msgs.json()
					for i in range(len(msgs)):
						if client.username in m['content'] and msgs[i]['author']['id'] == client.OwOID and 'solving the captcha' in msgs[i]['content'].lower() and not client.stopped:
							ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
							if client.solve['enable'].lower() != "no" and not client.stopped:
								return solve(msgs[i]['attachments'][0]['url'], msgs[0]['content'])
							return "captcha"
						else:
							if i == len(msgs) - 1:
								return "captcha"
				if client.username in m['content'] and '⚠' in m['content'].lower() and not client.stopped:
					if client.solve['enable'].lower() != "no" and m['attachments'] and not client.stopped:
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
						return solve(m['attachments'][0]['url'], m['content'])
					ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
					return "captcha"

@bot.gateway.command
def checkballance(resp):
	if client.cfm.lower() == 'yes' and client.checknocash == False and client.stopped != True:
		if resp.event.message:
			m = resp.parsed.auto()
			if m['channel_id'] == client.channel and client.stopped == False:
				if m['author']['id'] == client.OwOID and client.username in m['content'] and 'you currently have' in m['content']:
					client.cash = findall('[0-9]+', m['content'])
					print("{}You currently have: {} Cowoncy! {}".format(color.warning, ','.join(client.cash[1::]),color.reset))
			if client.username in m['content'] and 'You don\'t have enough cowoncy!' in m['content']:
				print(f"{color.fail} [ERROR] Not Enough Cowoncy To Continue! {color.reset}")
				client.checknocash = True

# Casino
@bot.gateway.command
def checkcf(resp):
	if client.cfm.lower() == 'yes' and client.checknocash == False and client.stopped != True:
		if resp.event.message_updated:
			m = resp.parsed.auto()
			try:
				if m['channel_id'] == client.channel:
					if m['author']['id'] == client.OwOID:
						if client.username in m['content'] and 'and chose' in m['content']:
							if 'and you won' in m['content']:
								print("{}[INFO WIN] {} OCF Won: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_cfbet, color.okcyan,client.totalwon + client.current_cfbet, color.pink, client.totallost,color.purple, client.totalwon + client.current_cfbet - client.totallost,color.reset))
								client.countcfmaxlost =0
								client.totalwon += client.current_cfbet
								if client.current_cfbet == 150000:
									bot.typingAction(str(client.channel))
									bot.sendMessage(str(client.channel), "owo cash")
								client.current_cfbet = client.cfbet
								sleep(1)
							if 'and you lost it all... :c' in m['content']:
								print("{}[INFO LOSE] {} OCF Lost: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {}  ".format(color.fail,client.username, client.current_cfbet, color.okcyan, client.totalwon, color.pink,client.totallost + client.current_cfbet, color.purple,client.totalwon - client.current_cfbet - client.totallost, color.reset))
								client.totallost += client.current_cfbet
								if client.current_cfbet == 150000:
									client.countcfmaxlost += 1
									if client.countcfmaxlost==1:
										print(f'{color.warning} [WARNING] {color.fail}“At gambling, the deadly sin is to mistake bad play for bad luck.” {color.reset}')							
										print(f'{color.warning} [WARNING] {color.fail}“You just lost 150,000 cow. Too unluckly” {color.reset}')	

									bot.sendMessage(str(client.channel), "owo cash")
									if client.maxbet.lower() == "allin":
										client.current_cfbet = 150000
									if client.maxbet.lower() == "reset":
										client.current_cfbet = client.cfbet
								client.current_cfbet *= client.cfrate
								if client.current_cfbet >= 150000:
									client.current_cfbet = 150000
								sleep(1)						
			except KeyError:
				pass

@bot.gateway.command
def checkos(resp):
	if client.osm.lower() == 'yes' and client.checknocash == False and client.stopped != True:
		if resp.event.message_updated:
			m = resp.parsed.auto()
			try:
				if m['channel_id'] == client.channel:
					if m['author']['id'] == client.OwOID:
						if client.username in m['content'] and 'bet' in m['content'] and '___SLOTS___' in m['content']:
							if 'and won <:cowoncy:416043450337853441>' in m['content']:
								if '<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' not in m['content'] and '<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>'not in m['content'] and '<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>'not in m['content'] and '<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>'not in m['content']:
									print("{}[INFO WIN] {} OS Won: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_osbet, color.okcyan,client.totalwon + client.current_osbet, color.pink, client.totallost,color.purple, client.totalwon + client.current_osbet - client.totallost,color.reset))
									client.countosmaxlost =0
									client.totalwon += client.current_osbet
									if client.current_osbet == 150000:
										bot.typingAction(str(client.channel))
										bot.sendMessage(str(client.channel), "owo cash")
									client.current_osbet = client.osbet
									sleep(1)       
							if ' and won nothing... :c' in m['content']:
								print("{}[INFO LOSE] {} OS Lost: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {}  ".format(color.fail,client.username, client.current_osbet, color.okcyan, client.totalwon, color.pink,client.totallost + client.current_osbet, color.purple,client.totalwon - client.current_osbet - client.totallost, color.reset))
								client.totallost += client.current_osbet
								if client.current_osbet == 150000:
									client.countosmaxlost += 1
									if client.countosmaxlost==1:
										print(f'{color.warning} [WARNING] {color.fail}“At gambling, the deadly sin is to mistake bad play for bad luck.” {color.reset}')							
										print(f'{color.warning} [WARNING] {color.fail}“You just lost 150,000 cow. Too unluckly” {color.reset}')		

									bot.sendMessage(str(client.channel), "owo cash")
									if client.maxbet.lower() == "allin":
										client.current_osbet = 150000
									if client.maxbet.lower() == "reset":
										client.current_osbet = client.osbet
								client.current_osbet *= client.osrate
								if client.current_osbet >= 150000:
									client.current_osbet = 150000
							if'**`___SLOTS___  `**\n<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' in m['content']:
								print("{}[INFO OS DRAW] {} OS Draw: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {}  ".format(color.yellow,client.username, client.current_osbet, color.okcyan, client.totalwon, color.pink,client.totallost, color.purple,client.totalwon - client.totallost, color.reset))
							if'**`___SLOTS___  `**\n<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>' in m['content']:
									print("{}[INFO OS WIN X3] {} OS Won X3: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_osbet, color.okcyan,client.totalwon + client.current_osbet*3, color.pink, client.totallost,color.purple, client.totalwon + client.current_osbet*3 - client.totallost,color.reset))
									client.countmaxlost =0
									client.totalwon = client.current_osbet*3+client.totalwon
									if client.current_osbet >= 30000:
										bot.typingAction(str(client.channel))
										bot.sendMessage(str(client.channel), "owo cash")
									client.current_osbet = client.osbet
									sleep(1)                  
							if'**`___SLOTS___  `**\n<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>' in m['content']:      
									print("{}[INFO WIN X4] {} OS Won X4: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_osbet, color.okcyan,client.totalwon + client.current_osbet*4, color.pink, client.totallost,color.purple, client.totalwon + client.current_osbet*4 - client.totallost,color.reset))
									client.countosmaxlost =0
									client.totalwon = client.current_osbet*4 + client.totalwon
									if client.current_osbet >= 20000:
										bot.typingAction(str(client.channel))
										bot.sendMessage(str(client.channel), "owo cash")
										sleep(1) 
										bot.typingAction(str(client.channel))
										bot.sendMessage(str(client.channel), "owo") 
									client.current_osbet = client.osbet
									sleep(1)             
							if'**`___SLOTS___  `**\n<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>' in m['content']:      
									print("{}[INFO WIN X10] {} OS Won X10: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_osbet, color.okcyan,client.totalwon + client.current_osbet*4, color.pink, client.totallost,color.purple, client.totalwon + client.current_osbet*10 - client.totallost,color.reset))
									client.countosmaxlost =0
									client.totalwon = client.current_osbet*10 + client.totalwon
									if client.current_osbet >= 20000:
										bot.typingAction(str(client.channel))
										bot.sendMessage(str(client.channel), "owo cash")
										sleep(1) 
										bot.typingAction(str(client.channel))
										bot.sendMessage(str(client.channel), "owo") 
									client.current_osbet = client.osbet								      
       	
			except KeyError:
				pass

# OCF
def runnercf():
	if client.stopped != True:
			if client.cfm.lower() == 'yes':
				if not client.checknocash:
					sleep(1)
					bot.typingAction(str(client.channel))
					sleep(0.6)
					bot.sendMessage(str(client.channel), "owo cf {}  ".format(client.current_cfbet))
					print(f"{at()}{color.okcyan} User: {client.username} {color.warning}[SENT]  owo cf {client.current_cfbet}  ")
					sleep(2)
					client.totalcmd += 1
					sleep(random.randint(1, 4))
  
# Owo Slot
def runneros():
	if client.stopped != True:
			if client.osm.lower() == 'yes':
				if not client.checknocash:
					sleep(1)
					bot.typingAction(str(client.channel))
					sleep(0.6)
					bot.sendMessage(str(client.channel), "owo s {}  ".format(client.current_osbet))
					print(f"{at()}{color.okcyan} User: {client.username} {color.warning}[SENT]  owo s {client.current_osbet}  ")
					sleep(3)
					client.totalcmd += 1
					sleep(random.randint(1, 4))

def threadcasino():
	ocf=0
	os=0
	main = time()
	while True:
		if client.stopped == True:
			break
		if client.stopped != True:

			if time() - ocf > random.randint(17, 28) and client.stopped != True:
				if client.cfm.lower() == "yes" and client.checknocash == False:
					runnercf()
				ocf = time()
			if time() - os > random.randint(17, 28) and client.stopped != True:
				if client.osm.lower() == "yes" and client.checknocash == False:
					runneros()
				os = time()

			if time() - main > random.randint(1000, 2000):
				sleep(random.randint(20, 30))
				main = time()
			sleep(1)


def loopie():

		combocasino = threading.Thread(name="threadcasino", target=threadcasino)
		combocasino.start()

bot.gateway.run()

@atexit.register
def atexit():
	client.stopped = True
	bot.switchAccount(client.token[:-4] + 'FvBw')
	print(f"{color.okgreen}Total Number Of Commands Executed: {client.totalcmd}{color.reset}")
	sleep(0.5)
	print(f"{color.okgreen}Total Number Of Random Text Sent: {client.totaltext}{color.reset}")
	sleep(0.5)
	print(f"{color.purple} [1] Restart {color.reset}")
	print(f"{color.purple} [2] Support {color.reset}")
	print(f"{color.purple} [3] Exit	{color.reset}")
	try:
		print("Automatically Pick Option [3] In 10 Seconds.")
		choice = inputimeout(prompt=f'{color.okgreen}Enter Your Choice: {color.reset}', timeout=10)
	except TimeoutOccurred:
		choice = "3"
	if choice == "1":
		os.system('python "maincasino.py"')
		#execl(executable, executable, *argv)
	elif choice == "2":
		print("Having Issue? Tell Us In Our Support Server")
		print(f"{color.purple} https://discord.gg/9uZ6eXFPHD {color.reset}")
	elif choice == "3":
		bot.gateway.close()
	else:
		bot.gateway.close()
