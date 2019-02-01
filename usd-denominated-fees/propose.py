import time
import click
import config
from grapheneapi.grapheneapi import GrapheneAPI
from bitshares.market import Market
from pprint import pprint
from datetime import datetime
from deepdiff import DeepDiff


@click.command()
@click.option("--rpchost", default="localhost")
@click.option("--rpcport", default=8092)
@click.option("--expiration", default=60 * 60 * 24 * 14)
@click.option("--broadcast/--no-broadcast", default=False)
@click.option("--proposer", default="xeroc")
def main(rpchost, rpcport, expiration, broadcast, proposer):
    rpc = GrapheneAPI(rpchost, rpcport)
    expiration = datetime.utcfromtimestamp(time.time() + int(expiration)).strftime(
        "%Y-%m-%dT%H:%M:%S"
    )

    # Get current fees
    obj = rpc.get_object("2.0.0")[0]
    old_fees = obj["parameters"]["current_fees"]
    scale = int(obj["parameters"]["current_fees"]["scale"]) / 1e4
    core_asset = rpc.get_asset("1.3.0")

    # Get ticker/current price
    market = Market(config.market)
    ticker = market.ticker()
    # core_exchange_rate = float(ticker["core_exchange_rate"])
    settlement_price = float(ticker["quoteSettlement_price"])

    # Translate native fee in core_asset fee
    new_fees = config.native_fees.copy()
    for opName in new_fees:
        for f in new_fees[opName]:
            if config.force_integer_core_fee:
                new_fees[opName][f] = int(
                    int(config.native_fees[opName][f] / scale * settlement_price)
                    * 10 ** core_asset["precision"]
                )
            else:
                new_fees[opName][f] = int(
                    config.native_fees[opName][f]
                    * 10 ** core_asset["precision"]
                    / scale
                    * settlement_price
                )

    tx = rpc.propose_fee_change(proposer, expiration, new_fees, broadcast)
    new_fees = tx["operations"][0][1]["proposed_ops"][0]["op"][1]["new_parameters"][
        "current_fees"
    ]

    # Show differences from previous to new fees
    pprint(DeepDiff(old_fees, new_fees))

    if not broadcast:
        print("=" * 80)
        print("Set --broadcast if the transaction shall be broadcast!")


if __name__ == "__main__":
    main()
