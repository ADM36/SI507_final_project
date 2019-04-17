from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import PerMode36, LeagueIDNullable
from nba_api.stats.library.parameters import LeagueID, PerMode48, Scope, Season, SeasonTypeAllStar, StatCategoryAbbreviation

import json
import requests
import pandas



#####################################

class CommonPlayerInfo(Endpoint):
    endpoint = 'commonplayerinfo'
    expected_data = {'AvailableSeasons': ['SEASON_ID'], 'CommonPlayerInfo': ['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION', 'HEIGHT', 'WEIGHT', 'SEASON_EXP', 'JERSEY', 'POSITION', 'ROSTERSTATUS', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'TEAM_CITY', 'PLAYERCODE', 'FROM_YEAR', 'TO_YEAR', 'DLEAGUE_FLAG', 'NBA_FLAG', 'GAMES_PLAYED_FLAG', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER'], 'PlayerHeadlineStats': ['PLAYER_ID', 'PLAYER_NAME', 'TimeFrame', 'PTS', 'AST', 'REB', 'PIE']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 player_id,
                 league_id_nullable=LeagueIDNullable.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'PlayerID': player_id,
                'LeagueID': league_id_nullable
        }
        if get_request:
            self.get_request()

    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.available_seasons = Endpoint.DataSet(data=data_sets['AvailableSeasons'])
        self.common_player_info = Endpoint.DataSet(data=data_sets['CommonPlayerInfo'])
        self.player_headline_stats = Endpoint.DataSet(data=data_sets['PlayerHeadlineStats'])



#########################################

class LeagueLeaders(Endpoint):
    endpoint = 'leagueleaders'
    expected_data = {'LeagueLeaders': ['PLAYER_ID', 'RANK', 'PLAYER', 'TEAM', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'EFF', 'AST_TOV', 'STL_TOV']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 per_mode48=PerMode48.default,
                 scope=Scope.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 stat_category_abbreviation=StatCategoryAbbreviation.default,
                 active_flag_nullable='',
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'LeagueID': league_id,
                'PerMode': per_mode48,
                'Scope': scope,
                'Season': season,
                'SeasonType': season_type_all_star,
                'StatCategory': stat_category_abbreviation,
                'ActiveFlag': active_flag_nullable
        }
        if get_request:
            self.get_request()

    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.league_leaders = Endpoint.DataSet(data=data_sets['LeagueLeaders'])


########################################

class PlayerCareerStats(Endpoint):
    endpoint = 'playercareerstats'
    expected_data = {'CareerTotalsAllStarSeason': ['PLAYER_ID', 'LEAGUE_ID', 'Team_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], 'CareerTotalsCollegeSeason': ['PLAYER_ID', 'LEAGUE_ID', 'ORGANIZATION_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], 'CareerTotalsPostSeason': ['PLAYER_ID', 'LEAGUE_ID', 'Team_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], 'CareerTotalsRegularSeason': ['PLAYER_ID', 'LEAGUE_ID', 'Team_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], 'SeasonRankingsPostSeason': ['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'RANK_MIN', 'RANK_FGM', 'RANK_FGA', 'RANK_FG_PCT', 'RANK_FG3M', 'RANK_FG3A', 'RANK_FG3_PCT', 'RANK_FTM', 'RANK_FTA', 'RANK_FT_PCT', 'RANK_OREB', 'RANK_DREB', 'RANK_REB', 'RANK_AST', 'RANK_STL', 'RANK_BLK', 'RANK_TOV', 'RANK_PTS', 'RANK_EFF'], 'SeasonRankingsRegularSeason': ['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'RANK_MIN', 'RANK_FGM', 'RANK_FGA', 'RANK_FG_PCT', 'RANK_FG3M', 'RANK_FG3A', 'RANK_FG3_PCT', 'RANK_FTM', 'RANK_FTA', 'RANK_FT_PCT', 'RANK_OREB', 'RANK_DREB', 'RANK_REB', 'RANK_AST', 'RANK_STL', 'RANK_BLK', 'RANK_TOV', 'RANK_PTS', 'RANK_EFF'], 'SeasonTotalsAllStarSeason': ['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], 'SeasonTotalsCollegeSeason': ['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'ORGANIZATION_ID', 'SCHOOL_NAME', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], 'SeasonTotalsPostSeason': ['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'], 'SeasonTotalsRegularSeason': ['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 player_id,
                 per_mode36=PerMode36.default,
                 league_id_nullable=LeagueIDNullable.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'PlayerID': player_id,
                'PerMode': per_mode36,
                'LeagueID': league_id_nullable
        }
        if get_request:
            self.get_request()

    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.career_totals_all_star_season = Endpoint.DataSet(data=data_sets['CareerTotalsAllStarSeason'])
        self.career_totals_college_season = Endpoint.DataSet(data=data_sets['CareerTotalsCollegeSeason'])
        self.career_totals_post_season = Endpoint.DataSet(data=data_sets['CareerTotalsPostSeason'])
        self.career_totals_regular_season = Endpoint.DataSet(data=data_sets['CareerTotalsRegularSeason'])
        self.season_rankings_post_season = Endpoint.DataSet(data=data_sets['SeasonRankingsPostSeason'])
        self.season_rankings_regular_season = Endpoint.DataSet(data=data_sets['SeasonRankingsRegularSeason'])
        self.season_totals_all_star_season = Endpoint.DataSet(data=data_sets['SeasonTotalsAllStarSeason'])
        self.season_totals_college_season = Endpoint.DataSet(data=data_sets['SeasonTotalsCollegeSeason'])
        self.season_totals_post_season = Endpoint.DataSet(data=data_sets['SeasonTotalsPostSeason'])
        self.season_totals_regular_season = Endpoint.DataSet(data=data_sets['SeasonTotalsRegularSeason'])
