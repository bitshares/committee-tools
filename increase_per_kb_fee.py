from grapheneapi.grapheneclient import GrapheneClient
from graphenebase.transactions import getOperationNameForId, operations
import json

proposer   = "xeroc"
expiration = "2016-01-21T23:59:59"
price_per_kbyte = 40  # in BTS
broadcast = False


class Wallet():
    wallet_host           = "localhost"
    wallet_port           = 8092

if __name__ == '__main__':
    graphene = GrapheneClient(Wallet)
    obj = graphene.getObject("2.0.0")
    current_fees = obj["parameters"]["current_fees"]["parameters"]
    scale = obj["parameters"]["current_fees"]["scale"] / 1e4

    # General change of parameter
    changes = {}
    for f in current_fees :
        if ("price_per_kbyte" in f[1]):
            # Set the current fees
            changes[getOperationNameForId(f[0])] = f[1]
            # update the price_per_kbyte
            changes[getOperationNameForId(f[0])]["price_per_kbyte"] = int(price_per_kbyte / scale * 1e5)

    # overwrite / set specific fees
    changes["transfer"]["price_per_kbyte"]       = int(  20 / scale * 1e5)
    changes["account_update"]["price_per_kbyte"] = int(   5 / scale * 1e5)

    print("=" * 80)
    print(json.dumps(changes, indent=4))
    print("=" * 80)
    tx = graphene.rpc.propose_fee_change(proposer, expiration, changes, broadcast)
    print(json.dumps(tx["operations"][0][1]["proposed_ops"][0]["op"][1]["new_parameters"], indent=4))

    if not broadcast:
        print("=" * 80)
        print("Set broadcast to 'True' if the transaction shall be broadcast!")
