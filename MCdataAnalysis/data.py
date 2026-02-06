import pandas as pd

df = pd.read_csv('MCdataAnalysis/f1_data.csv')
df.head()

# removes weird characters or spaces.
df['winner_name'] = df['winner_name'].str.replace('Â','').str.strip()
df['team'] = df['team'].str.strip()

target_teams = ['McLaren', 'McLaren Mercedes', 'McLaren Ford', 'McLaren TAG', 'McLaren Honda']

result = df.query("time < '2:02:30' and team in @target_teams and winner_name == 'Lando Norris'")

# Group by driver, count the dates they won, and sort from highest to lowest
# leaderboard = df.groupby('winner_name')['date'].count().sort_values(ascending=False)
# print(leaderboard.head(50))

print(result)