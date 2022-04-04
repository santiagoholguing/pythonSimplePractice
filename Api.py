import requests
import json
from pprint import pprint



url = "https://jsonplaceholder.typicode.com/todos/1"


#GET
print("--------Get Example--------------------")
response =requests.get(url)
pprint(response.json())
pprint(response.status_code)
print("----------------End-------------------- \n\n\n")


##POST
print("--------Post Example--------------------")
api_url = "https://jsonplaceholder.typicode.com/todos"
todo ={"userId":"abc", "title": "santiago holguin giraldo", "completed": False} #collection
response = requests.post(api_url, json=todo)
pprint(response.json())
pprint(response.status_code)
print("----------------End--------------------\n\n\n")




#PUT
#before
print("--------Put Example--------------------")
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
pprint(response.json())


#after
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
pprint(response.json())
print("----------------End--------------------\n\n\n")



print("--------Patch Example--------------------")
#PATCH
api_url = "https://jsonplaceholder.typicode.com/todos/10"

todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
pprint(response.json())

print("----------------End--------------------\n\n\n")




print("--------Delete Example--------------------")
#DELETE
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
pprint(response.json())
print("----------------End--------------------\n\n\n")