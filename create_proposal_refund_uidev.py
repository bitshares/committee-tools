from pprint import pprint
from getpass import getpass
from datetime import datetime, timedelta

from bitshares import BitShares
from bitshares.amount import Amount
from bitshares.asset import Asset


bitshares = BitShares(nobroadcast=False)
bitshares.wallet.unlock(getpass())

proposal = bitshares.new_proposal(
    proposer="xeroc",
    proposal_expiration=timedelta(days=3).seconds,
    proposal_review=3600,
)

bitshares.transfer(
    "gibbs-from-ncis",
    4631.34999,
    "BTS",
    account="onboarding.bitshares.foundation",
    append_to=proposal,
)

test = Asset("TEST")
test.change_issuer("committee-issuer", append_to=proposal)

pprint(bitshares.broadcast())
