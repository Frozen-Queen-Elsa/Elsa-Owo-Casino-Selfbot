from requests import get, post

class CAPI:
	def __init__(self, userID:str, server:int):
		self.ID = userID
		self.url = None
		if server == 1: self.url = "https://autofarmsupport.tk"
		elif server == 2: self.url = "https://afbot.dev"
		else:
			for url in ['https://autofarmsupport.tk/check', 'https://afbot.dev/check']:
				if get(url, params={'id': self.ID}, timeout=30).ok:
					self.url = url[:-6]
					break
			if not self.url:
				self.url = "https://autofarmsupport.tk/check"
		print(self.url)
	def solve(self, Json):
		Json['id'] = self.ID
		result = post(self.url, json=Json, timeout=300)
		if result.ok:
			return result.json()
		elif result.status_code == 401:
			return False

	def report(self, Json):
		Json['id'] = self.ID
		post(self.url + "/report", json=Json, timeout=120)
