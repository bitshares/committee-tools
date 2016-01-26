from grapheneexchange import GrapheneExchange
from graphenebase.transactions import getOperationNameForId
import math
import config

if __name__ == '__main__':
    dex   = GrapheneExchange(config, safe_mode=False)
    graphene = dex.rpc

    # Get current fees
    core_asset = graphene.get_asset("1.3.0")
    committee_account = dex.rpc.get_account("committee-account")
    proposals = dex.ws.get_proposed_transactions(committee_account["id"])

    for proposal in proposals:
        print("Proposal: %s" % proposal["id"])

        prop_op = proposal["proposed_transaction"]["operations"]

        if len(prop_op) > 1 :
            print(" - [Warning] This proposal has more than 1 operation")

        for op in prop_op :

            if op[0] == 31:

                fees = op[1]["new_parameters"]["current_fees"]["parameters"]
                scale = int(op[1]["new_parameters"]["current_fees"]["scale"]) / 1e4

                # Get ticker/current price
                ticker = dex.returnTicker()[config.watch_markets[0]]
                core_exchange_rate = ticker["core_exchange_rate"]
                settlement_price = ticker["settlement_price"]

                fee_named = {}
                for f in fees:
                    opName = getOperationNameForId(f[0])
                    fee_named[opName] = f[1].copy()
                    for o in f[1]:
                        if opName in config.native_fees :
                            fee_named[opName][o] = int(f[1][o]) / 10 ** core_asset["precision"] * scale / core_exchange_rate
                            if config.native_fees[opName][o] != 0.0:
                                offset = 1 - (fee_named[opName][o] / config.native_fees[opName][o])
                                if math.fabs(offset) > config.tolerance_percentage / 100:
                                    print(" - [Warning] %30s price for %30s differs by %+9.3f%% (%9.3f instead of %9.3f)" %
                                          (o, opName, offset * 100, fee_named[opName][o], config.native_fees[opName][o]))
                        else :
                            print(" - [Warning] The parameter %s in operation %s is not defined in your set of native fees!" % (o, opName))
            else :
                print(" - [Warning] Another operation is part of this proposal: %s" % getOperationNameForId(op[0]))
