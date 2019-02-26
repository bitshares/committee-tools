import click
from grapheneapi.grapheneapi import GrapheneAPI
from bitsharesbase.operations import getOperationNameForId
from bitshares.utils import formatTimeFromNow
import json
from deepdiff import DeepDiff


@click.command()
@click.option("--rpchost", default="localhost")
@click.option("--rpcport", default=8092)
@click.option("--expiration", default=60 * 60 * 24 * 2)
@click.option("--broadcast/--no-broadcast", default=False)
@click.option("--proposer", default="xeroc")
def main(rpchost, rpcport, expiration, broadcast, proposer):
    rpc = GrapheneAPI(rpchost, rpcport)
    obj = rpc.get_object("2.0.0")[0]
    current_fees = obj["parameters"]["current_fees"]["parameters"]
    old_fees = obj["parameters"]["current_fees"]
    scale = obj["parameters"]["current_fees"]["scale"] / 1e4

    # General change of parameter
    changes = {}

    # Copy old fees
    for f in current_fees:
        changes[getOperationNameForId(f[0])] = f[1].copy()

    # New fees
    changes["account_update"]["fee"] = int(0.02527 / scale * 1e5)
    changes["proposal_create"]["fee"] = int(5 / scale * 1e5)

    tx = rpc.propose_fee_change(
        proposer, formatTimeFromNow(expiration), changes, broadcast
    )
    new_fees = tx["operations"][0][1]["proposed_ops"][0]["op"][1]["new_parameters"][
        "current_fees"
    ]

    click.echo(json.dumps(DeepDiff(old_fees, new_fees), indent=4))

    if not broadcast:
        click.echo("Set broadcast to 'True' if the transaction shall be broadcast!")


if __name__ == "__main__":
    main()
