import pandas as pd
pth="./movie_metadata.csv"
movies=pd.read_csv(pth)
print('Columns: %d\nRows: %d' %(movies.shape[1],movies.shape[0]))
print(movies.columns)
print(movies.loc[:,'country'].value_counts())
BG_filter=movies.loc[:,'country']=='Bulgaria'
BG_filtered_rows=movies[BG_filter].shape
BG_filtered=movies.loc[BG_filter,['movie_title','country']]
print(BG_filtered)
print(BG_filtered_rows)