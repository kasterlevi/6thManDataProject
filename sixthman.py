import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playbyplay
import numpy as np
import time
from statistics import mode

# Initializations
nba_teams = teams.get_teams()
season_list = ['2000-01', '2001-02', '2002-03', '2003-04', '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', \
              '2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', \
              '2018-19', '2019-20', '2020-21', '2021-22']


def get_game_ids(team_id, season):
  gamefinder = leaguegamefinder.LeagueGameFinder(
    season_nullable=season,
    season_type_nullable=SeasonType.regular,
    team_id_nullable=team_id)
  time.sleep(1)
  games_dict = gamefinder.get_normalized_dict()
  games = games_dict['LeagueGameFinderResults']
  game_id_list = [(game['GAME_ID'], game['MATCHUP']) for game in games]

  return game_id_list


def get_game_log(game_id):
  # Takes a Tuple of game id and a string of what the matchup is
  # Returns: A Tuple of the game log, and a specification of whether the team we
  #'care' about is home or aaway
  df = playbyplay.PlayByPlay(game_id[0]).get_data_frames()[0]
  time.sleep(1)
  home_away = 'Away' if '@' in game_id[1] else 'Home'
  return (df, home_away)


def get_6th_man(game_log_tuple):
  df = game_log_tuple[0]
  if game_log_tuple[1] == 'Home':
    df = df.loc[df['EVENTMSGTYPE'] == 8,
                ['PCTIMESTRING', 'PERIOD', 'HOMEDESCRIPTION']]
    df = df[df['HOMEDESCRIPTION'].notnull()].reset_index(drop=True)
    df = df[(df[['PCTIMESTRING',
                 'PERIOD']] == df.loc[0,
                                      ['PCTIMESTRING', 'PERIOD']]).all(axis=1)]
    df = df.rename(columns={'HOMEDESCRIPTION': 'DESCRIPTION'})
  else:
    df = df.loc[df['EVENTMSGTYPE'] == 8,
                ['PCTIMESTRING', 'PERIOD', 'VISITORDESCRIPTION']]
    df = df[df['VISITORDESCRIPTION'].notnull()].reset_index(drop=True)
    df = df[(df[['PCTIMESTRING',
                 'PERIOD']] == df.loc[0,
                                      ['PCTIMESTRING', 'PERIOD']]).all(axis=1)]
    df = df.rename(columns={'VISITORDESCRIPTION': 'DESCRIPTION'})
  return [statement.split(' ')[1] if '.' not in statement.split(' ')[1] else \
          (statement.split(' ')[1] + ' ' + statement.split(' ')[2]) for statement in df['DESCRIPTION']]


def return_mode_player(sixth_man_list):
  # NOT COMPLETE!!!
  a = 1
  pass


def main():
  # NOT COMPLETE!!!
  sixth_man_df = pd.DataFrame({'Player': [], 'Season': [], 'Team': []})
  for team in nba_teams:
    for season in season_list:
      game_ids = get_game_ids(team['id'], season)
      game_logs = [get_game_log(game) for game in game_ids]
      sixth_man_list = [get_6th_man(log) for log in game_logs]
      print(sixth_man_list)
