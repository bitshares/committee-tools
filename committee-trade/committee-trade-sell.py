from grapheneexchange import GrapheneExchange
from pprint import pprint


class Config():
    wallet_host           = "localhost"
    wallet_port           = 8092
    witness_url           = "wss://bitshares.openledger.info/ws"
    watch_markets         = ["USD:BTS",
                             "EUR:BTS",
                             "GOLD:BTS",
                             "SILVER:BTS",
                             "CNY:BTS",
                             "BTC:BTS",
                             ]
    market_separator      = ":"
    account               = "committee-trade"
    proposer              = "xeroc"

    amount_premium = [ [1/3, 1.08],
                       [1/3, 1.10],
                       [1/3, 1.12],
                      ]

if __name__ == '__main__':
    config = Config
    dex   = GrapheneExchange(config,
                             safe_mode=False,
                             propose_only=True)
    r = dex.returnTicker()
    balances = dex.returnBalances()
    for m in config.watch_markets:
        quote, base = m.split(config.market_separator)
        if quote == "BTS" :
            continue

        # p = r[m]["settlement_price"]
        p = r[m]["highestBid"]
        print("Settlement  %s: %12.3f" % (quote, r[m]["settlement_price"]))
        print("Highest Bid %s: %12.3f" % (quote, r[m]["highestBid"]))

        for a in config.amount_premium:
            amount = balances[quote] * a[0]
            sell_price = p * a[1]
            print("Selling %f %s for %f %s/%s" % (amount, quote, sell_price, base, quote))
            dex.sell(m, sell_price, amount)

    dex.propose_all(proposer=config.proposer)
