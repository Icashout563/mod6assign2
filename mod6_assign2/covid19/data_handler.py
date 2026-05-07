import pandas as pd

def load_data():
    return pd.DataFrame({"cases": [100, 200, 300]})


import pytest

import pandas as pd

from data_handler import load_data, summarize_data


@pytest.fixture
def sample_df():
    return pd.DataFrame({

        'id': [1, 2],

        'name': ['Cozy Apartment', 'Luxury Loft'],

        'price': [100, 300],

        'neighbourhood': ['Downtown', 'Uptown'],

        'room_type': ['Entire home', 'Private room']

    })


def test_load_data():
    df = load_data()

    assert isinstance(df, pd.DataFrame)

    assert not df.empty


def test_summarize_data():
    df = load_data()

    summary = summarize_data(df)

    assert 'price' in summary


def test_filter_price_valid(sample_df):
    filtered = sample_df[(sample_df['price'] >= 50) & (sample_df['price'] <= 200)]

    assert len(filtered) == 1


def test_filter_price_empty(sample_df):
    filtered = sample_df[(sample_df['price'] >= 400) & (sample_df['price'] <= 500)]

    assert len(filtered) == 0


def test_export_json(tmp_path, sample_df):
    filename = tmp_path / "test.json"

    sample_df.to_json(filename, orient='records')

    assert filename.exists()