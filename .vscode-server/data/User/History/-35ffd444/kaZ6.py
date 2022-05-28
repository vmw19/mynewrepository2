import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users"


def get_user(pk):
    url = "%/%" % (URL, pk)
    response = requests.get(url)
    if resonse.status_code ==200:
        pprint(response.json())
    else:
        print("Something went wrong with retrieving the target user.")

def delete_user(pk):
    url = "%/%" % (URL, pk)
    response =requests.delete(url)
    if response.status_code ==204:
        
