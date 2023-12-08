from Constants import kite, API_KEY
import csv
import json
from kiteconnect import KiteTicker
from ManageAccessToken import getSavedAccessToken

class KiteOps():

    def getHoldings(self):
        instruments: [] = kite.ltp(["NSE:NIFTY BANK"])
        fields = ['instrument_token', 'exchange_token', 'tradingsymbol', 'name', 'instrument_type', 'exchange', 'segment', 'last_price', 'tick_size', 'lot_size', 'expiry', 'strike']
        # for instrument in instruments:
        #     print(instrument)

        with open('ltp.json', 'w') as openfile:
            # for instrument in instruments:
            json_object = json.dumps(instruments, indent=4, default=str)
            openfile.write(json_object)
            # writer = csv.DictWriter(openfile, fieldnames = fields)
            # writer.writeheader()
            # writer.writerows(instruments)

        

class Ticker():
    accesstoken = getSavedAccessToken()
    print("API_KEY ---> ", API_KEY)
    print("access_token ---> ", accesstoken)
    kws = KiteTicker(API_KEY, accesstoken)

    def on_ticks(ws, ticks):
    # Callback to receive ticks.
    # logging.debug("Ticks: {}".format(ticks))
        print(ticks)

    def on_connect(ws, response):
        # Callback on successful connect.
        # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
        ws.subscribe([256265, 260105])

        # Set RELIANCE to tick in `full` mode.
        # ws.set_mode(ws.MODE_FULL, [738561])

    def on_close(ws, code, reason):
        # On connection close stop the event loop.
        # Reconnection will not happen after executing `ws.stop()`
        ws.stop()

    # Assign the callbacks.
    kws.on_ticks = on_ticks
    kws.on_connect = on_connect
    kws.on_close = on_close
    
    def startTicker(self):
        self.kws.connect()


sharedKiteOps = KiteOps()
sharedKiteTicker = Ticker()