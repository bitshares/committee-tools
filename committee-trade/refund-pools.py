from grapheneapi.grapheneclient import GrapheneClient
from pprint import pprint
import config
from datetime import datetime
import time


def formatTimeFromNow(secs=0):
    return datetime.utcfromtimestamp(time.time() + int(secs)).strftime('%Y-%m-%dT%H:%M:%S')


if __name__ == '__main__':
    client   = GrapheneClient(config)
    core_asset = client.getObject("1.3.0")
    account  = client.rpc.get_account(config.account)
    proposer = client.rpc.get_account(config.proposer)

    ops = []

    for assetname in config.refund_asset_pools:
        asset = client.rpc.get_asset(assetname)
        dynamic = client.getObject(asset["dynamic_asset_data_id"])
        fee_pool = dynamic["fee_pool"]

        difference = config.refund_target_amount * 10 ** core_asset["precision"] - int(fee_pool)

        if difference > 0 :
            print("Asset %s has only %f %s in Fee Pool. Filling in %f %s" %
                    (assetname,
                     fee_pool / 10 ** core_asset["precision"],
                     core_asset["symbol"],
                     difference / 10 ** core_asset["precision"],
                     core_asset["symbol"]))
            op = client.rpc.get_prototype_operation("asset_fund_fee_pool_operation")
            op[1]["from_account"] = account["id"]
            op[1]["asset_id"] = core_asset["id"]
            op[1]["amount"] = int(difference)
            ops.append(op)

    buildHandle = client.rpc.begin_builder_transaction()
    for op in ops:
        client.rpc.add_operation_to_builder_transaction(buildHandle, op)
    client.rpc.set_fees_on_builder_transaction(buildHandle, "1.3.0")
    client.rpc.propose_builder_transaction2(buildHandle, 
                                            proposer["name"],
                                            formatTimeFromNow(60 * 60 * 24),
                                            0,
                                            False)
    client.rpc.set_fees_on_builder_transaction(buildHandle, "1.3.0")
    tx = client.rpc.sign_builder_transaction(buildHandle, False)
    pprint(tx)
