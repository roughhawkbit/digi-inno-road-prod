# Authentication Setup

This package uses the `python-o365` package to connect to SharePoint, where the input data is stored and results will be written out to. Data should only ever be written to storage on machines that belong to the University.

## Google Drive setup

Follow the instructions [here](https://www.merge.dev/blog/get-folders-google-drive-api) for the sections **Prerequisites and project setup** and for **Configure your app to access the Google Drive API**, but with the following exceptions and additional guidance:
* On the **OAuth consent screen** set the **User Type** to **Internal** instead of External. This can make things a little more fiddly later on, but provides greater security.
* When downloading the JSON file with credentials, rename that file `credentials.json` and store it in the `secrets` subdirectory. All `.json` files in that subdirectory are ignored by git and so will not be pushed to GitHub.


## Accessing the Google drive
When first trying to access the data on Google Drive, a browser window should open requesting that you log in. If using a machine where the primary Google account registered is _not_ your university account, then the browser window that opens will attempt to log you in using the wrong account and this will not be permitted.

Within the terminal window running `gdrive_auth.py`, there should be a console output like:
```
Please visit this URL to authorise this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=...
```
Copy this URL to a browser window where you _are_ logged in using your university Google account and the correct Google account should be choosable.

TODO: replace this workaround with a better solution.
