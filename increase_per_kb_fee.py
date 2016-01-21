from grapheneapi.grapheneclient import GrapheneClient
from graphenebase.transactions import getOperationNameForId
import json
from deepdiff import DeepDiff

proposer   = "xeroc"
expiration = "2016-01-21T22:59:59"
price_per_kbyte = 40  # in BTS
broadcast = False


class Wallet():
    wallet_host           = "localhost"
    wallet_port           = 8092

if __name__ == '__main__':
    graphene = GrapheneClient(Wallet)
    obj = graphene.getObject("2.0.0")
    current_fees = obj["parameters"]["current_fees"]["parameters"]
    old_fees = obj["parameters"]["current_fees"]
    scale = obj["parameters"]["current_fees"]["scale"] / 1e4

    # General change of parameter
    changes = {}
    for f in current_fees :
        if ("price_per_kbyte" in f[1]) and (f[1]["price_per_kbyte"] is 20):
            print("Changing operation %s[%d]" % (getOperationNameForId(f[0]), f[0]))
            changes[getOperationNameForId(f[0])] = f[1].copy()
            changes[getOperationNameForId(f[0])]["price_per_kbyte"] = int(price_per_kbyte / scale * 1e5)

    # overwrite / set specific fees
    # changes["transfer"]["price_per_kbyte"]       = int(  20 / scale * 1e5)
    # changes["account_update"]["price_per_kbyte"] = int(   5 / scale * 1e5)

    print("=" * 80)
    tx = graphene.rpc.propose_fee_change(proposer, expiration, changes, broadcast)
    new_fees = tx["operations"][0][1]["proposed_ops"][0]["op"][1]["new_parameters"]["current_fees"]

    print(json.dumps(DeepDiff(old_fees, new_fees), indent=4))

    if not broadcast:
        print("=" * 80)
        print("Set broadcast to 'True' if the transaction shall be broadcast!")
