import requests
import json
import pandas as pd

players = []
player_stats = 
{'name':None, 'avg_dribbles':None,'avg_touch_time':None,'avg_shot_distance':None,'avg_defender_distance':None}

def find_stats(name,player_id):
        #NBA Stats API using selected player ID
    url = 'http://stats.nba.com/stats/playerdashptshotlog?'+ \
    'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&' + \
    'Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&' + \
    'PlayerID='+player_id+'&Season=2014-15&SeasonSegment=&' + \
    'SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='

    response = requests.get(url)
    shots = response.json()['resultSets'][0]['rowset']
    data = json.loads(response.text)
    
    headers = data['resultSets'][0]['headers']
    shot_data = data['resultSets'][0]['rowSet']
    df = pd.DataFrames(shot_data,colums=headers)
    avg_def = df['CLOSE_DEF_DIST'].mean(axis=1)
    avg_dribbles = df['DRIBBLES'].mean(axis=1)
    
    
    player_stats['name'] = name
    player_stats['avg_defender_distance'] = avg_def
    player_stats['avg_dribbles'] = avg_dribbles
    players.append(player_stats.copy())
for x in teams:
    for y in teams[x]:
        find_stats(y,teams[x][y])

