from pprint import pprint
from grapheneapi.grapheneapi import GrapheneAPI
from bitshares.utils import formatTimeFromNow
import json

proposer   = "xeroc"
expiration = formatTimeFromNow(60 * 60 * 1.5)
broadcast  = True


if __name__ == '__main__':
    graphene = GrapheneAPI("localhost", 8092)
    obj = graphene.get_object("2.0.0")[0]
    current_fees = obj["parameters"]["current_fees"]["parameters"]
    old_fees = obj["parameters"]["current_fees"]
    scale = obj["parameters"]["current_fees"]["scale"] / 1e4

    pprint(old_fees)

    # General change of parameter
    """
    {'long_symbol': 60698376,
     'price_per_kbyte': 12139,
     'symbol3': '9711740216',
     'symbol4': 2427935054}
    """
    changes = {"asset_create": {
        'symbol3': str(9 * 10 ** 9 * 10 **5),
        'symbol4': str(9 * 10 ** 9 * 10 **5),
        'long_symbol': str(9 * 10 ** 9 * 10 **5),
        'price_per_kbyte': str(12139),
        }
    }

    print("=" * 80)
    tx = graphene.propose_fee_change(proposer, expiration, changes, broadcast)
    new_fees = tx["operations"][0][1]["proposed_ops"][0]["op"][1]["new_parameters"]["current_fees"]


    pprint(tx)

    if not broadcast:
        print("=" * 80)
        print("Set broadcast to 'True' if the transaction shall be broadcast!")
