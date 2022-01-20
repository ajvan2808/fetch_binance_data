import sqlite3
import requests
import logging_handler

logger = logging_handler.setup_logging()


# TODO: Get P2P Binance price, write and output loggers
def fetch_data(url='https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search') -> list:
    payload = dict(page=1, rows=10, payTypes=[], asset="USDT", tradeType="BUY", fiat="VND", publisherType="merchant")

    headers = {'Content-Type': "application/json"}

    res = requests.post(url, json=payload, headers=headers)
    if res:
        responses = res.json()
        price_list = [float(adv['adv']['price']) for adv in responses['data']]
        logger.info('Get price list.')
    else:
        logger.info('No response.')

    return price_list


# TODO: Calculate avg_price function
def calculate_price(num):
    avg_num = sum(num) / len(num)
    total_num = sum(num)
    return avg_num, total_num


# TODO: Connect and write to db
def add_to_db(price_data):
    try:
        conn = sqlite3.connect('BinanceP2P.db')
        cur = conn.cursor()
        table_sql = ''' 
                    CREATE TABLE IF NOT EXISTS p2pprice 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                    total_price FLOAT,
                    average_price FLOAT,
                    created_on DEFAULT CURRENT_TIMESTAMP)
                    '''

        cur.execute(table_sql)
        logger.info('Table created.')

        avg_price = calculate_price(price_data)[0]
        total_price = calculate_price(price_data)[1]
        cur.execute('''INSERT INTO p2pprice (average_price, total_price) VALUES(?, ?)''', (avg_price, total_price))
        logger.info('Insert average price, total price into database.')

        conn.commit()
        conn.close()

    except Exception as err:
        print(err)


if __name__ == '__main__':
    logger.info('------ Start ------')
    data = fetch_data()
    add_to_db(data)
    logger.info('------ End ------')

# for adv in responses['data']:
#     price_lst.append(adv['adv']['price'])
