import pytest
import pandas as pd
from data_handler import load_data, summarize_data, filter_by_price, export_to_json

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'id': [1, 2],
        'name': ['Cozy Apartment', 'Luxury Loft'],
        'price': [100, 300],
        'neighbourhood': ['Downtown', 'Uptown'],
        'room_type': ['Entire home', 'Private room']
    })

def test_load_data_returns_dataframe():
    df = load_data()
    assert isinstance(df, pd.DataFrame)

def test_load_data_not_empty():
    df = load_data()
    assert not df.empty

def test_filter_price_valid(sample_df):
    filtered = filter_by_price(sample_df, 50, 200)
    assert len(filtered) == 1

def test_filter_price_empty(sample_df):
    filtered = filter_by_price(sample_df, 400, 500)
    assert len(filtered) == 0

def test_filter_price_all(sample_df):
    filtered = filter_by_price(sample_df, 50, 500)
    assert len(filtered) == 2

def test_export_json(tmp_path, sample_df):
    filename = str(tmp_path / "test.json")
    export_to_json(sample_df, filename)
    import os
    assert os.path.exists(filename)

def test_export_json_content(tmp_path, sample_df):
    filename = str(tmp_path / "test.json")
    export_to_json(sample_df, filename)
    assert open(filename).read() != ""

def test_summarize_data(sample_df):
    summary = summarize_data(sample_df)
    assert 'price' in summary

def test_summarize_data_returns_dict(sample_df):
    summary = summarize_data(sample_df)
    assert isinstance(summary, dict)

def test_load_data_has_price_column():
    df = load_data()
    assert 'price' in df.columns
