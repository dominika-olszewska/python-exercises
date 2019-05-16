import requests
# TASKS (11p)

# 1 Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)


def getBitbayApi():
    response = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
    data = response.json()
    best_bid_BB = data['bid']
    best_ask_BB = data['ask']

    return best_bid_BB, best_ask_BB


def getBitMarketApi():
    response = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json")
    data = response.json()
    best_bid_BM = data['bid']
    best_ask_BM = data['ask']

    return best_bid_BM, best_ask_BM

BitBayPrices = getBitbayApi()
BitMarketPrices = getBitMarketApi()

def comparePrices():
    if BitBayPrices[0] > BitMarketPrices[0] and BitBayPrices[1] > BitMarketPrices[1]:
        print("Currently the BitMarket exchange market is better for buying whilst BitBay is better for selling")
    elif BitBayPrices[0] < BitMarketPrices[0] and BitBayPrices[1] > BitMarketPrices[1]:
        print("Currently the BitBay exchange market is better for both buying and selling")
    elif BitBayPrices[0] > BitMarketPrices[0] and BitBayPrices[1] < BitMarketPrices[1]:
        print("Currently the BitMarket exchange market is better for both buying and selling")
    elif BitBayPrices[0] < BitMarketPrices[0] and BitBayPrices[1] < BitMarketPrices[1]:
        print("Currently the BitBay exchange market is better for buying whilst BitMarket is better for selling")


comparePrices()