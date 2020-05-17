import pandas as pd

# read csv
df=pd.read_csv('game_data.csv')

# descirbe df
#print(df.describe())

# remove non-int values from game-id
df['game_id']=pd.to_numeric(df['game_id'], errors='coerce', downcast='signed')

# replace na with average of previous and next game_id
df['game_id'] = (df['game_id'].ffill()+df['game_id'].bfill())/2
df['game_id'] = df['game_id'].bfill().ffill()

# cast as int
df['game_id']=df['game_id'].astype(int)
# renaming column to col to avoid conflict in postgres
df.rename(columns={'column': 'col'}, inplace=True)

df.to_csv('game_data_proc.csv', index=False)
