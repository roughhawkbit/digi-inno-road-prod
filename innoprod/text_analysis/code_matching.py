import pandas as pd
import re

from innoprod.text_analysis import matching_status
from innoprod.text_analysis.matching_status import MatchingStatus

def get_next_unmatched_sentence(recurring_sentences_df):
    code_names = [col for col in recurring_sentences_df.columns if col != 'Cleaned Sentence']
    for _, row in recurring_sentences_df.iterrows():
        if all(row[code_name] for code_name in code_names):
            return row['Cleaned Sentence']


def preview_code_patterns_impact(code_name, code_patterns, recurring_sentences_df):
    matches = recurring_sentences_df['Cleaned Sentence'].apply(lambda x: any(is_pattern_in_sentence(pattern, x) for pattern in code_patterns))

    if code_name in recurring_sentences_df.columns:
        new_statuses = [matching_status.update_status(current_status, new_match) for current_status, new_match in zip(recurring_sentences_df[code_name], matches)]
    else:
        new_statuses = matches.map(matching_status.initial_map)

    preview_df = recurring_sentences_df[new_statuses != matching_status.MatchingStatus.NO_MATCH][['Cleaned Sentence']].copy()
    preview_df[code_name] = new_statuses[new_statuses != matching_status.MatchingStatus.NO_MATCH]
    return preview_df


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
    matches = recurring_sentences_df['Cleaned Sentence'].apply(lambda x: any(is_pattern_in_sentence(pattern, x) for pattern in code_patterns))

    # Insert the matches into the sentences dataframe
    recurring_sentences_df[code_name] = matches.map(matching_status.initial_map)

    return codes_df, recurring_sentences_df


def modify_code(code_name, code_patterns, codes_df, recurring_sentences_df):

    # TODO update the code_df 

    matches = recurring_sentences_df['Cleaned Sentence'].apply(lambda x: any(is_pattern_in_sentence(pattern, x) for pattern in code_patterns))

    new_statuses = [matching_status.update_status(current_status, new_match) for current_status, new_match in zip(recurring_sentences_df[code_name], matches)]

    recurring_sentences_df[code_name] = new_statuses

    return codes_df, recurring_sentences_df


def is_pattern_in_sentence(pattern, sentence):
    m = re.search(pattern, sentence)
    return m is not None
    