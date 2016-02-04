from grapheneexchange import GrapheneExchange
import json
from datetime import datetime
import time
from deepdiff import DeepDiff
import config


if __name__ == '__main__':
    dex   = GrapheneExchange(config, safe_mode=False)
    graphene = dex.rpc
    expiration = datetime.utcfromtimestamp(time.time() + int(config.expires_from_now)).strftime('%Y-%m-%dT%H:%M:%S')

    # Get current fees
    obj = graphene.get_object("2.0.0")[0]
    old_fees = obj["parameters"]["current_fees"]
    scale = int(obj["parameters"]["current_fees"]["scale"]) / 1e4
    core_asset = graphene.get_asset("1.3.0")

    # Get ticker/current price
    ticker = dex.returnTicker()[config.watch_markets[0]]
    core_exchange_rate = ticker["core_exchange_rate"]
    settlement_price = ticker["settlement_price"]

    # Translate native fee in core_asset fee
    new_fees = config.native_fees.copy()
    for opName in new_fees:
        for f in new_fees[opName]:
            if config.force_integer_core_fee :
                new_fees[opName][f] = int(int(config.native_fees[opName][f] / scale * core_exchange_rate) * 10 ** core_asset["precision"])
            else:
                new_fees[opName][f] = int(config.native_fees[opName][f] * 10 ** core_asset["precision"] / scale * core_exchange_rate)

    tx = graphene.propose_fee_change(config.proposer, expiration, new_fees, config.broadcast)
    new_fees = tx["operations"][0][1]["proposed_ops"][0]["op"][1]["new_parameters"]["current_fees"]

    # Show differences from previous to new fees
    print(json.dumps(DeepDiff(old_fees, new_fees), indent=4))

    if not config.broadcast:
        print("=" * 80)
        print("Set broadcast to 'True' if the transaction shall be broadcast!")
