import pandas as pd

def replace_values(series: pd.Series, old_value, new_value):
    mask = (series == old_value)
    series.loc[mask] = new_value
    return series

def characterise_df_columnwise(df):
    characterisation = []
    for col in df.columns:
        mask = is_non_empty(df[col])
        u = df[mask][col].unique().size
        c = sum(mask)
        N = df[col].size
        var_char = {
            'Name': col,
            # 'Type': 
            'Uniqueness (n)': u,
            'Uniqueness (%)': u / N,
            'Completeness (n)': c,
            'Completeness (%)': c / N
        }
        characterisation.append(var_char)
    characterisation = pd.DataFrame(characterisation, columns=['Name', 'Uniqueness (n)', 'Uniqueness (%)', 'Completeness (n)', 'Completeness (%)'])
    return characterisation

def is_non_empty(series: pd.Series):
    # TODO consider switching isna() for notna()
    empty_strs = (series == '').fillna(False)
    nan_strs = (series == 'nan').fillna(False)
    return (empty_strs != nan_strs) == (series.isna())

def remove_newlines_from_str_series(series: pd.Series.str):
    return series.replace('\n', '', regex=True)

def parse_sterling_monetary_values(series: pd.Series.str):
    series = series.str.replace('£', '')
    series = series.str.replace(',', '')
    series = replace_values(series, '-', None)
    series = replace_values(series, '', None)
    return pd.to_numeric(series)

if __name__ == '__main__':
    series = pd.Series(['a', 'b', '', 'd', 'nan'])
    print(is_non_empty(series))