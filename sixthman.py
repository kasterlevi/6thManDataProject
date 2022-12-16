import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playbyplay
import numpy as np
import time
from statistics import multimode
import os

# Initializations
nba_teams = teams.get_teams()
season_list = ['2000-01', '2001-02', '2002-03', '2003-04', '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', \
              '2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', \
              '2018-19', '2019-20', '2020-21', '2021-22']


def get_game_ids(team_id, season):
  time.sleep(.6)
  gamefinder = leaguegamefinder.LeagueGameFinder(
    season_nullable=season,
    season_type_nullable=SeasonType.regular,
    team_id_nullable=team_id)
  time.sleep(.6)
  games_dict = gamefinder.get_normalized_dict()
  games = games_dict['LeagueGameFinderResults']
  game_id_list = [(game['GAME_ID'], game['MATCHUP']) for game in games]

  return game_id_list


def get_game_log(game_id):
  # Takes a Tuple of game id and a string of what the matchup is
  # Returns: A Tuple of the game log, and a specification of whether the team we
  #'care' about is home or aaway
  time.sleep(.6)
  df = playbyplay.PlayByPlay(game_id[0]).get_data_frames()[0]
  time.sleep(.6)
  home_away = 'Away' if '@' in game_id[1] else 'Home'
  return (df, home_away)


def get_6th_man(game_log_tuple):
  df = game_log_tuple[0]
  if game_log_tuple[1] == 'Home':
    df = df.loc[df['EVENTMSGTYPE'] == 8,
                ['PCTIMESTRING', 'PERIOD', 'HOMEDESCRIPTION']]
    df = df[df['HOMEDESCRIPTION'].notnull()].reset_index(drop=True)
    print(df)
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
  #print(df)
  return [(statement.split(':')[1]).split('FOR')[0]  for statement in df['DESCRIPTION']]


def return_mode_player(sixth_man_list):
  total_players_list = []
  for value in sixth_man_list:
      for x in value: total_players_list.append(x)
  return multimode(total_players_list)

def add_to_list(sixth_men_mode, sixth_man_df_list, season, team):
    for player in sixth_men_mode:
        sixth_man_df_list.append(pd.DataFrame({'Player': [player], 'Season': [season], 'Team': [team['full_name']]}))
    return sixth_man_df_list

def check_sixth_man_df_exists():
  if os.path.exists('data/sixth_man_data.csv'):
    return [pd.read_csv('data/sixth_man_data.csv')]
  else:
    pd.DataFrame({}).to_csv('data/sixth_man_data.csv')
    return []

def get_team_and_year(nba_teams, season_list, sixth_man_df_list):
    # IF the Df exists
    if len(sixth_man_df_list) == 1:
        df = sixth_man_df_list[0]
        last_team = df.loc[len(df) - 1, 'Team']
        last_season = df.loc[len(df) - 1, 'Season']
        # Get team_list
        for i in range(len(nba_teams)):
            if last_team == nba_teams[i]['full_name']:
                used_team_list = nba_teams[i:]
        # Get correct season_list and update team_list if need be
        if last_season == '2021-22':
            used_season_list = season_list
            used_team_list = used_team_list[1:]
        else: 
            correct_index = season_list.index(last_season)
            used_season_list = season_list[(correct_index+1):]
    # If df does not exist
    else: 
        used_season_list = season_list
        used_team_list = nba_teams

    return used_season_list, used_team_list


def sixth_man_main():
  # NOT COMPLETE!!!
  # This
  sixth_man_df_list = check_sixth_man_df_exists()
  used_season_list, used_team_list = get_team_and_year(nba_teams, season_list, sixth_man_df_list)
  i = 0
  for team in used_team_list:
    if i > 0:
      used_season_list = season_list
    i = i + 1
    for season in used_season_list:
      #print('here')
      game_ids = get_game_ids(team['id'], season)
      game_logs = [get_game_log(game) for game in game_ids]
      sixth_man_list = [get_6th_man(log) for log in game_logs]
      sixth_men_mode = return_mode_player(sixth_man_list)
      sixth_man_df_list = add_to_list(sixth_men_mode, sixth_man_df_list, season, team)
      #print('Updated Happened')
      df = pd.concat(sixth_man_df_list)
      sixth_man_df_list = [df]
      os.remove('data/sixth_man_data.csv')
      df.to_csv('data/sixth_man_data.csv', index=False)
