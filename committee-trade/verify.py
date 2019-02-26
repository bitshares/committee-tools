from grapheneexchange import GrapheneExchange
from pprint import pprint


class Config:
    wallet_host = "localhost"
    wallet_port = 8092
    witness_url = "wss://bitshares.openledger.info/ws"
    watch_markets = [
        "USD:BTS",
        "EUR:BTS",
        "GOLD:BTS",
        "SILVER:BTS",
        "CNY:BTS",
        "BTC:BTS",
    ]
    market_separator = ":"
    account = "committee-trade"
    proposer = "xeroc"


if __name__ == "__main__":
    config = Config
    dex = GrapheneExchange(config, safe_mode=False)
    graphene = dex.rpc

    # Get current fees
    core_asset = graphene.get_asset("1.3.0")
    committee_account = dex.rpc.get_account("committee-trade")
    proposals = dex.ws.get_proposed_transactions(committee_account["id"])

    r = dex.returnTicker()

    for proposal in proposals:
        print("Proposal: %s" % proposal["id"])

        prop_op = proposal["proposed_transaction"]["operations"]

        for op in prop_op:

            if op[0] == 1:

                order = op[1]

                if order["min_to_receive"]["asset_id"] != "1.3.0":
                    print("[Warning] not selling asset for BTS!")

                base = dex.rpc.get_asset(order["amount_to_sell"]["asset_id"])
                quote = dex.rpc.get_asset(order["min_to_receive"]["asset_id"])

                amount_base = (
                    int(order["amount_to_sell"]["amount"]) / 10 ** base["precision"]
                )
                amount_quote = (
                    int(order["min_to_receive"]["amount"]) / 10 ** quote["precision"]
                )

                m = base["symbol"] + config.market_separator + quote["symbol"]
                settlement_price = r[m]["settlement_price"]

                price = amount_quote / amount_base
                premium = (price / settlement_price - 1) * 100
                print(
                    "Selling %f %s for %f %s/%s (premium %5.2f%%)"
                    % (
                        amount_base,
                        base["symbol"],
                        price,
                        quote["symbol"],
                        base["symbol"],
                        premium,
                    )
                )

            else:
                print(
                    " - [Warning] Another operation is part of this proposal: %s"
                    % (op[0])
                )
