import pandas as pd

def load_data():
    return pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Cozy Apartment', 'Luxury Loft', 'Beach House'],
        'price': [100, 300, 150],
        'neighbourhood': ['Downtown', 'Uptown', 'Seaside'],
        'room_type': ['Entire home', 'Private room', 'Entire home']
    })

def summarize_data(df):
    return df.describe().to_dict()

def filter_by_price(df, min_price, max_price):
    return df[(df['price'] >= min_price) & (df['price'] <= max_price)]

def export_to_json(df, filename):
    df.to_json(filename, orient='records', indent=2)
    return filename
