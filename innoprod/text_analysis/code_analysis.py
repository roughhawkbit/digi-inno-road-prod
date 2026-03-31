from ipywidgets import HTML
import re

HTML_TOOLTIP_PREAMBLE = r"<style>.tooltip {position:relative;display:inline-block;cursor:pointer;} .tooltiptext{visibility:hidden;width: 130px;background-color:black;color:#fff;text-align:center;border-radius:6px;padding:5px 0;position:absolute;z-index:1;} .tooltip:hover .tooltiptext{visibility:visible;}</style>"

def decorate_matches(highlighted_sentence, pattern, title, highlight_color):
    # TODO include keyword title as a hover tooltip
    matches = re.findall(pattern, highlighted_sentence, flags=re.IGNORECASE)
    for match in matches:
        highlighted_sentence = re.sub(
            re.escape(match), 
            f'<span class="tooltip"; style="background-color: {highlight_color};">{match}<span class="tooltiptext">{title}</span></span>', 
            highlighted_sentence,
            flags=re.IGNORECASE
        )
    return highlighted_sentence


class CodeAnalysis:
    def __init__(self, recurring_sentences_df):
        self.recurring_sentences_df = recurring_sentences_df
        self.recurring_sentences_df['Analysed'] = False
        self.keywords = {}
        self.quantifiers = {}

    def get_next_sentence(self):
        remaining_mask = self.recurring_sentences_df['Analysed'] == False
        if not remaining_mask.any():
            return None
        return self.recurring_sentences_df[remaining_mask]['Cleaned Sentence'].iloc[0]

    def display_next_sentence(self):
        sentence = self.get_next_sentence()
        if sentence is None:
            print("All sentences have been analysed.")
        else:
            print(sentence)

    def display_sentence_with_highlights(self, sentence):
        highlighted_sentence = HTML_TOOLTIP_PREAMBLE + sentence
        for keyword_pattern, keyword_title in self.keywords.items():
            for quantifier_pattern, quantifier_title in self.quantifiers.items():
                pattern = quantifier_pattern.replace('KEYWORD', keyword_pattern)
                highlighted_sentence = decorate_matches(highlighted_sentence, pattern, quantifier_title, 'lightblue')
            highlighted_sentence = decorate_matches(highlighted_sentence, keyword_pattern, keyword_title, 'yellow')
        return HTML(highlighted_sentence)

    def mark_sentence_analysed(self, sentence):
        self.recurring_sentences_df.loc[self.recurring_sentences_df['Cleaned Sentence'] == sentence, 'Analysed'] = True

    def add_keyword(self, keyword_pattern, keyword_title):
        self.keywords[keyword_pattern] = keyword_title

    def add_quantifier(self, quantifier_pattern, quantifier_title):
        self.quantifiers[quantifier_pattern] = quantifier_title


