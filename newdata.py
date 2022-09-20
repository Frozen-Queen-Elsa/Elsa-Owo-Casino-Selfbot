from menu import UI
from json import load, dump
from time import sleep
from color import color
ui = UI()

#[0] Exit And Save")
#[1] Change All Settings")
#[2] Change Token")
#[3] Change Channel")
#[4] Change Solve Captcha")
#[5] Change Owo Casino Setting")
#[6] Change Webhook Settings")	

def main():
	with open("settings.json", "r") as f:
		data = load(f)
	ui.newData()
	choice = input(f"{color.okgreen}Enter Your Choice:  {color.reset}")
	if choice == "0":
        
		pass
	elif choice == "1":

		t(data, True)
		c(data, True)
		webhook(data, True)
		casinom(data, True)


	elif choice == "2":
		t(data, False)
	elif choice == "3":
		c(data, False)
	elif choice == "4":
		solve(data, False)
	elif choice == "5":
		casinom(data, False)
	elif choice == "6":
		webhook(data, False)
 
	else:
		ui.slowPrinting(f"{color.fail}[INFO] {color.reset}Invalid Choice")
def t(data,all):
 data['token'] = input("Please Enter Your Account Token: ")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()
def c(data,all):
 data['channel'] = input("Please Enter Your Channel ID: ")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()
def webhook(data,all):
 data['webhook'] = input("Toggle Discord Webhook, Enter Webhook Link If You Want It To Ping You If OwO Asked Captcha. Otherwise Enter \"None\": ")
 if data['webhook'] != "None":
  data['webhookping'] = input("Do You Want To Ping A Specified User When OwO Asked Captcha? If Yes Enter User ID. Otherwise Enter \"None\": ")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()


def solve(data, all):
 data['solve']['enable'] = input(f"{color.okgreen}Toggle Automatically Captcha Solving(YES/NO) [Dont use with the other solver]: {color.yellow}")
 if data['solve']['enable'].lower() == "yes":
    ui.slowPrinting(f"{color.okgreen}Available Captcha Solving Server:\n1: https://autofarmsupport.tk\n2: https://afbot.dev{color.yellow}")
    data['solve']['server'] = input(f"{color.okgreen}Which Server Do You Want To Use (1/2): {color.yellow}")
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()
def casinom(data, all):
 data['maxbet'] = input(f"{color.okgreen}Are you prefer all in to die or reset bet when the bet > 150k ? (AllIn/Reset): {color.yellow}")
 data['cfm']=input(f"{color.okgreen}Do you want to play CoinFlip (YES/NO/): {color.yellow}")
 if data['cfm'].lower()== 'yes':
    ui.slowPrinting(f"{color.cyan}[INFO] {color.warning}Input Coinflip Information")
    data['cfbet'] = input(f"{color.okgreen}Enter Your Bet Amount for CoinFlip (Must Be Integer): {color.yellow}")
    data['cfrate'] = input(f"{color.okgreen}Enter Your Bet Rate Multiple for CoinFlip (Ngã ở đâu x? ở đó) (Best is x4) (x2 is not good) (Must Be Integer): {color.yellow}")
        
 data['osm']=input("Do you want to play Owo Slot (YES/NO/): ")
 if data['osm'].lower()== 'yes':
    ui.slowPrinting(f"{color.cyan}[INFO] {color.warning}Input Coinflip Information")
    data['osbet'] = input(f"{color.okgreen}Enter Your Bet Amount for OwoSlot (Must Be Integer):{color.yellow} ")
    data['osrate'] = input(f"{color.okgreen}Enter Your Bet Rate Multiple for OwoSlot (Ngã ở đâu x? ở đó) (Best is x3) (x2 is not good) (Must Be Integer): {color.yellow}")       
 file = open("settings.json", "w")
 dump(data, file)
 file.close()
 ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
 if not all:
  main()


if __name__ == "__main__":
  main()

