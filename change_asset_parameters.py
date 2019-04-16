import json
import click

from uptick.decorators import unlock, online
from uptick.main import main

from pprint import pprint

from bitshares.utils import formatTimeFromNow
from bitshares.asset import Asset
from bitshares.account import Account
from bitsharesbase.operations import Asset_update, Asset_update_bitasset


@main.command()
@click.option("--expiration", default=60 * 60 * 24 * 2)
@click.option("--account", default="xeroc")
@click.option("--review_period", default=3600)
@click.pass_context
@online
@unlock
def update(ctx, expiration, account, review_period):
    """ Update parameters here
    """

    asset = Asset("RUB", full=True)
    bitasset = asset["bitasset_data"]
    similar_to_asset = Asset("RUBLE", full=True)
    similar_to_bitasset = similar_to_asset["bitasset_data"]

    ops = list()
    # ops.append(
    #    Asset_update(
    #        **{
    #            "fee": {"amount": 0, "asset_id": "1.3.0"},
    #            "issuer": asset["issuer"],
    #            "asset_to_update": asset["id"],
    #            "new_options": similar_to_asset["options"],
    #            "extensions": [],
    #        }
    #    )
    # )

    ops.append(
        Asset_update_bitasset(
            **{
                "fee": {"amount": 0, "asset_id": "1.3.0"},
                "issuer": asset["issuer"],
                "asset_to_update": asset["id"],
                "new_options": similar_to_bitasset["options"],
                "extensions": [],
            }
        )
    )

    account = Account(account)
    proposal = ctx.blockchain.new_proposal(
        proposer=account, proposal_review=review_period, proposal_expiration=expiration
    )
    ctx.blockchain.finalizeOp(ops, account, "active", append_to=proposal)

    tx = proposal.broadcast()

    click.echo(json.dumps(tx, indent=4))


if __name__ == "__main__":
    main()
