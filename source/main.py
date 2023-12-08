# from server import RequestTokenRetrievalServer
from connect import getLoginUrl, generateNewAccessToken, setKiteAccessToken
from KiteOps import sharedKiteOps, sharedKiteTicker
from ManageAccessToken import getSavedAccessToken, saveNewAccessToken


def setup():
    savedAccessToken = getSavedAccessToken()
    if savedAccessToken is None:
        print('Login url is: ', getLoginUrl())
        requestToken = input('Please enter request token after login: \n')
        accessToken = generateNewAccessToken(requestToken)
        saveNewAccessToken(accessToken)
        setKiteAccessToken(accessToken)
    else:
        setKiteAccessToken(savedAccessToken)

setup()
# sharedKiteOps.getHoldings()
sharedKiteTicker.startTicker()