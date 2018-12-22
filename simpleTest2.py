
from binance.client import Client
from binance.websockets import BinanceSocketManager
import pymongo



client = Client("a","b")

bm = BinanceSocketManager(client)


myclient = pymongo.MongoClient("mongodb://poya:Muhammad00.@ds135592.mlab.com:35592/data_db")

mydb = myclient ["data_db"]

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



