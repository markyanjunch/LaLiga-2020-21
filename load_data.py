from utils import *
from api_cache import get_league, get_players
from scrape_cache import get_goalscorers, get_assists


def get_tree():
    try:
        treeFile = open('data/tree.json', 'r')
        contents = treeFile.read()
        tree = json.loads(contents)
        treeFile.close()
    except:
        # Construct the tree using the data from the API
        # Root is the league node, second level are team nodes, leaves are player nodes
        LaLiga20 = get_league()['response'][0]['league']
        root = LeagueNode()
        root.set_league(LaLiga20)
        # Load team nodes (children) to the root league
        TEAMS = [standings for standings in LaLiga20['standings'][0]]
        TEAM_NODES = []
        for TEAM in TEAMS:
            teamnode = TeamNode()
            teamnode.set_team(TEAM)
            root.set_child(teamnode)
        # Load player nodes (children) to each team node
        for t in root.teams:
            team_id = t.id
            players_list = get_players(team=team_id)
            for player in players_list:
                playernode = PlayerNode()
                playernode.set_player(player)
                t.set_child(playernode)
        # get the tree
        tree = Construct_Tree(root)
    return tree


# Either load the tree from json file or construct a new tree
tree = get_tree()
# Load scraped data from the Wikipedia page
df_goalscorers = get_goalscorers()
df_assists = get_assists()
