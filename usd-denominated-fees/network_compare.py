from grapheneapi.grapheneapi import GrapheneAPI
from bitsharesbase.operations import getOperationNameForId
from bitshares.market import Market
import math
import config


if __name__ == '__main__':
    graphene = GrapheneAPI(config.wallet_host, config.wallet_port)

    # Get current fees
    obj = graphene.get_object("2.0.0")[0]
    fees = obj["parameters"]["current_fees"]["parameters"]
    scale = int(obj["parameters"]["current_fees"]["scale"]) / 1e4
    core_asset = graphene.get_asset("1.3.0")

    # Get ticker/current price
    market = Market(config.watch_markets[0])
    ticker = market.ticker()
    core_exchange_rate = float(ticker["core_exchange_rate"])
    settlement_price = float(ticker["quoteSettlement_price"])

    fee_named = {}
    for f in fees:
        opName = getOperationNameForId(f[0])
        fee_named[opName] = {}
        # derive in USD
        for o in f[1]:
            if opName in config.native_fees :
                if config.force_integer_core_fee :
                    fee_named[opName][o] = int(int(f[1][o]) / 10 ** core_asset["precision"]) * scale / core_exchange_rate
                else:
                    fee_named[opName][o] = int(f[1][o]) / 10 ** core_asset["precision"] * scale / core_exchange_rate
                scalingfactor = (config.native_fees[opName][o] / fee_named[opName][o]) if fee_named[opName][o] else 999
                # if math.fabs(scalingfactor) > config.tolerance_percentage / 100:
                #     print("=" * 30 + "Warning:" + "=" *30)
                print("%23s price for %41s differs by %8.3fx (network: %9.4f USD / proposal: %9.4f USD)" %
                      (o, opName, scalingfactor, fee_named[opName][o], config.native_fees[opName][o]))
            else :
                print("[Warning] The operation %s is not defined in your set of native fees!" % opName)
