from grapheneexchange import GrapheneExchange
from graphenebase.transactions import getOperationNameForId
import math
import config


if __name__ == '__main__':
    dex   = GrapheneExchange(config, safe_mode=False)
    graphene = dex.rpc

    # Get current fees
    obj = graphene.get_object("2.0.0")[0]
    fees = obj["parameters"]["current_fees"]["parameters"]
    scale = int(obj["parameters"]["current_fees"]["scale"]) / 1e4
    core_asset = graphene.get_asset("1.3.0")

    # Get ticker/current price
    ticker = dex.returnTicker()[config.watch_markets[0]]
    core_exchange_rate = ticker["core_exchange_rate"]

    fee_named = {}
    for f in fees:
        opName = getOperationNameForId(f[0])
        fee_named[opName] = {}
        # derive in USD
        for o in f[1]:
            if opName in config.native_fees :
                fee_named[opName][o] = int(f[1][o]) / 10 ** core_asset["precision"] * scale / core_exchange_rate
                scalingfactor = (config.native_fees[opName][o] / fee_named[opName][o]) if fee_named[opName][o] else 999
                if math.fabs(scalingfactor) > config.tolerance_percentage / 100:
                    print("%23s price for %41s differs by %8.3fx (network: %9.4f USD / proposal: %9.4f USD)" %
                          (o, opName, scalingfactor, fee_named[opName][o], config.native_fees[opName][o]))
            else :
                print("[Warning] The operation %s is not defined in your set of native fees!" % opName)
