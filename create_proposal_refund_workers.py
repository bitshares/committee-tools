from pprint import pprint
from getpass import getpass
from datetime import datetime, timedelta

from bitshares import BitShares
from bitshares.amount import Amount


bitshares = BitShares(nobroadcast=False)
bitshares.wallet.unlock(getpass())

proposal = bitshares.new_proposal(
    proposer="xeroc",
    proposal_expiration=timedelta(days=3).seconds,
    proposal_review=3600,
)

for i in range(1, 4):
    bitshares.create_worker(
        "refund100k-{}".format(i),
        daily_pay=Amount(100000, "BTS"),
        begin=datetime(2019, 2, 1, 0, 0, 0),
        end=datetime(2030, 12, 31, 23, 59, 59),
        payment_type="refund",
        account="committee-account",
        append_to=proposal,
    )


for i in range(1, 4):
    bitshares.create_worker(
        "refund50k-{}".format(i),
        daily_pay=Amount(50000, "BTS"),
        begin=datetime(2019, 2, 1, 0, 0, 0),
        end=datetime(2030, 12, 31, 23, 59, 59),
        payment_type="refund",
        account="committee-account",
        append_to=proposal,
    )

bitshares.create_worker(
    "threshold-bsip",
    daily_pay=Amount(1, "BTS"),
    begin=datetime(2019, 2, 1, 0, 0, 0),
    end=datetime(2030, 12, 31, 23, 59, 59),
    payment_type="refund",
    account="committee-account",
    append_to=proposal,
)

pprint(bitshares.broadcast())
