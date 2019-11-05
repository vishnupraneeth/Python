import requests
import json
def get_resourse():

    BASE_URL="http://127.0.0.1:8000/"
    END_POINT="api/"
    id=input("Enter some id ")
    resp=requests.get(BASE_URL+END_POINT+id+'/')
    print(resp.json())
    print(resp.status_code)

get_resourse()

def get_all():

    BASE_URL="http://127.0.0.1:8000/"
    END_POINT="api/"
    
    resp=requests.get(BASE_URL+END_POINT)
    print(resp.json())
    print(resp.status_code)

get_all()
