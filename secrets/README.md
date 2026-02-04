# Secrets

## Credentials
See docs / auth_setup.md for how `credentials.json` is created.

## Token
`token.json` is created automatically and should not need manual editing. This file can be safely deleted, however, for example if changing the access scope during development.

## Sheet
A manually created/edited document that specifies the sheet access data. Of the format:
``` json
{
    "sheet_id": "...",
    "ranges":{
        "Roadmaps": "Roadmaps&SDRs!A2:BI222",
        "Grants": "Grants!A1:U314"
    }
}
```

The `sheet_id` is _not_ the filename as shown on the browser portal. Instead, attempt to **Share** the sheet via the browser portal, copying the hyperlink, and then extract the long string of characters from that hyperlink. For example, if this is the sharing hyperlink:
```
https://docs.google.com/spreadsheets/d/abcdefghijklmnopqrstuvwxyz/edit?usp=sharing
```
then the `sheet_id` is `abcdefghijklmnopqrstuvwxyz`.