import os, time, sys
from time import sleep, strftime, localtime, time
from color import color
class UI:

	@classmethod
	def slowPrinting (cls, text):
		for letter in text:
			sys.stdout.write(letter)
			sys.stdout.flush()

			sleep(0.000001)
		print()

	@classmethod
	def logo(cls):
		print(f'{color.okcyan}{elsa}{color.reset}')
		print(f"                   {color.purple}Version: ELSA OWO CASINO {color.reset}")
		sleep(0.5)
		print()
		print("╔═════════════════════════════════════════════════════════════════════════════════╗")
		print()
		cls.slowPrinting(f" {color.yellow}This is the moded auto by {color.okcyan}Iris {color.yellow}({color.okcyan}FrozenQueenElsa{color.yellow}). {color.reset}")
		cls.slowPrinting(f" {color.yellow}Thanks to {color.okcyan}ahihiyou20{color.yellow} for the original version{color.reset}")
		cls.slowPrinting(f" {color.yellow}Thanks to {color.okcyan}Naru2203{color.yellow} for the auto owo slot version{color.reset}")
		print()
		print("╚═════════════════════════════════════════════════════════════════════════════════╝")
		print()
		sleep(1)
	@classmethod
	def start(cls):
		print("╔═══════════════════════════════╗")
		print()
		print(f"       {color.purple}[1]{color.reset} Load Data")
		print(f"       {color.purple}[2]{color.reset} Create New data")
		print(f"       {color.purple}[3]{color.reset} Additional Info")
		print()
		print("╚═══════════════════════════════╝")



	@classmethod
	def newData(cls):
		print("╔═══════════════════════════════════════════╗")
		print()
		print("         [0] Exit And Save")
		print("         [1] Change All Settings")
		print("         [2] Change Token")
		print("         [3] Change Channel")
		print("         [4] Change Solve Captcha")
		print("         [5] Change Owo Casino Setting")
		print("         [6] Change Webhook Settings")	
		print()
		print("╚═══════════════════════════════════════════╝")
	@classmethod
	def info(cls):
		print(f"{color.purple}╔═════════════════Support════════════════╗{color.reset}")
		print(f"\t{color.purple}https://discord.gg/9uZ6eXFPHD{color.reset}")
		print(" ")
		print(f"{color.purple}╔═══════════════════════════════════════════════════════════════════════════Disclaimer═══════════════════════════════════════════════════════╗{color.reset}")
		print(f"\t{color.purple}This SelfBot Is Only For Education Purpose Only. Deny All Other Promises Or Responsibilities. Use The SelfBot At Your Own Risk.")
		print(" ")
		print(f'{color.purple}╔═════════════════Credit═════════════════╗{color.reset}')
		print(f'\t{color.purple} [Developer] {color.okcyan} Sudo-Nizel{color.reset}')
		print(f'\t{color.purple} [Developer] {color.okcyan} ahihiyou20{color.reset}')
		print(f'\t{color.purple} [Developer] {color.okcyan} Iris(ThanhThanh){color.reset}')
		print(" ")

		print("Note: Alright If You See Someone Selling This Code Then You Got Scammed Because This Code Is Free!")
		sleep(0.5)
		print("Press Enter To Exit")
		input()


elsa='''\
								███████╗██╗     ███████╗ █████╗                                                           
								██╔════╝██║     ██╔════╝██╔══██╗                                                          
								█████╗  ██║     ███████╗███████║                                                          
								██╔══╝  ██║     ╚════██║██╔══██║                                                          
								███████╗███████╗███████║██║  ██║                                                          
								╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝                                                          
                                                                                          
 ██████╗ ██╗    ██╗ ██████╗     ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔═══██╗██║    ██║██╔═══██╗    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║██║ █╗ ██║██║   ██║    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
██║   ██║██║███╗██║██║   ██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
╚██████╔╝╚███╔███╔╝╚██████╔╝    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
 ╚═════╝  ╚══╝╚══╝  ╚═════╝     ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                          
'''