import pandas as pd

from .wrangling_tools import replace_values, remove_newlines_from_str_series

def wrangle_roadmaps(roadmaps_df):
    # Convert Likert scales to integers
    likert_cols = [
        'How did you find the process of accessing the programme?',
        'How valuable did you find the involvement of your contact within the programme during the course of the support?',
        'How valuable did you find the GROWTHmapper and its report in identifying the key areas of supporting your business?',
        'How valuable did you find the support you received from the Expert Coach during the course of the programme?',
        'To what extent were you satisfied with the Programme overall?',
    ]
    for col in likert_cols:
        mask = roadmaps_df[col].notna()
        roadmaps_df.loc[mask, col] = roadmaps_df[mask][col].str[0]

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
    for col in int_cols + likert_cols:
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
    
    # Boolean values (nullable)
    bool_cols = [
        'Do you have a Digital Champion in place?',
        'Has resource consumption (electricity, gas, waste, and water) or Greenhouse Gas emissions reduced since you started working with the Programme?'
    ]
    for col in bool_cols:
        roadmaps_df[col] = roadmaps_df[col].map({'Yes': True, 'No': False})

    # Categorical values
    categorical_cols = {
        'Referral Source': None,
        'LEP': None,
        'Local Authority': None,
        'Org Size by Number of FTE (calc)': ['Micro - 1-9', 'Small - 10-49', 'Medium - 50-249'],
        'Main historical barrier': None,
        'Application area of technology in the Action Plan': None,
        'Sub-application area of technology in the Action Plan': None,
        'Anticipated Made Smarter Support Package(s) to be accessed': None, # TODO handle as a list of categoricals?
        # 'Other business support referrals', TODO values would need some cleaming up first
        'Would you recommend the Programme to others?': ['No', 'Maybe', 'Yes']
    }
    for col, ordering in categorical_cols.items():
        roadmaps_df[col] = roadmaps_df[col].astype("category")
        if ordering is not None:
            roadmaps_df[col] = roadmaps_df[col].cat.set_categories(ordering, ordered=True)

    # Text columns
    text_cols = [
        'Summary review of Edge Digital diagnostic report & current state and key improvement areas',
        'What are the internal barriers to growth? How do you intend to finance future growth? Are there sufficient leadership and management skills in the business to achieve your growth? What opportunities do you have to expand into new markets?',
        'Level of current Strategic Digital Skills/knowledge in the business',
        'Level of current Technical Digital Skills/knowledge in the business',
        'Whether the business is already investing/adopting/utilising Industry 4.0 Technologies, with examples',
        'Summary of the identified problems, including Gap Analysis',
        'Key potential industry 4.0 solutions to address the identified problems/gaps',
        'Recommended Action Plan to utilise Industry 4.0 Technology',
        'Overview of qualitative benefits of recommended Action Plan (positive/negative)',
        'Skills and other requirements that will be needed to successfully implement the recommended Action Plan',
        'What has been your overall opinion of the support you have received in this programme? (Add comments)',
        
    ]
    for col in text_cols:
        roadmaps_df[col] = remove_newlines_from_str_series(roadmaps_df[col])

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
    for col in categorical_cols:
        grants_df[col] = grants_df[col].astype("category")

    return grants_df


from ..sheet_tools import get_sheet_dfs

if __name__ == "__main__":
    data = get_sheet_dfs()
    roadmaps_df = data['Roadmaps']
    roadmaps_df = wrangle_roadmaps(roadmaps_df)