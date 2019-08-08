import requests
from st2common.runners.base_action import Action
class book(Action):
	def run(self, book):
		book = {"Content-Type": "application/json", "Accept": "application/json" , 'book': book}
		resp = requests.post('http://fakerestapi.azurewebsites.net/api/Books', json=book)
		if resp.status_code != 201:
				print(resp.json())