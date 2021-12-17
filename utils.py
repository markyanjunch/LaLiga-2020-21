import json


class LeagueNode:
    def __init__(self, id=140, name="La Liga", country="Spain",
                 logo=None, flag=None, season=2020, teams=None):
        # primary information of league
        self.id = id
        self.name = name

        # detailed league information
        self.details = {'country': country, 'logo': logo, 'flag': flag, 'season': season}

        # list of children nodes
        if teams is None:
            teams = []
        self.teams = teams

    def set_league(self, league):
        self.id = league['id']
        self.name = league['name']
        self.details['country'] = league['country']
        self.details['logo'] = league['logo']
        self.details['flag'] = league['flag']
        self.details['season'] = league['season']

    def set_child(self, team_node):
        self.teams.append(team_node)


class TeamNode:
    def __init__(self, rank=None, id=None, name=None, logo=None,
                 played=38, win=None, draw=None, lose=None,
                 goals_for=None, goals_against=None, goalsDiff=None,
                 points=None, description=None,
                 players=None):
        # primary information of team
        self.id = id
        self.name = name

        # detailed team information
        self.details = {'rank': rank, 'logo': logo, 'played': played, 'win': win, 'draw': draw, 'lose': lose,
                        'goals_for': goals_for, 'goals_against': goals_against, 'goalsDiff': goalsDiff,
                        'points': points, 'description': description}

        # list of children nodes
        if players is None:
            players = []
        self.players = players

    def set_team(self, team):
        self.id = team['team']['id']
        self.name = team['team']['name']
        self.details['rank'] = team['rank']
        self.details['logo'] = team['team']['logo']
        self.details['played'] = team['all']['played']
        self.details['win'] = team['all']['win']
        self.details['draw'] = team['all']['draw']
        self.details['lose'] = team['all']['lose']
        self.details['goals_for'] = team['all']['goals']['for']
        self.details['goals_against'] = team['all']['goals']['against']
        self.details['goalsDiff'] = team['goalsDiff']
        self.details['points'] = team['points']
        if team['description'] is None:
            self.details['description'] = ""
        else:
            self.details['description'] = team['description']

    def set_child(self, player_node):
        self.players.append(player_node)


class PlayerNode:
    def __init__(self, id=None, name=None, age=None, nationality=None,
                 height=None, weight=None, photo=None,
                 matches_played=0, lineups=0, minutes=0, position=None,
                 rating=None):
        # primary information of player
        self.id = id
        self.name = name

        # detailed player information
        self.details = {'age': age, 'nationality': nationality, 'height': height, 'weight': weight, 'photo': photo,
                        'matches_played': matches_played, 'lineups': lineups, 'minutes': minutes, 'position': position,
                        'rating': rating}

    def set_player(self, player):
        self.id = player['player']['id']
        self.name = player['player']['name']
        self.details['age'] = player['player']['age']
        self.details['nationality'] = player['player']['nationality']
        if player['player']['height'] is None:
            self.details['height'] = ""
        else:
            self.details['height'] = player['player']['height']
        if player['player']['weight'] is None:
            self.details['weight'] = ""
        else:
            self.details['weight'] = player['player']['weight']
        self.details['photo'] = player['player']['photo']
        self.details['matches_played'] = player['statistics'][0]['games']['appearences']
        self.details['lineups'] = player['statistics'][0]['games']['lineups']
        self.details['minutes'] = player['statistics'][0]['games']['minutes']
        self.details['position'] = player['statistics'][0]['games']['position']
        if player['statistics'][0]['games']['rating'] is None:
            self.details['rating'] = ""
        else:
            self.details['rating'] = player['statistics'][0]['games']['rating']


# Load the tree structure into json file
def Construct_Tree(root):
    tree = {
        'NodeType': 'LeagueNode',
        'id': root.id,
        'name': root.name,
        'details': root.details,
        'children': [
            {
                'NodeType': 'TeamNode',
                'id': team.id,
                'name': team.name,
                'details': team.details,
                'children': [
                    {
                        'NodeType': 'PlayerNode',
                        'id': player.id,
                        'name': player.name,
                        'details': player.details
                    }
                    for player in team.players
                ]
            }
            for team in root.teams
        ]
    }
    with open('data/tree.json', "w") as treeFile:
        json.dump(tree, treeFile)
    return tree
