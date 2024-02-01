import requests
import vault
import pandas as pd

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



def create_teams(df):
    
    team_columns=df['teams'][2]['visitors'].keys()
    team_df=pd.DataFrame(columns=team_columns)
    
    for match in df["teams"]:
        
        if match['visitors']['id'] not in team_df['id'].values:
            team_df=pd.concat([team_df,pd.DataFrame([match['visitors']])])
            
        if match['home']['id'] not in team_df['id'].values:
            team_df=pd.concat([team_df,pd.DataFrame([match['home']])])

    return team_df