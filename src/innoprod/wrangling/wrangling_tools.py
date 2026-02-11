import pandas as pd

def replace_values(df, colname, old_value, new_value):
    mask = df[colname] == old_value
    df.loc[mask, colname] = new_value
    return df

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
    characterisation = pd.DataFrame(characterisation, columns=['Name', 'Uniqueness', 'Completeness'])
    return characterisation


def is_in_date_format(series: pd.Series):
    if not pd.api.types.is_string_dtype(series):
        return False

def is_non_empty(series: pd.Series):
    # Values cannot be both '' and NaN, so this mask is True only when both are false
    empty_strs = (series == '').fillna(False)
    nan_strs = (series == 'nan').fillna(False)
    return (empty_strs != nan_strs) == (series.isna())

if __name__ == '__main__':
    series = pd.Series(['a', 'b', '', 'd', 'nan'])
    print(is_non_empty(series))