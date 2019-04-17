#pip install nba_api
import requests

from nba_api.stats.endpoints import playercareerstats


career = playercareerstats.PlayerCareerStats(player_id='203076')
#print(career.get_data_frames()[0])

from nba_api.stats.static import teams
# get_teams returns a list of 30 dictionaries, each an NBA team.
nba_teams = teams.get_teams()
#print('Number of teams fetched: {}'.format(len(nba_teams)))
for team in nba_teams:
    print(team['abbreviation'])
#dict_keys(['id', 'full_name', 'abbreviation', 'nickname', 'city', 'state', 'year_founded'])

from nba_api.stats.static import players
# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
#print('Number of players fetched: {}'.format(len(nba_players)))
nba_players[:5]
#print(nba_players)

spurs = [team for team in nba_teams
         if team['full_name'] == 'San Antonio Spurs'][0]

#print(type(spurs))

big_fundamental = [player for player in nba_players
                   if player['full_name'] == 'Tim Duncan'][0]

#print(big_fundamental['id'])

#print(players.find_players_by_first_name('lebron'))

#print(teams.find_teams_by_state('ohio'))

#print(big_fundamental)



# Basic Request
from nba_api.stats.endpoints import commonplayerinfo

player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
player_dic = player_info.available_seasons.get_dict()

#print(player_dic)
print(player_info.common_player_info.get_data_frame())
