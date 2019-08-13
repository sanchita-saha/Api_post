import requests
import json, ast
from st2common.runners.base_action import Action
class book(Action):
	def run(self,ID,Title,Description,PageCount,Excerpt,PublishDate):
		book = {"ID": ID, "Title": Title, "Description": Description, "PageCount": PageCount, "Excerpt": Excerpt, "PublishDate": PublishDate}
		#print(book)
		resp = requests.post('http://fakerestapi.azurewebsites.net/api/Books', json=book)
		if resp.status_code != 201:
			jdata = ast.literal_eval(json.dumps(resp.json()))
			print(jdata)