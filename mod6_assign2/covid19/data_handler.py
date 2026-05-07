import pandas as pd

def load_data():
    return pd.DataFrame({
        'date': ['2023-01-01', '2023-01-08', '2023-01-15'],
        'country': ['USA', 'USA', 'USA'],
        'cases': [1000, 1500, 1200],
        'deaths': [50, 75, 60]
    })

def summarize_data(df):
    return df.describe().to_dict()

def filter_by_date(df, start_date, end_date):
    return df[(df['date'] >= start_date) & (df['date'] <= end_date)]

def weekly_report(df):
    df['date'] = pd.to_datetime(df['date'])
    return df.groupby(pd.Grouper(key='date', freq='W'))['cases'].sum().to_dict()
