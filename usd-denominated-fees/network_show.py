from grapheneapi.grapheneapi import GrapheneAPI
from bitsharesbase.operations import getOperationNameForId
from bitshares.market import Market
import json
import config


if __name__ == "__main__":
    graphene = GrapheneAPI(config.wallet_host, config.wallet_port)

    # Get current fees
    obj = graphene.get_object("2.0.0")[0]
    fees = obj["parameters"]["current_fees"]["parameters"]
    scale = int(obj["parameters"]["current_fees"]["scale"]) / 1e4
    core_asset = graphene.get_asset("1.3.0")

    # Get ticker/current price
    market = Market(config.market)
    ticker = market.ticker()
    core_exchange_rate = float(ticker["core_exchange_rate"])
    settlement_price = float(ticker["quoteSettlement_price"])

    fee_named = {}
    for f in fees:
        opName = getOperationNameForId(f[0])
        fee_named[opName] = {}
        # derive in USD
        for o in f[1]:
            fee_named[opName][o] = (
                int(f[1][o]) / 10 ** core_asset["precision"] * scale / settlement_price
            )

    print(json.dumps(fee_named, indent=4))
