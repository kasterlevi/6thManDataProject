# How important are 6th Men to Team Success?
## Summary 
Hello future general managers and NBA Fans, welcome to our Kaggle Compeition!
In this competition you will use use the statistics of all the 6th men since 2000-01 to predict team success, which is quantified by team win percentage. 

We have gone through the game logs of each NBA game in the past two decades, and have kept track of who the first person into the game was for each team. We were then able to calculate who the 6th man was for each team every season. These players have been added to the dataset that you will be using! 

The competition is simple: use the single season 6th man player statistics to predict their team's win percentage! We have provided you with 3 csv files datasets to get started: train.csv, test.csv, and example_submission.csv. Below we go into futher detail about what each of these CSV's contains.

## CSV Description (Availible in Availible_CSVs)

### train.csv:

This CSV contains the season stats for 546 6th men, as well as their team's corresponding win percentage. You will use this information to create a numerical model that takes the player season statistics and then predicts the win percentage of their team. This could be any model of your choosing: linear regression, random forest, a neural network, etc. 

### test.csv:

This CSV contains the season stats for 137 6th men, but does not contain the corresponding win percentage. You will use the model you created using train.csv to create predictions for each of the rows in the CSV. You will then create a two column csv that contains these predictions. The first column will be the player id, and the second column will be the team win percentage prediciton for that player. This csv will then be compared against the actual solutions to determine the success of your model. 

### example_submission.csv:

This CSV contains an example of what the your final submission csv created by running your model on test.csv should look like. As you can see, one column is a list of player id's, and the other column is a list of corresponding win percentage predictions. Here the win percentage predictions are generated randomly. 

## Data Dictionary:

|Column|Definition|
|-----|----|
|MIN|Average Minutes Played Per Game|
|FGM|Average Field Goals Made Per Game|
|FGA|Average Field Goals Attempted Per Game|
|FG3M|Average 3 Pointers Made Per Game|
|FG3A|Average 3 Pointers Attempted Per Game|
|FTM|Average Free Throws Made Per Game|
|FTA|Average Free Throws Attempted Per Game|
|OREB|Average Number of Offensive Rebounds Per Game|
|DREB|Average Number of Defensive Rebounds Per Game|
|REB|Average Number of Rebounds Per Game|
|AST|Average Number of Assists Per Game|
|TOV|Average Number of Turnovers Per Game|
|STL|Average Number of Steals Per Game|
|BLK|Average Number of Blocks Per Game|
|BLKA| |
|PF|Average Number of Personal Fouls Per Game|
|PFD| |
|PTS|Average Number of Points Per Game|
|PLUS_MINUS|Average Plus Minus Per Game|
|Games|Number of Games Played|
|WL|Team Win Percentage (What we want to Predict)|


## How to Participate 
### Create a Model
Using the training dataset that we provide, you should create a model than accuretly predicts win percentage (the column named 'WL'). Once you have a model that makes these predictions, you can make these predictions on the test dataset that we provide you. Once you have these predictions from the test data, you should put this information in a CSV that you can submit to kaggle, following the format of example_submission.csv. 
### Submission of your CSV:
You should submit a csv file with exactly 137 entries plus a header row. Your submission will show an error if you have extra columns (beyond PlayerId and WinPercentage) or rows.

The file should have exactly 2 columns:
- PlayerId (sorted in any order)
- WL (contains your numerical Win percentage predictions, which are values between 0 and 1)

### Evaluation of your submission: 
After your CSV is submitted, your predictions will be compared to the actual predictions to obtain the Mean Absolute Error (MAE) of your model. The benchmark MAE that you should attempt to meet is .066. This is a difficult benchmark to hit; however, through testing we determined that it is possible to meet and even exceed this benchmark using more than one choice of model.  The people who meet this benchmark will be shown on Kaggle, and the top scoring participants will be ranked as well. 

HINT: If you are stuck, try to do some feature selection. 


