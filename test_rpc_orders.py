import sys
import hashlib
import json
import random
import time

import setting
from test_rpc_init import transaction

if __name__ == '__main__':
    accounts = setting.accounts

    print('=== Create SELL limit orders ===')
    while True:
        price = random.randint(300, 800)
        amount = 1 * 10**18
        quote = price * 10**6
        call = f'{{"p": "zen", "f": "trade_limit_order", "a": ["BTC", -{amount}, "USDC", {quote}]}}'
        print(f'Sell Limit: price={price}, amount={amount // 10**18}')
        tx_hash = transaction(call)
        print(f'  tx: {tx_hash}')

        quote = price * amount * (10**6) // (10**18)
        call = f'{{"p": "zen", "f": "trade_limit_order", "a": ["BTC", {amount}, "USDC", -{quote}]}}'
        print(f'Buy Limit: price={price}, amount={amount // 10**18}')
        tx_hash = transaction(call)
        print(f'  tx: {tx_hash}')

        time.sleep(5)

    # print('=== Market SELL ===')
    # amount = int(0.1 * 10**18)
    # call = f'{{"p": "zen", "f": "trade_market_order", "a": ["BTC", -{amount}, "USDC", null]}}'
    # print(f'Market SELL: amount={amount // 10**18}')
    # tx_hash = transaction(call)
    # print(f'  tx: {tx_hash}')

    # print('=== Market BUY ===')
    # amount = 100 * 10**6
    # call = f'{{"p": "zen", "f": "trade_market_order", "a": ["BTC", null, "USDC", -{amount}]}}'
    # print(f'Market BUY: amount={amount // 10**18}')
    # tx_hash = transaction(call)
    # print(f'  tx: {tx_hash}')


    # print('\n=== Done ===')