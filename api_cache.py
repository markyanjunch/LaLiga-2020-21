import requests
import json
import time

from secrets import x_apisports_key


def get_league(league=140, season=2020):
    url = "https://v3.football.api-sports.io/standings"
    params = {'league': league, 'season': season}
    headers = {
        'x-apisports-key': x_apisports_key,
    }
    try:
        cache_file = open('data/teams_cache.json', 'r')
        cache_contents = cache_file.read()
        league = json.loads(cache_contents)
        cache_file.close()
    except:
        print("Cache not found, start caching...")
        time.sleep(1)
        response = requests.request("GET", url, headers=headers, params=params)
        league = json.loads(response.text)
        with open('data/teams_cache.json', "w") as league_cache:
            json.dump(league, league_cache)
    return league


def get_players(team, league=140, season=2020):
    url = "https://v3.football.api-sports.io/players"
    params = {'league': 140, 'season': 2020, 'team': team}
    headers = {
        'x-apisports-key': x_apisports_key,
    }
    try:
        cache_file = open(f'data/players_cache_{team}.json', 'r')
        cache_contents = cache_file.read()
        players = json.loads(cache_contents)
        cache_file.close()
    except:
        print("Cache not found, start caching...")
        time.sleep(1)
        response = requests.request("GET", url, headers=headers, params=params)
        page_default = json.loads(response.text)  # default page=1, 20 players per page
        pages = page_default['paging']['total']
        players = page_default['response']
        for p in range(2, pages+1):
            params['page'] = p
            time.sleep(1)
            response = requests.request("GET", url, headers=headers, params=params)
            page_temp = json.loads(response.text)
            players.extend(page_temp['response'])
        with open(f'data/players_cache_{team}.json', "w") as league_cache:
            json.dump(players, league_cache)
    return players
