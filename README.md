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
This CSV contains the information on who each 6th man is for each team and each season. There are 683 total players included in this

### sixth_men_game_logs.csv:

### sixth_men_season_stats.csv:

## playground.ipynb
This notebook is where we tested and ran the functions from sixthman.py and Kaggle_Competition_Materials/Kaggle_Comp.py. Apart from this, the playground represents a place where you can view our thought processes and see how we tested going through the Kaggle Competition as if we were a participant.  Additionally, this playground represents a place where you can examine each of the CSV's described above, and even test out trying to beat the benchmark of the Kaggle competition on your own. 

## poetry.lock and pyproject.toml

## sixthman.py

