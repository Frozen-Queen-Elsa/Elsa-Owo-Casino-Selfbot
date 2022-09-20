
from requests import get
from color import color
from menu import UI
from time import sleep
from re import findall
from inputimeout import TimeoutOccurred, inputimeout
import json
ui = UI()
class data:
	def __init__(self):


		self.OwOID = '408785106942164992'
		self.totalcmd = 0
		self.totaltext = 0
		self.username=""
		self.userid = ""
		self.stopped = False
		#OCF
		self.checknocash=False
		self.totalwon=0
		self.totallost=0
		self.checknocash=False
		self.countcfmaxlost=0
		self.countosmaxlost=0

		with open('settings.json', "r") as file:
			data = json.load(file)
			self.token = data["token"]
			self.channel = data["channel"]	
			self.webhook = data["webhook"]
			self.webhookping = data["webhookping"]
			self.solve = data['solve']
	
			#OCF
			self.cfm =data['cfm']
			self.cfbet = int(data["cfbet"])
			self.current_cfbet = self.cfbet
			self.cfrate = int(data["cfrate"])
			self.osm =data['osm']
			self.osbet = int(data["osbet"])
			self.current_osbet = self.osbet
			self.osrate = int(data["osrate"])
			self.maxbet = data["maxbet"]   


		


	def check(self):
		if self.token and self.channel == 'nothing' or self.token and self.channel == '123':
			print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
			sleep(2)
			from newdata import main
			main()
		else:
			response = get('https://discord.com/api/v9/users/@me',headers={"Authorization": self.token})
			if response.status_code != 200:
				print(f"{color.fail} !!! [ERROR] !!! {color.reset} Invalid Token")
				sleep(2)
		
a = data()
a.check()
