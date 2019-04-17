
from flask import Flask, render_template, session, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import mysql.connector

from leauge_leader_nba import LeagueLeaders
from player_stats import PlayerCareerStats
from common_player import CommonPlayerInfo

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, PerMode48, Scope, Season, SeasonTypeAllStar, StatCategoryAbbreviation, LeagueIDNullable
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
from nba_api.stats.static import teams, players


import json
import requests
import pandas

################################################################################

#Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'adm36'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./nba_players.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#from db import db
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

# engine = create_engine('sqlite://', echo=False)
# engine = create_engine('mysql+mysqlconnector://[user]:[pass]@[host]:[port]/[schema]', echo=False)
# data.to_sql(name='sample_table2', con=engine, if_exists = 'append', index=False)

class NBA_Player(db.Model):
    __tablename__ = "nba_players"
    id = db.Column(db.Integer, primary_key=True)
    playerid = db.Column(db.Integer)
    season = db.Column(db.String(64))
    team = db.Column(db.String(64), db.ForeignKey("nba_teams.abbrev"))
    fg_pct = db.Column(db.Float)
    rebounds = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    points = db.Column(db.Integer)

    def __repr__(self):
        return "{} has been added to your database".format(self.playerid)

class NBA_Team(db.Model):
    __tablename__ = "nba_teams"
    abbrev = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))

    def __repr__(self):
        return "{} has been added to your database".format(self.name)

#########
######### Everything above this line is important/useful setup, not problem-solving.
#########
#
#
# ####################################################################
#
#
# def get_or_create_director(director_name):
#     director = Director.query.filter_by(name=director_name).first()
#     if director:
#         return director
#     else:
#         director = Director(name=director_name)
#         session.add(director)
#         session.commit()
#         return director

nba_players = players.get_players()

#####################################################################
## Main route
#
# @app.route('/')
# def index():
#     movies = Movie.query.all()
#     num_movies = len(movies)
#     return render_template('index.html', num_movies=num_movies)

@app.route('/career_stats/<player_name>/')
def new_player(player_name):
    new_player = [player for player in nba_players
                       if player['full_name'] == player_name][0]
    player_id = new_player['id']
    player = PlayerCareerStats(player_id)
    player_reg_season = player.season_totals_regular_season
    player_data = player_reg_season.get_data_frame()

    for index, row in player_data.iterrows():
        career_player = NBA_Player(playerid = row['PLAYER_ID'],
        season = row['SEASON_ID'],
        team = row['TEAM_ABBREVIATION'],
        fg_pct = row['FG_PCT'],
        rebounds = row['REB'],
        assists = row['AST'],
        points = row['PTS'])
        # )
        session.add(career_player)
        session.commit()

    return render_template("analysis.html", name = player_name, data = player_data)

@app.route('/leaders/<years>/<season_type>/<stat>/')
def league_leader(years, season_type, stat):
    leader = LeagueLeaders(season = years, season_type_all_star = season_type, stat_category_abbreviation = stat)
    league_leaders_data = leader.league_leaders.get_data_frame()

    return render_template("analysis.html", name = years, data = league_leaders_data)


@app.route('/bio/<player_name>/')
def player_bio(player_name):
    # director = get_or_create_director(director)
    new_player = [player for player in nba_players
                       if player['full_name'] == player_name][0]
    player_id = new_player['id']
    player = CommonPlayerInfo(player_id)
    player_data = player.common_player_info.get_data_frame()

    return "Before joinging the NBA, {} played basketball at {}. He was born on {}. While playing in the NBA, his height was {} and his weight was {} pounds.".format(player_name, player_data.at[0,'SCHOOL'], player_data.at[0,'BIRTHDATE'][:10], player_data.at[0,'HEIGHT'],player_data.at[0,'WEIGHT'])

    # return render_template("analysis.html", name = player_name, data = duncan_data )

@app.route('/teams')
def see_all_teams():
    nba_teams = teams.get_teams()
    for team in nba_teams:
        if db.session.query(db.exists().where(NBA_Team.name == team['full_name'])).scalar():
            pass
        else:
            for team in nba_teams:
                add_team = NBA_Team(abbrev = team['abbreviation'],
                name = team['full_name'],
                city = team['city'],
                state = team['state'])
                session.add(add_team)
                session.commit()

    all_teams = NBA_Team.query.all()
    names = []
    for t in all_teams:
        newlist = [t.name,t.city, t.state]
        names.append(newlist) # names will be a list of tuples
    return render_template('all_teams.html',team_names=names)

if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver
