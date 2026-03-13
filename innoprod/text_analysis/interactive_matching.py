import ipywidgets

from innoprod.text_analysis.matching_status import MatchingStatus, update_status

def verification_widget(recurring_sentences_df, code_name):
    # TODO handle cases where sentences were previously verified or marked incorrect/broken - maybe show them in the widget with different styling?
    w = ipywidgets.SelectMultiple(
        options=recurring_sentences_df[recurring_sentences_df[code_name] == MatchingStatus.UNVERIFIED]['Cleaned Sentence'],
        value=[],
        disabled=False,
        layout={'width': 'max-content'},
    )
    return w

def _apply_verification_to_row(row, code_name, interact_values):
    current_status = row[code_name]
    new_match = row['Cleaned Sentence'] in interact_values
    if current_status == MatchingStatus.UNVERIFIED:
        return MatchingStatus.VERIFIED if new_match else current_status
    return current_status


def apply_verification(recurring_sentences_df, code_name, w):
    interact_values = w.get_interact_value()
    recurring_sentences_df[code_name] = recurring_sentences_df.apply(
        lambda row: _apply_verification_to_row(row, code_name, interact_values),
        axis=1
    )
    return recurring_sentences_df