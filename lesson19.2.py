import pandas as pd

# Import the dataset
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
df = pd.read_csv(url)

# Select Team, Yellow Cards, and Red Cards columns
selected_columns = df[["Team", "Yellow Cards", "Red Cards"]]

# How many teams participated in the Euro2012?
num_teams = selected_columns.shape[0]

# Filter teams that scored more than 6 goals
high_scoring_teams = df[df["Goals"] > 6]

print("Selected Columns:")
print(selected_columns)

print("Number of Teams Participated in Euro2012:", num_teams)

print("Teams that Scored More Than 6 Goals:")
print(high_scoring_teams)