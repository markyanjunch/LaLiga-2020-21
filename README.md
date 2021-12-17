# La Liga 2020-21
*Final Project for SI507 Intermediate Programming @ Umich*

## Overview 
<img src="images/LaLiga_Santander.png" width="100" align="right">

[La Liga](https://www.laliga.com/en-US) is the men's top professional football division of the Spanish football league system.

In this project, I collected La Liga 2020-21 season data from multiple sources, and processed them into a tree structure. A flask app is created to provide interactive data presentations.

## Code Usage
To run the app locally, download this repo to your local environment. 

### secrets.py
An API key is needed to access [API-FOOTBALL](https://www.api-football.com).
Store your API key in a new file called secrets.py:
```python
x_apisports_key = '<your api-key>'
```
**For SI507 teaching team, kindly use the secrets.py which I submitted on Canvas.**
### Packages
Required packages for the project are listed in [requirements.txt](requirements.txt):
```text
requests>=2.26.0
bs4>=0.0.1
pandas>=1.3.4
Flask>=2.0.2
beautifulsoup4>=4.10.0
plotly>=5.4.0
```
You can install the packages in the command line using:
```commandline
pip install -r requirements.txt
```

### Run Application
After getting secrets.py in the code folder and having all required pakage installed, in the terminal, run:
```commandline
python laliga.py
```
You will see something like:
```commandline
 * Serving Flask app 'laliga' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
In your browser, visit http://127.0.0.1:5000/ to start playing with the app!

## Data Sources
1. API-FOOTBALL: https://www.api-football.com/  
The API is a RESTFUL API for football data. It is used to get information of the league, teams and players. 
Methods to access and cache the data are included in [api_cache.py](api_cache.py).  
Cached files are stored under [data](data) folder:  
[teams_cache.json](data/teams_cache.json) contains information of the league and all the 20 teams.  
Players data for each team are stored in **players_cache_<team_id>.json** with corresponding team ids.  
**More details please see the Project Document I submitted on Canvas.**

2. 2020–21 La Liga Wikipedia page: https://en.wikipedia.org/wiki/2020%E2%80%9321_La_Liga  
This is the Wikipedia page for La Liga 2020-21 season. 
It is used to get information of top goal scorers and top assist in that match season.  
These two tables are scraped and cached using the methods in [scrape_cache.py](scrape_cache.py).  
Cached files are stored under [data](data/) folder:  
[goalscorers.csv](data/goalscorers.csv) stores the Top goalscorers table under [Season statistics](https://en.wikipedia.org/wiki/2020%E2%80%9321_La_Liga#Season_statistics) section.  
[assists.csv](data/assists.csv) stores the Top assists table under [Season statistics](https://en.wikipedia.org/wiki/2020%E2%80%9321_La_Liga#Season_statistics) section.  
**More details please see the Project Document I submitted on Canvas.**

