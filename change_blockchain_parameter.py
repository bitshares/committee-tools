import json
import click
from grapheneapi.grapheneapi import GrapheneAPI
from bitshares.utils import formatTimeFromNow


@click.command()
@click.option("--rpchost", default="localhost")
@click.option("--rpcport", default=8092)
@click.option("--expiration", default=60 * 60 * 24 * 2)
@click.option("--broadcast/--no-broadcast", default=False)
@click.option("--proposer", default="xeroc")
def main(rpchost, rpcport, expiration, broadcast, proposer):
    rpc = GrapheneAPI(rpchost, rpcport)

    """ Update parameters here
    """
    updated_parameters = dict(maximum_transaction_size=1048576}

    tx = rpc.propose_parameter_change(
        proposer, formatTimeFromNow(expiration), updated_parameters, broadcast
    )

    click.echo(json.dumps(tx, indent=4))

    if not broadcast:
        click.echo("Set broadcast to 'True' if the transaction shall be broadcast!")


if __name__ == "__main__":
    main()
