import pandas as pd

from innoprod.text_analysis import matching_status

def add_code(code_name, code_patterns, codes_df, recurring_sentences_df):
    
    # Register the new code in the codes dataframe
    single_code_df = pd.DataFrame({'Code': [code_name], 'Patterns': [code_patterns]})
    if codes_df is None:
        codes_df = single_code_df.copy()
    elif code_name in codes_df['Code'].values:
        return modify_code(code_name, code_patterns, codes_df, recurring_sentences_df)
    else:
        codes_df = pd.concat([codes_df, single_code_df], ignore_index=True)
    
    # Assess the impact of the new code on the sentences dataframe
    # TODO does not yet handle regular expressions
    matches = recurring_sentences_df['Cleaned Sentence'].apply(lambda x: any(pattern in x for pattern in code_patterns))

    # Insert the matches into the sentences dataframe
    recurring_sentences_df[code_name] = matches.map(matching_status.initial_map)

    return codes_df, recurring_sentences_df


def modify_code(code_name, code_patterns, codes_df, recurring_sentences_df):

    # TODO update the code_df 

    matches = recurring_sentences_df['Cleaned Sentence'].apply(lambda x: any(pattern in x for pattern in code_patterns))

    new_statuses = [matching_status.update_status(current_status, new_match) for current_status, new_match in zip(recurring_sentences_df[code_name], matches)]

    recurring_sentences_df[code_name] = new_statuses

    return codes_df, recurring_sentences_df

