from flask import Flask, render_template, request
from load_data import tree, df_goalscorers, df_assists
import plotly.graph_objects as go

app = Flask(__name__)


def by_team():
    teams = {}
    for team in tree['children']:
        teams[team['name']] = len(team['children'])
    x_vals = []
    y_vals = []
    for key in teams:
        x_vals.append(key)
        y_vals.append(teams[key])
    bars_data = go.Bar(x=x_vals, y=y_vals, text=y_vals, textposition='auto')
    fig = go.Figure(data=bars_data)
    div = fig.to_html(full_html=False)
    return div


def by_nationality():
    countries = {}
    for team in tree['children']:
        for player in team['children']:
            country = player['details']['nationality']
            if country not in countries.keys():
                countries[country] = 1
            else:
                countries[country] += 1
    x_vals = []
    y_vals = []
    for key in countries:
        x_vals.append(key)
        y_vals.append(countries[key])
    bars_data = go.Bar(x=x_vals, y=y_vals, text=y_vals, textposition='auto')
    fig = go.Figure(data=bars_data)
    div = fig.to_html(full_html=False)
    return div


def by_position():
    positions = {}
    for team in tree['children']:
        for player in team['children']:
            position = player['details']['position']
            if position not in positions.keys():
                positions[position] = 1
            else:
                positions[position] += 1
    x_vals = []
    y_vals = []
    for key in positions:
        x_vals.append(key)
        y_vals.append(positions[key])
    bars_data = go.Bar(x=x_vals, y=y_vals, text=y_vals, textposition='auto')
    fig = go.Figure(data=bars_data)
    div = fig.to_html(full_html=False)
    return div


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/tree')
def show_tree():
    parent = (tree['name'], tree['details']['logo'])
    children = [
        (
            team['name'],
            team['id'],
            [
                (
                    player['name'],
                    player['id'],
                    player['details']['position']
                ) for player in team['children']
            ]
        ) for team in tree['children']
    ]
    return render_template('tree.html', parent=parent, children=children)


@app.route('/league')
def show_league():
    name = tree['name']
    country = tree['details']['country']
    logo = tree['details']['logo']
    flag = tree['details']['flag']
    season = tree['details']['season']
    return render_template('league.html', name=name, country=country, logo=logo, flag=flag, season=season)


@app.route('/team/<team_id>')
def show_team(team_id):
    for team in tree['children']:
        if team['id'] == int(team_id):
            rank = team['details']['rank']
            name = team['name']
            logo = team['details']['logo']
            played = team['details']['played']
            win = team['details']['win']
            draw = team['details']['draw']
            lose = team['details']['lose']
            goals_for = team['details']['goals_for']
            goals_against = team['details']['goals_against']
            goalsDiff = team['details']['goalsDiff']
            points = team['details']['points']
            description = team['details']['description']
            return render_template('team.html', rank=rank, name=name, logo=logo, played=played,
                                   win=win, draw=draw, lose=lose,
                                   goals_for=goals_for, goals_against=goals_against, goalsDiff=goalsDiff,
                                   points=points, description=description, id=team_id)


@app.route('/player/<player_id>')
def show_player(player_id):
    for team in tree['children']:
        for player in team['children']:
            if player['id'] == int(player_id):
                photo = player['details']['photo']
                name = player['name']
                position = player['details']['position']
                age = player['details']['age']
                nationality = player['details']['nationality']
                height = player['details']['height']
                weight = player['details']['weight']
                played = player['details']['matches_played']
                lineups = player['details']['lineups']
                minutes = player['details']['minutes']
                rating = player['details']['rating']
                return render_template('player.html', photo=photo, name=name,
                                       position=position, age=age, nationality=nationality,
                                       height=height, weight=weight,
                                       played=played, lineups=lineups, minutes=minutes, rating=rating)


@app.route('/team/<team_id>/players')
def show_team_players(team_id):
    for team in tree['children']:
        if team['id'] == int(team_id):
            name = team['name']
            players = team['children']
            return render_template('team_players.html', name=name, players=players)


@app.route('/standings')
def show_standings():
    teams = tree['children']
    return render_template('standings.html', teams=teams)


@app.route('/scorers')
def show_scorers():
    table = df_goalscorers.to_html(index=False)
    return render_template('scorers.html', table=table)


@app.route('/assists')
def show_assists():
    table = df_assists.to_html(index=False)
    return render_template('assists.html', table=table)


@app.route('/choose')
def choose_visual():
    return render_template('choose.html')


@app.route('/visual', methods=['POST'])
def show_visual():
    visual = request.form['visual']
    tp = "team"
    if visual == "team":
        plot_div = by_team()
    elif visual == "nationality":
        plot_div = by_nationality()
        tp = "nationality"
    else:
        plot_div = by_position()
        tp = "position"
    return render_template('visual.html', plot_div=plot_div, type=tp)


if __name__ == '__main__':
    app.run()
