import gdax
import time



class myWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"    
        self.products = ["ETH-USD"]
        self.tracker = ["ETH-USD"]
        self.message_count = 0
    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'side' in msg and 'sequence' in msg and 'size' in msg and 'time' in msg:
            print msg["sequence"], msg["price"], msg["size"], (float(msg["price"])*float(msg["size"])),  msg["side"]
            fhTH = open('tradeHistory.txt','a')
            fhTH.write((str((msg["sequence"])) + " "+ str(msg["price"]) + " " + str(msg["size"]) + " " + str((float(msg["price"])*float(msg["size"]))) + " " +  str(msg["side"]))+ " " + str(msg["time"]))
            fhTH.write("\n")             
    def on_close(self):
        print "closed"
       
wsClient = myWebsocketClient()
wsClient.start()
