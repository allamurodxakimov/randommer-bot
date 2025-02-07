import requests
from .randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        endpoint = "Name"
        url  = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        params = {
            "nameType":nameType,"quantity":quantity
        }
        respons = requests.get(url, params=params,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
        
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        endpoint = "Name/Suggestions"
        url  = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        params = {
            "startingWords":startingWords
        }
        respons = requests.get(url, params=params,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        endpoint = "Name/Cultures"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        respons = requests.get(url=url,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code