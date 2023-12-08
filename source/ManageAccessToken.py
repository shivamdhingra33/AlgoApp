import json
import datetime
import pytz
from Constants import ACCESS_TOKEN_FILE

currentDate = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).date())

def saveNewAccessToken(accessToken):
    dictionary = {
        "currentDate": currentDate,
        "accessToken": accessToken
    }
    json_object = json.dumps(dictionary, indent=4)
    with open(ACCESS_TOKEN_FILE, "w") as outfile:
        outfile.write(json_object)
    
def getSavedAccessToken():
    try:
        with open(ACCESS_TOKEN_FILE, 'r') as openfile:
            json_object = json.load(openfile)
        if currentDate == json_object["currentDate"]:
            accessToken = json_object["accessToken"]
            return accessToken
        else:
            return None
    except OSError as e:
        print(e.errno)
        return None

# saveNewAccessToken("shovsohvs")
# print(getSavedAccessToken())