
from binance.client import Client
from binance.websockets import BinanceSocketManager
import pymongo



client = Client("a","b")

bm = BinanceSocketManager(client)


myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = myclient ["basic_MDA"]

mycol = mydb ["data"]     # collection is mongo is same as a Table 


def process_message(a):

    mydict = [a]
    mycol.insert_many(mydict)
    print(a['k']['c'])
# 
    
#    if c >= 1:
#        print ('BUY')
#    else:
#        print( "dont BUYY")
conn_key = bm.start_kline_socket('MDABTC', process_message, interval='15m')
bm.start()



