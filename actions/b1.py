import requests
from st2common.runners.base_action import Action
class MyEchoAction(Action):
	book = {"summary": "Take out trash", "description": "" }
	resp = requests.post('https://todolist.example.com/tasks/', json=book)
	if resp.status_code != 201:
			raise ApiError('POST /tasks/ {}'.format(resp.status_code))
			print('Created book. ID: {}'.format(resp.json()["id"]))