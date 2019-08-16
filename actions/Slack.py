import requests
import json, ast
from st2common.runners.base_action import Action
class book(Action):
	def run(self,messege):
		book = {"text": messege}
		#print(book)
		resp = requests.post('https://hooks.slack.com/services/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', json=book)
		if resp.status_code != 201:
			#jdata = ast.literal_eval(json.dumps(resp.json()))
			print('mayukh pagol')