from grapheneexchange import GrapheneExchange
from pprint import pprint
import config

if __name__ == '__main__':
    dex   = GrapheneExchange(config,
                             safe_mode=False,
                             propose_only=True)
    r = dex.returnTicker()
    balances = dex.returnBalances()
    for m in config.watch_markets:
        quote, base = m.split(config.market_separator)
        if quote == "BTS" :
            continue

        settlement_price = r[m]["settlement_price"]
        highestBid = r[m]["highestBid"]
        print("Settlement  %7s: %12.3f" % (quote, r[m]["settlement_price"]))
        print("Highest Bid %7s: %12.3f" % (quote, r[m]["highestBid"]))

        if quote in config.amount_premium:
            for a in config.amount_premium[quote]:
                sell_price = settlement_price * (1 + a["premium"] / 100)
                amount = balances[quote] * a["volume_percentage"] / 100

                # do not sell below the highest bid!
                if sell_price < highestBid :
                    print("Highest bid is higher than sell price! Changing sell price")
                    sell_price = highestBid

                premium = (sell_price / settlement_price - 1) * 100

                if premium > 15:
                    print("Premium is %f%% and thus higher than 15%%.  Selling at 15%%!" % premium)
                    sell_price = settlement_price * 1.15
                    premium = (sell_price / settlement_price - 1) * 100

                print("Selling %f %s for %f %s/%s (premium: %2.2f%%)" % (amount, quote, sell_price, base, quote, premium))
                dex.sell(m, sell_price, amount, expiration=24 * 60 * 60)

            dex.propose_all(proposer=config.proposer)
            dex.proposals_clear()
