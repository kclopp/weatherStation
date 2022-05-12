import requests
import json
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials as accCreds
from os.path import exists
from pathlib import Path
from pprint import pprint

# URL for ambientweather.net API
url = "https://rt.ambientweather.net/v1/devices/";

# Retreives locally stored API Key and formates it for use
with open("apiKey", "r") as file:
    apiVar = file.read().replace('\n', '')


# Retreives locally stored Application Key and formates it for use
with open("applicationKey", "r") as file:
    appVar = file.read().replace('\n', '')

# Creates varable for use in in requests call
par = {'apiKey' : apiVar, 'applicationKey' : appVar}

# Creates opbect from API call
r = requests.get(url, params=par)

# recursivly formats object into dict of usefull information
ld = r.content
ld = json.loads(ld)
ld = ld[0]['lastData']

fieldName = []
for key, value in ld.items():
    fieldName.append(key)

# Adds two custome field names for off line measurements 
fieldName.append("soildMoisture")
fieldName.append("SoidTemp")

fieldValue = []
for key, value in ld.items():
    fieldValue.append(value)

'''
path = Path('test.csv')

if (True == path.is_file()):
    with open('test.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldName)
        #writer.writeheader()
        writer.writerow(ld)
else:
    with open('test.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldName)
        writer.writeheader()
        writer.writerow(ld)

'''

##pprint(fieldName)
pprint(r)
#pprint(ld)

#This ends the portion scraping data from my PWS and creating a spreadsheed

#This begins comunicating with Google sheets

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = accCreds.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("ambWeather").sheet1

data = sheet.cell(1,1)

a = str(data)

if a == "<Cell R1C1 None>":
    # Inserts File Headers
    sheet.insert_row(fieldName, 1)
    sheet.insert_row(fieldValue, 2)
else:
    #Inserts fresh data at row two pushing old data down
    sheet.insert_row(fieldValue, 2)

#print(a)
#print(type(a))
#print(data)




