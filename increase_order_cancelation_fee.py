from grapheneapi.grapheneclient import GrapheneClient
import json
from deepdiff import DeepDiff

proposer   = "xeroc"
expiration = "2016-01-28T05:59:59"
broadcast  = False


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
    changes = {"limit_order_cancel": {
               "fee" : int(0.01 / scale * 1e5)
               }}

    print("=" * 80)
    tx = graphene.rpc.propose_fee_change(proposer, expiration, changes, broadcast)
    new_fees = tx["operations"][0][1]["proposed_ops"][0]["op"][1]["new_parameters"]["current_fees"]

    print(json.dumps(DeepDiff(old_fees, new_fees), indent=4))

    if not broadcast:
        print("=" * 80)
        print("Set broadcast to 'True' if the transaction shall be broadcast!")
