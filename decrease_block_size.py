from grapheneapi.grapheneapi import GrapheneAPI
from bitshares.utils import formatTimeFromNow
import json
from deepdiff import DeepDiff

proposer   = "xeroc"
expiration = formatTimeFromNow(10 * 60)
broadcast  = True


if __name__ == '__main__':
    graphene = GrapheneAPI("localhost", 8092)
    obj = graphene.get_object("2.0.0")

    # General change of parameter
    changes = {"maximum_block_size": 2000000}

    print("=" * 80)
    tx = graphene.propose_parameter_change(proposer, expiration, changes, broadcast)
    print(json.dumps(tx, indent=4))
