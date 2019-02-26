import json
from grapheneapi import GrapheneAPI
import config

if __name__ == "__main__":

    client = GrapheneAPI(
        config.wallet_host,
        config.wallet_port,
        config.wallet_user,
        config.wallet_password,
    )
    proposer = client.get_account(config.proposer_account)
    from_account = client.get_account(config.transfer_from)
    to_account = client.get_account(config.transfer_to)

    ops = []
    assetsavailable = client.list_account_balances("committee-account")
    for balance in assetsavailable:
        asset = client.get_asset(balance["asset_id"])
        if asset["id"] == "1.3.0":
            continue
        transfer_amount = int(balance["amount"] * config.transfer_percentage / 100.0)
        op = client.get_prototype_operation("transfer_operation")
        op[1]["amount"]["amount"] = transfer_amount
        op[1]["amount"]["asset_id"] = asset["id"]
        op[1]["from"] = from_account["id"]
        op[1]["to"] = to_account["id"]
        ops.append(op)

    buildHandle = client.begin_builder_transaction()
    for op in ops:
        client.add_operation_to_builder_transaction(buildHandle, op)
    client.set_fees_on_builder_transaction(buildHandle, "1.3.0")

    params = client.get_object("2.0.0")[0]
    preview = params["parameters"]["committee_proposal_review_period"]

    client.propose_builder_transaction2(
        buildHandle, proposer["name"], config.expiration, preview, False
    )
    client.set_fees_on_builder_transaction(buildHandle, "1.3.0")

    # Sign and broadcast
    tx = client.sign_builder_transaction(buildHandle, config.broadcast)

    print(json.dumps(tx, indent=4))
