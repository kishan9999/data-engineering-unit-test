from data_process import load_csv, clean_data, transform_data
import pandas as pd
# pip install pytest-mock

def test_load_csv(mocker):
    # Mock the pd.read_csv method
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}))

    # Call the load_csv function
    df = load_csv('dummy_path.csv')

    print(df.head())
    
    # Validate the returned DataFrame
    assert not df.empty
    assert list(df.columns) == ['col1', 'col2']
    assert df.shape == (2, 2)
    
def test_clean_data():
    # Create a sample DataFrame
    data = {'col1': [' a', 'b ', None], 'col2': [1, None, 3]}
    df = pd.DataFrame(data)
    
    # Clean the data
    cleaned_df = clean_data(df)
    
    # Validate the cleaned DataFrame
    assert cleaned_df.isna().sum().sum() == 0
    assert cleaned_df.shape == (1, 2)
    assert cleaned_df['col1'].iloc[0] == 'a'


def test_transform_data():
    # Create a sample DataFrame
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)
    
    # Transform the data
    transformed_df = transform_data(df)
    
    # Validate the transformed DataFrame
    assert 'col_sum' in transformed_df.columns
    assert transformed_df['col_sum'].iloc[0] == 4
    assert transformed_df['col_sum'].iloc[1] == 6

# pytest test_data_process.py -s