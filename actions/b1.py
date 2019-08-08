import requests
from st2common.runners.base_action import Action
class book(Action):
	def run(self, book):
		book = {{"ID": 0, "Title": "string", "Description": "string", "PageCount": 0, "Excerpt": "string", "PublishDate": "2019-08-07T11:05:53.591Z"}}
		resp = requests.post('http://fakerestapi.azurewebsites.net/api/Books', json=book)
		if resp.status_code != 201:
				print(resp.json())