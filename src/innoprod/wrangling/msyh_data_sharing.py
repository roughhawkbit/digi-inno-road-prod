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
        roadmaps_df[col] = pd.to_numeric(roadmaps_df[col])

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


def wrangle_grants(grants_df):
     # Integer values
    int_cols = [
        'Project Number'
    ]
    for col in int_cols:
        grants_df = replace_values(grants_df, col, '', None)
        grants_df[col] = grants_df[col].astype("Int64")

    # Monetary values
    monetary_cols = [
        'Anticipated Total Cost',
        'Grant Value for this Application',
        'Approved Total Project Cost',
        'Grant Amount Offered',
        'Actual Project Spend',
        'Actual amount claimed',
        'Claimed Variance to Offer'
    ]
    for col in monetary_cols:
        grants_df[col] = grants_df[col].str.replace(pat={'£':'', ',':''})
        grants_df = replace_values(grants_df, col, '-', None)
        grants_df = replace_values(grants_df, col, '', None)
        grants_df[col] = pd.to_numeric(grants_df[col])

    # Date values
    date_cols = [
        'Application Date',
        'Date Grant Offered',
        'Grant Expiry Date',
        'Date Claimed',
        'Date Offer Withdrawn',
        'Client invoice date',
        'Date Grant Paid'
    ]
    for col in date_cols:
        grants_df[col] = pd.to_datetime(grants_df[col], format="%m/%d/%Y")

    # Categorical values
    categorical_cols = [
        'GAF Type Intensity',
        'Application Status',
        'Claim Status'
    ]

    return grants_df


from ..sheet_tools import get_sheet_dfs

if __name__ == "__main__":
    data = get_sheet_dfs()
    roadmaps_df = data['Roadmaps']
    roadmaps_df = wrangle_roadmaps(roadmaps_df)