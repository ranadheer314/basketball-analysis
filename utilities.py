import requests
import vault

def get_response(url,query):
    #url = "https://api-nba-v1.p.rapidapi.com/seasons"

    headers = {
        "X-RapidAPI-Key": vault.key,
        "X-RapidAPI-Host": vault.host
    }

    return requests.get(url, headers=headers, params=query)


def get_teams(response):
    list_1=[]
    for i in range(len(response.json()['response'])):
        visitors=response.json()['response'][i]['teams']['visitors']['name']
        home=response.json()['response'][i]['teams']['home']['name']
        list_1.append([visitors,home])
    return list_1
