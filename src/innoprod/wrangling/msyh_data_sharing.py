import pandas as pd

from .wrangling_tools import replace_values

def wrangle_roadmaps(roadmaps_df):
    # Integer values
    int_cols = [
        'Number of GAFs', 
        'Number of FTE Employees (calc)',
        'Number of FT employees',
        'Number of PT employees',
        'Current Digital Readiness Score (refer to PAS:1040)',
        'Anticipated resulting Digital Readiness Score (refer to PAS:1040)',
        'Employee Increase (FTE calc)',
        'Employees at Project Completion (FTE)'
    ]
    for col in int_cols:
        roadmaps_df = replace_values(roadmaps_df, col, '', None)
        roadmaps_df[col] = roadmaps_df[col].astype("Int64")

    # Monetary values
    monetary_cols = [
        'Turnover',
        'Increased Turnover £',
        'Increased Pre-Tax Profits',
        'Increased TO/Employee', 
        'Increased GVA'
    ]
    for col in monetary_cols:
        roadmaps_df[col] = roadmaps_df[col].str.replace(pat={'£':'', ',':''})
        roadmaps_df = replace_values(roadmaps_df, col, '-', None)
        roadmaps_df = replace_values(roadmaps_df, col, '', None)
        roadmaps_df['Turnover'] = pd.to_numeric(roadmaps_df['Turnover'])

    # Date values
    date_cols = [
        'Enquiry Date',
        'Registration Form Complete',
        'Edge Digital Diagnostic Complete',
        'GROWTHmapper Diagnostic Date',
        'Roadmap Complete',
        'SDR Complete Date'
    ]
    for col in date_cols:
        roadmaps_df[col] = pd.to_datetime(roadmaps_df[col], format="%m/%d/%Y")
    
    # Boolean values (with missing)
    bool_cols = [
        'Do you have a Digital Champion in place?',
        'Has resource consumption (electricity, gas, waste, and water) or Greenhouse Gas emissions reduced since you started working with the Programme?'
    ]


    # Categorical values
    categorical_cols = [
        'Referral Source',
        'LEP',
        'Local Authority',
        '.... MANY MORE'
    ]

    return roadmaps_df


from ..sheet_tools import get_sheet_dfs

if __name__ == "__main__":
    data = get_sheet_dfs()
    roadmaps_df = data['Roadmaps']
    roadmaps_df = wrangle_roadmaps(roadmaps_df)