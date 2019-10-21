# -*- coding: utf-8 -*-
import click
from uptick.main import main
from uptick.decorators import online, unlock
from pprint import pprint
from bitshares.asset import Asset
from bitshares.account import Account
from bitsharesbase.operations import Asset_update, Asset_update_bitasset


@main.command()
@click.argument("symbols", nargs=-1)
@click.option("--proposer", default="xeroc")
@click.option("--expiration", default=60 * 60 * 24 * 7)
@click.option("--review", default=3600)
@click.option("--broadcast/--no-broadcast", default=False)
@online
@unlock
@click.pass_context
def propose(ctx, symbols, proposer, expiration, review, broadcast):
    proposal = ctx.blockchain.new_proposal(
        proposer=proposer, proposal_expiration=expiration, proposal_review=review
    )

    for symbol in symbols:
        asset = Asset(symbol, full=True, blockchain_instance=ctx.blockchain)
        assert asset.is_bitasset

        bitasset_options = asset["bitasset_data"]["options"].copy()
        options = asset["options"].copy()

        """ Changes to options and bitasset options
        """
        bitasset_options.update(
            dict(force_settlement_offset_percent=0, minimum_feeds=7)
        )

        """ END OF CHANGES
        """
        op = Asset_update(
            **{
                "fee": {"amount": 0, "asset_id": "1.3.0"},
                "issuer": asset["issuer"],
                "asset_to_update": asset["id"],
                "new_options": options,
                "extensions": [],
            }
        )
        ctx.blockchain.finalizeOp(op, proposer, "active", append_to=proposal)

        op = Asset_update_bitasset(
            **{
                "fee": {"amount": 0, "asset_id": "1.3.0"},
                "issuer": asset["issuer"],
                "asset_to_update": asset["id"],
                "new_options": bitasset_options,
                "extensions": [],
            }
        )

        ctx.blockchain.finalizeOp(op, proposer, "active", append_to=proposal)

    pprint(proposal.json())
    if broadcast or click.confirm("Broadcast?"):
        pprint(proposal.broadcast())


if __name__ == "__main__":
    main()
