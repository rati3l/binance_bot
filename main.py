from config import API_KEY, PRIV_KEY, DB_FILE
from binance.client import Client
from db.db import DB

def main():
    database = DB(DB_FILE)
    # database.push_next_operation('DUPA4')
    print(database.get_next_operation())
    print(database.get_score())
    # client = Client(API_KEY, PRIV_KEY)
    # depth = client.get_order_book(symbol='BTCUSDT')
    # prices = client.get_all_tickers()
    # print(prices)


if __name__ == '__main__':
    main()

    