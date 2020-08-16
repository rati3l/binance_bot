from config import API_KEY, PRIV_KEY, DB_FILE
from binance.client import Client
from db.db import DB
from time import sleep
from binance.enums import *
import math 
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def test_order(client, order_type, price):
    order_params = client.create_test_order(
                                symbol='BTCUSDT',
                                side=order_type,
                                type=ORDER_TYPE_LIMIT,
                                timeInForce=TIME_IN_FORCE_GTC,
                                quantity=0.01,
                                price=price)
def main():
    database = DB(DB_FILE)
    client = Client(API_KEY, PRIV_KEY)
    database.push_next_operation('BUY')

    last_price = 0
    while True:
        operation = database.get_next_operation()
        current_price = float(client.get_avg_price(symbol='BTCUSDT')['price'])

        if operation == 'BUY':
            if current_price > last_price:
                test_order(client, SIDE_BUY, math.floor(current_price * 100)/100)
                database.push_next_operation('SELL')
                logging.info(f'bought for {current_price}')
                buy_price = current_price

        elif operation == 'SELL':
            if current_price - buy_price > 1:
                test_order(client, SIDE_SELL,  math.floor(current_price * 100)/100)
                score = current_price - buy_price
                logging.info(f"selling for {score * 0.01} profit")
                database.push_score(score * 0.01)
                database.push_next_operation('BUY')
        
        last_price = current_price
        sleep(1)


if __name__ == '__main__':
    main()

    