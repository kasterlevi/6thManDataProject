# How important are 6th Men to Team Success?
## Summary 
Hello future general managers and NBA Fans, welcome to our Kaggle Compeition!
In this competition you will use use the statistics of all the 6th men since 2000-01 to predict team success, which is quantified by team win percentage. 

We have gone through the game logs of each NBA game in the past two decades, and have kept track of who the first person into the game was for each team. We were then able to calculate who the 6th man was for each team every season. These players have been added to the dataset that you will be using! 

The competition is simple: use the single season 6th man player statistics to predict their team's win percentage! We have provided you with 3 csv files datasets to get started: train.csv, test.csv, and example_submission.csv. Below we go into futher detail about what each of these CSV's contains.

## CSV Description 

### train.csv:

This CSV contains the season stats for ___ 6th men, as well as their team's corresponding win percentage. You will use this information to create a numerical model that takes the player season statistics and then predicts the win percentage of their team. This could be any model of your choosing: linear regression, random forest, a neural network, etc. 

### test.csv:

This CSV contains the season stats for ___ 6th men, but does not contain the corresponding win percentage. You will use the model you created using train.csv to create predictions for each of the rows in the CSV. You will then create a two column csv that contains these predictions. The first column will be the player id, and the second column will be the team win percentage prediciton for that player. This csv will then be compared against the actual solutions to determine the success of your model. 

### example_submission.csv:

This CSV contains an example of what the your final submission csv created by running your model on test.csv should look like. As you can see, the index is a list of player id's, and the other column is a list of corresponding win percentage predictions. Here the win percentage predictions are generated randomly. 

## How to Participate 
### Submission of your CSV:
You should submit a csv file with exactly ___ entries plus a header row. Your submission will show an error if you have extra columns (beyond PlayerId and WinPercentage) or rows.

The file should have exactly 1 column and 1 index:
- Index: PlayerId (sorted in any order)
- Column: WL (contains your numerical predictions: between 0 and 1)

### Evaluation of your submission:



