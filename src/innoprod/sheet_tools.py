import json
import pandas as pd
import os.path

from .gdrive_auth import read_spreadsheet
from .path_tools import secrets_path

def get_sheet_details():
    sheet_secrets = os.path.join(secrets_path(), 'sheet.json')
    with open(sheet_secrets, 'r') as f:
        sheet_details = json.load(f)
    return sheet_details

def get_sheet_dfs():
    sheet_details = get_sheet_details()
    data = {}
    for name, rng in sheet_details['ranges'].items():
        lol = read_spreadsheet(sheet_details['sheet_id'], rng)
        df = pd.DataFrame(lol[1:], columns=lol[0])
        data[name] = df
    return data

if __name__ == "__main__":
    data = get_sheet_dfs()
    print(f'Read in {len(data)} sheets')