from Constants import *
import webbrowser
from Constants import kite

def getLoginUrl():
    return kite.login_url()

def startConnection():
    webbrowser.open(getLoginUrl())

def generateNewAccessToken(requestToken):
    data = kite.generate_session(requestToken, api_secret=API_SECRET)
    return data["access_token"]

def setKiteAccessToken(accessToken):
    kite.set_access_token(accessToken)