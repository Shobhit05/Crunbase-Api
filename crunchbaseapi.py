import requests
import pprint
import json
import time
import datetime



class CrunchBase():

    def __init__(self,key):
        self.Base_Url="https://api.crunchbase.com/v3/odm-organizations?user_key="+key
        self.key=key


    def domain_name_search(self,url):
        new_url=str(self.Base_Url+"&domain_name=\'"+url+"\'")
        req=requests.get(new_url)
        json_data = json.loads(req.text)
        return(json_data)

    def updated_companies(self):
        epoch_date=str(int(datetime.datetime.now().timestamp()))
        req=requests.get("https://api.crunchbase.com/v3/odm-organizations?user_key=d900b3954e457c3d7491c2ed79ba2b93&updated_since="+epoch_date)
        json_data = json.loads(req.text)
        return(json_data)

    def get_company_people(self,name):
        url1= str("https://api.crunchbase.com/v3/odm-people?user_key="+self.key+"&query="+name)
        req1=requests.get(url1)
        json_data1 = json.loads(req1.text)
        pprint.pprint(json_data1)
        
        
        

