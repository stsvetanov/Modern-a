import pandas as pd


def unique_sales():
    df = pd.read_csv("../sales-001.csv")
    df.columns = ['ID', 'Country', 'City', 'Order_Date', 'Price']

    if df.empty:
        print('INVALID INPUT')
    else:
        data = df.loc[:, ('ID', 'City')]
        data.sort_values('ID', inplace=True)
        data.drop_duplicates(subset='ID', keep=False, inplace=True)

    clean_df = data.groupby(['City'])['ID'].apply(lambda x: ','.join(x)).reset_index()

    final = clean_df.values.tolist()

    if len(final) == 0:
        print('NO UNIQUE SALES')
    else:
        print(*final, sep='\n')


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("unique_sales()", setup="from __main__ import unique_sales", number=100))
