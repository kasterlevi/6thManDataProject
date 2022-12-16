import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playbyplay
import numpy as np
import time
import random
from statistics import multimode
import os
from sklearn.model_selection import train_test_split

def create_player_ids(csv_location):
    '''
    Input: Location of Aggregated Sixth Man Data
    Output: DataFrame with randomized Player ID's, and the name, team, and season removed.
    '''
    df = pd.read_csv(csv_location)
    df = df.sample(frac=1, random_state=10).reset_index(drop=True)
    df.index.name = 'Player ID'
    return df.drop(['PLAYER_NAME', 'Team', 'Season'],axis=1)

def train_test_csvs(df):
    '''
    Input: Sixth Man df with player ID's
    Output in order: train_df, test_df, solution_df
    '''
    y = df['WL']
    X = df.drop(['WL'], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    train_df = X_train.merge(y_train, right_index=True, left_index=True)
    return train_df, X_test, y_test

def generate_example_submission(solution_df):
    random.seed(10)
    example_df = solution_df.to_frame()
    random_values = [random.uniform(0,1) for x in range(len(solution_df))]
    example_df['WL'] = random_values
    return example_df

def save_csvs(train_df, test_df, solution_df, example_df):
    train_df.to_csv('Kaggle_Competition_Materials/Available_CSVs/train.csv')
    test_df.to_csv('Kaggle_Competition_Materials/Available_CSVs/test.csv')
    example_df.to_csv('Kaggle_Competition_Materials/Available_CSVs/example_submission.csv')
    solution_df.to_csv('Kaggle_Competition_Materials/Hidden_CSV/solutions.csv')

def generate_all_csvs():
    df = create_player_ids('data/sixth_men_season_stats.csv')
    train_df, test_df, solution_df = train_test_csvs(df)
    example_df = generate_example_submission(solution_df)
    save_csvs(train_df, test_df, solution_df, example_df)
    
    