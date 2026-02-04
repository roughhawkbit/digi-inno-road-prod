# Code adapted from https://www.merge.dev/blog/get-folders-google-drive-api

import json
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
SECRETS_DIR = "./secrets/"
TOKEN_PATH = SECRETS_DIR + "token.json"
CREDENTIALS_PATH = SECRETS_DIR + "credentials.json"

def getCredentials():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists(TOKEN_PATH):
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          CREDENTIALS_PATH, SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(TOKEN_PATH, "w") as token:
      token.write(creds.to_json())
  return creds

def getFiles(mimeType: str):
  """
  Returns a list of all file names of the given MIME type.
  
  :param mimeType: The Media Type, as specified in https://developers.google.com/workspace/drive/api/guides/mime-types
  :type mimeType: str
  """
  outputs = []

  try:
    service = build("drive", "v3", credentials=getCredentials())
    page_token = None

    while True:
      # Call the Drive v3 API
      results = (
          service.files()
          .list(q=f"mimeType = '{mimeType}'",
                spaces="drive",
                fields="nextPageToken, files(id, name)",
                pageToken = page_token)
          .execute()
      )
      items = results.get("files", [])
      for item in items:
        outputs.append(item['name'])
      
      if page_token is None:
        break
  except HttpError as error:
    print(f"An error occurred: {error}")
  
  return outputs

def readSpreadsheet(sheet_id: str, range: str):
  try:
    service = build("sheets", "v4", credentials=getCredentials())
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=sheet_id, range=range)
        .execute()
    )
    values = result.get("values", [])
    return values
  except HttpError as err:
    print(err)
  return None


if __name__ == "__main__":
  # print("Folders:\n" + "\n".join(getFiles("application/vnd.google-apps.folder")))
  # print("Spreadsheets:\n" + "\n".join(getFiles("application/vnd.google-apps.spreadsheet")))
  with open('./secrets/sheet.json', 'r') as f:
    sheet_metadata = json.load(f)
  for name, range in sheet_metadata['ranges'].items():
    print(readSpreadsheet(sheet_metadata['sheet_id'], range))
