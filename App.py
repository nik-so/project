import gspread
 
Sheet_credential = gspread.service_account("credential.json")
# Open Spreadsheet by key
spreadsheet = Sheet_credential.open_by_key('1FLriyowMmKSBaIZVpI0akL3uCin7Eulryld3ZsGQUj8')
print(spreadsheet.title)