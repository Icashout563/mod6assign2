import pytest
import pandas as pd
from data_handler import load_data, summarize_data, filter_by_date, weekly_report

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'date': ['2023-01-01', '2023-01-08', '2023-01-15'],
        'country': ['USA', 'USA', 'USA'],
        'cases': [1000, 1500, 1200],
        'deaths': [50, 75, 60]
    })

def test_load_data_returns_dataframe():
    df = load_data()
    assert isinstance(df, pd.DataFrame)

def test_load_data_not_empty():
    df = load_data()
    assert not df.empty

def test_filter_by_date_valid(sample_df):
    filtered = filter_by_date(sample_df, '2023-01-01', '2023-01-08')
    assert len(filtered) == 2

def test_filter_by_date_empty(sample_df):
    filtered = filter_by_date(sample_df, '2024-01-01', '2024-12-31')
    assert len(filtered) == 0

def test_filter_by_date_all(sample_df):
    filtered = filter_by_date(sample_df, '2023-01-01', '2023-12-31')
    assert len(filtered) == 3

def test_export_json(tmp_path, sample_df):
    filename = str(tmp_path / "test.json")
    sample_df.to_json(filename, orient='records')
    import os
    assert os.path.exists(filename)

def test_export_json_content(tmp_path, sample_df):
    filename = str(tmp_path / "test.json")
    sample_df.to_json(filename, orient='records')
    assert open(filename).read() != ""

def test_summarize_data(sample_df):
    summary = summarize_data(sample_df)
    assert 'cases' in summary

def test_summarize_data_returns_dict(sample_df):
    summary = summarize_data(sample_df)
    assert isinstance(summary, dict)

def test_load_data_has_cases_column():
    df = load_data()
    assert 'cases' in df.columns
