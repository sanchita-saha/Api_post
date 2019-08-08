import requests
from st2common.runners.base_action import Action
class book(Action):
	book = {"Content-Type": "application/json", "Accept": "application/json" , 'book':'LOREM'}
	resp = requests.post('http://fakerestapi.azurewebsites.net/api/Books', json=book)
	if resp.status_code != 201:
			print('Created book. ID: {}'.format(resp.json()[0]))