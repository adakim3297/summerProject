import importlib
import requests
import json
import bs4

def login(id, password):
    url = 'https://hisnet.handong.edu/login/_login.php' 
    s = requests.Session()
    payload = {  
        'id' : id,
        'password' : password
    }
    res = s.post(url, data=payload)
    
    print(res.text)
    return s

sesstion = login('rlarkfbs', '134679rla!@!')