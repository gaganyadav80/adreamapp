import requests
# import xlrd
# import panda
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import fertilizer

#count = 1

while True:
    fertilizer.fertilizer_time()

    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('a-team.json', scope)
    gs = gspread.authorize(credentials)

    gsheet = gs.open("test_case_1").sheet1
    # wsheet = gsheet.worksheet("data")
    # all_cells = wsheet.range('A1:D3')
    # print(gsheet.get_all_records())
    name = [None] * 6
    phone = [None] * 6
    i=0
    count = 0
    for i in range(6):
        name[i] = gsheet.cell(i+2, 2).value
        phone[i] = gsheet.cell(i+2, 3).value
        i = i + 1

    '''
    for i in range(6):
        print(name[i])

    print("\n\n")
    for i in range(6):
        print(phone[i])

    i=0
    while(i<6):
        querystring = {'message': f"Hello {name[i]}, Your phone number is {phone[i]}"}
        print(querystring['message'])
        i = i+1


    '''
    url = "https://www.fast2sms.com/dev/bulk"


    text1=open("output_file.txt","r")
    text2 = open("output_file_1.txt","r")
    if text1.mode=="r":
        contents=text1.read()
        if text2.mode == "r":
            contents2=text2.read()



    i=0
    fertilizer.count += 1
    while(i<6):
        querystring = {
            "authorization":"wKaVxc2CQbpXDYrtJ4eROyvm7ALsuMWko0h9SE5ziFNnZgj1fUXPmGSOZv9gNpAHY8fwiBIos4JF3tj7",
            "sender_id":"FSTSMS",
            "message": f"Hello {name[i]}, {contents}\n\n{contents2}",
            "language":"english",
            "route":"p",
            "numbers": f"{phone[i]}",
            }

        headers = {'cache-control': "no-cache"}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(f"Sending SMS to {name[i]} with status: ")
        print(response.text)
        print("\n\n")
        i = i+1
    time.sleep(86400)
