# La Liga 2020-21
*Final Project for SI507 Intermediate Programming @ Umich*

## Overview 
<img src="images/LaLiga_Santander.png" width="100" align="right">
La Liga is the men's top professional football division of the Spanish football league system.

In this project, I collect La Liga 2020-21 season data from multiple sources, and process them into a tree structure. A flask app is created to provide interactive data presentations.

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
You can install the packages in command line using:
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