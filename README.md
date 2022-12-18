# 6thManProject
Hi! Welcome to the README for Sam, Levi, and Nate's 6th Man project! Here we will give an overview of what is included in our repository, and how we suggest you use each of these items. Thank you!

## Kaggle_Competition_Materials Folder
This Folder Contains all of the information pertinent to the Kaggle Compeition. It includes a Kaggler's Guide, all of the CSV's that the Participant has access to, and an example of how someone can participate. This Folder has it's own README, so I would suggest checking that out for more in depth information on everything that this guide includes. 

## Data Folder
This folder contains all of the CSV's that we used to create the final dataset's for the Kaggle Competition. Further descriptions of how we obtained these datasets can be found below, but in short each of these datasets required data manipulation and/or the use of the nba_api to obtain the data. Although we may have the information necessary for you to generate some of these csv's yourself, we do not recommend attempting to replicate the creation of these files on your own. Due to rate limits imposed by nba.com it may take a very long time to generate even a single one of these files. For example, it took multiple days to create sixth_man_data.csv, and it was necessary to wrap the function inside a loop that allowed it to restart if it failed. 

[Nba_api](https://github.com/swar/nba_api) is a great, continuously-updated API which can be used to pull game logs and statistics for all nba teams and players from nba.com. We highly suggest using it for any nba related inquirys that you might have. 

### all_teams_game_logs.csv:

### all_teams_seasons.csv:

### sixth_man_data.csv: 
This CSV contains the information on who each 6th man is for each team and each season since 2000-01. Each row in this CSV represents a player, and the 3 columns, 'Player', 'Season', and 'Team', represent information about that player. 

This CSV can be generated by running the sixth_man_main() function from sixthman.py. If you choose to run this function, we recommend wraping it inside a loop that allows it to re-start if it fails due to API issues. The best location to run this function is in playground.ipynb or from the terminal. 

More information on the specific steps necessary for the generation of this function can be found in sixthman.py
 

### sixth_men_game_logs.csv:

### sixth_men_season_stats.csv:

## playground.ipynb
This notebook is where we tested and ran the functions from sixthman.py and Kaggle_Competition_Materials/Kaggle_Comp.py. Apart from this, the playground represents a place where you can view our thought processes and see how we tested going through the Kaggle Competition as if we were a participant.  Additionally, this playground represents a place where you can examine each of the CSV's described above, and even test out trying to beat the benchmark of the Kaggle competition on your own. 

## poetry.lock and pyproject.toml

## sixthman.py
This file contains the functions necessary for the creation of data/sixth_man_data.csv.

### Functions
sixth_man_main(): This function, which requires no inputs, generates 6th_man_data.csv when it is run. Using the functions described below, it loads in the game logs for each nba team and season. Then, it determines who the 6th man is from each game log. Then it uses this list of 6th men to determine who the overall 6th man is for each team and season. Finally, it adds each 6th man, team, and season to a dataframe that is eventually saved as as sixth_man_data.csv. As noted above, we do not recommend attempting to run this function on your own, due to the long time it takes to complete. 

Initializations: These are not functions, but there are 2 initializations at the top of the page that must be done before any of the functions can be run. These include establishing the list of nba teams from the api, and specifying the list of seasons that we are using. 

get_game_ids(team_id, season): Given a team_id and a season, this function gets all list of "game id's" for that team and year. This is necessary because these game id's are needed to get the game logs from the API.

get_game_log(game_id): Given a GameId, this function returns a tuple of the game log for that game, and whether the team we want the data for was home or away.

get_6th_man(game_log_tuple): Given a game log tuple, this function looks at the game log, and determines who the 6th man was for the team we are hoping to obtain the data for. If multiple people checked into the game at the same time, then they are all considered the 6th man for that game. 

return_mode_player(sixth_man_list): Given a list of who the sixth man was for all of a team's games, this function determines who was the 6th man the most times. If multiple people tie for doing this the most times, then they are all considered the overall 6th man for that team and year.

add_to_list(sixth_men_mode, sixth_man_df_list, season, team): Given the overall 6th man for a team, the season, the team, and a list of previous 6th men that we have found, this function adds an additional row to the list of overall 6th men. 

check_sixth_man_df_exists(): This is a setup function that is used to determine whether there is already a csv called sixth_man_data.csv present. If there is not one, then it creates and saves one. If this function is present, then it loads this CSV and appends the new rows to this already created CSV. 

get_team_and_year(nba_teams, season_list, sixth_man_df_list): This function is used if we try to run sixth_man_main() when there is already a csv called sixth_man_data.csv present. The purpose of this function is to determine what team and season we need to find the next overall 6th man for. In other words, this function lets us know where sixth_man_data.csv was last left left off. 
