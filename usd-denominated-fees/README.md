# Compare with Network

Compare the network fees (denoted in USD) with your local settings from `config.py`.

    $ python3 network_compare.py
    [Warning] premium_fee price for account_create differs by -2.810229% (7.286893 instead of 15)
    [Warning] membership_lifetime_fee price for account_upgrade differs by -23.159763% (36.434467 instead of 100)
    [Warning] fee price for account_transfer differs by -1.157988% (1.821723 instead of 5)
    [Warning] long_symbol price for asset_create differs by -0.649541% (18.217234 instead of 20)
    [Warning] symbol3 price for asset_create differs by -611.471152% (1821.723350 instead of 3500)
    [Warning] symbol4 price for asset_create differs by 33.896446% (1093.034010 instead of 1000)
    [Warning] fee price for asset_update_bitasset differs by -1.157988% (1.821723 instead of 5)
    [Warning] fee price for asset_update_feed_producers differs by -1.157988% (1.821723 instead of 5)
    [Warning] fee price for asset_settle differs by -1.688976% (0.364345 instead of 5)
    [Warning] fee price for asset_global_settle differs by -1.157988% (1.821723 instead of 5)
    [Warning] fee price for witness_create differs by -11.579882% (18.217234 instead of 50)
    [Warning] fee price for withdraw_permission_delete differs by -1.821723% (0.000000 instead of 5)
    [Warning] fee price for committee_member_create differs by 4.815629% (18.217234 instead of 5)
    [Warning] fee price for vesting_balance_create differs by -1.820396% (0.003643 instead of 5)
    [Warning] fee price for worker_create differs by 4.815629% (18.217234 instead of 5)
    [Warning] fee price for override_transfer differs by -1.795174% (0.072869 instead of 5)
    [Warning] The operation blind_transfer is not defined in your set of native fees!
    [Warning] The operation blind_transfer is not defined in your set of native fees!
    [Warning] The operation asset_claim_fees is not defined in your set of native fees!

# Show from Network

Show the network fees denoted in USD.

    $ python3 network_show.py
    {
        "limit_order_create": {
            "fee": 0.018217233502893736
        },
        "asset_create": {
            "long_symbol": 18.217233502893738,
            "symbol3": 1821.723350289374,
            "price_per_kbyte": 3.643446700578748e-07,
            "symbol4": 1093.0340101736242
        },
        "blind_transfer": {
            "fee": 0.018217233502893736,
            "price_per_output": 0.018217233502893736
        },
        "account_create": {
            "premium_fee": 7.286893401157495,
            "basic_fee": 0.018217233502893736,
            "price_per_kbyte": 0.0036434467005787476
        },
        "asset_settle": {
            "fee": 0.36434467005787474
        },
        "transfer": {
            "fee": 0.07286893401157495,
            "price_per_kbyte": 0.03643446700578747
        },
        "asset_fund_fee_pool": {
            "fee": 0.0036434467005787476
        },
        "transfer_from_blind": {
            "fee": 0.018217233502893736
        },
        "override_transfer": {
            "fee": 0.07286893401157495,
            "price_per_kbyte": 3.643446700578748e-07
        },
        "proposal_update": {
            "fee": 0.07286893401157495,
            "price_per_kbyte": 3.643446700578748e-07
        },
        "asset_update_feed_producers": {
            "fee": 1.8217233502893737
        },
        "withdraw_permission_create": {
            "fee": 0.0036434467005787476
        },
        "proposal_delete": {
            "fee": 0.0036434467005787476
        },
        "vesting_balance_withdraw": {
            "fee": 0.07286893401157495
        },
        "asset_issue": {
            "fee": 0.07286893401157495,
            "price_per_kbyte": 0.0036434467005787476
        },
        "custom": {
            "fee": 0.0036434467005787476,
            "price_per_kbyte": 3.643446700578748e-07
        },
        "account_upgrade": {
            "membership_annual_fee": 7.286893401157495,
            "membership_lifetime_fee": 36.434467005787475
        },
        "asset_reserve": {
            "fee": 0.07286893401157495
        },
        "withdraw_permission_update": {
            "fee": 0.0036434467005787476
        },
        "asset_claim_fees": {
            "fee": 0.07286893401157495
        },
        "account_transfer": {
            "fee": 1.8217233502893737
        },
        "fill_order": {},
        "committee_member_create": {
            "fee": 18.217233502893738
        },
        "asset_publish_feed": {
            "fee": 0.0036434467005787476
        },
        "vesting_balance_create": {
            "fee": 0.0036434467005787476
        },
        "limit_order_cancel": {
            "fee": 0.0
        },
        "committee_member_update": {
            "fee": 0.07286893401157495
        },
        "call_order_update": {
            "fee": 0.07286893401157495
        },
        "withdraw_permission_claim": {
            "fee": 0.07286893401157495,
            "price_per_kbyte": 3.643446700578748e-07
        },
        "asset_update": {
            "fee": 1.8217233502893737,
            "price_per_kbyte": 3.643446700578748e-07
        },
        "transfer_to_blind": {
            "fee": 0.018217233502893736,
            "price_per_output": 0.018217233502893736
        },
        "worker_create": {
            "fee": 18.217233502893738
        },
        "account_update": {
            "fee": 0.07286893401157495,
            "price_per_kbyte": 0.0036434467005787476
        },
        "witness_create": {
            "fee": 18.217233502893738
        },
        "account_whitelist": {
            "fee": 0.010930340101736243
        },
        "withdraw_permission_delete": {
            "fee": 0.0
        },
        "asset_update_bitasset": {
            "fee": 1.8217233502893737
        },
        "witness_update": {
            "fee": 0.07286893401157495
        },
        "proposal_create": {
            "fee": 0.07286893401157495,
            "price_per_kbyte": 3.643446700578748e-07
        },
        "balance_claim": {},
        "assert": {
            "fee": 0.0036434467005787476
        },
        "committee_member_update_global_parameters": {
            "fee": 0.0036434467005787476
        },
        "asset_global_settle": {
            "fee": 1.8217233502893737
        },
        "asset_settle_cancel": {}
    }

# Propose

Propose your local settings as new fees.

    $ python3 propose.py
    {
        "values_changed": [
            "root['parameters'][0][1]['fee']: 2000000 ===> 2744653",
            "root['parameters'][0][1]['price_per_kbyte']: 1000000 ===> 1921257",
            "root['parameters'][1][1]['fee']: 500000 ===> 823396",
            "root['parameters'][2][1]['fee']: 0 ===> 27446",
            "root['parameters'][3][1]['fee']: 2000000 ===> 27446",
            "root['parameters'][5][1]['premium_fee']: 200000000 ===> 411698076",
            "root['parameters'][5][1]['basic_fee']: 500000 ===> 8233961",
            "root['parameters'][5][1]['price_per_kbyte']: 100000 ===> 192125",
            "root['parameters'][6][1]['fee']: 2000000 ===> 27446",
            "root['parameters'][6][1]['price_per_kbyte']: 100000 ===> 192125",
            "root['parameters'][7][1]['fee']: 300000 ===> 1372326",
            "root['parameters'][8][1]['membership_annual_fee']: 200000000 ===> 228721153",
            "root['parameters'][8][1]['membership_lifetime_fee']: 1000000000 ===> 2744653846",
            "root['parameters'][9][1]['fee']: 50000000 ===> 137232692",
            "root['parameters'][10][1]['price_per_kbyte']: 10 ===> 192125",
            "root['parameters'][10][1]['long_symbol']: 500000000 ===> 548930769",
            "root['parameters'][10][1]['symbol3']: '50000000000' ===> '96062884615'",
            "root['parameters'][10][1]['symbol4']: '30000000000' ===> '27446538461'",
            "root['parameters'][11][1]['fee']: 50000000 ===> 27446538",
            "root['parameters'][11][1]['price_per_kbyte']: 10 ===> 192125",
            "root['parameters'][12][1]['fee']: 50000000 ===> 137232692",
            "root['parameters'][13][1]['fee']: 50000000 ===> 137232692",
            "root['parameters'][14][1]['fee']: 2000000 ===> 2744653",
            "root['parameters'][14][1]['price_per_kbyte']: 100000 ===> 192125",
            "root['parameters'][15][1]['fee']: 2000000 ===> 2744653",
            "root['parameters'][16][1]['fee']: 100000 ===> 192125",
            "root['parameters'][17][1]['fee']: 10000000 ===> 137232692",
            "root['parameters'][18][1]['fee']: 50000000 ===> 137232692",
            "root['parameters'][19][1]['fee']: 100000 ===> 2744",
            "root['parameters'][20][1]['fee']: 500000000 ===> 1372326923",
            "root['parameters'][21][1]['fee']: 2000000 ===> 27446538",
            "root['parameters'][22][1]['fee']: 2000000 ===> 4116980",
            "root['parameters'][22][1]['price_per_kbyte']: 10 ===> 1921257",
            "root['parameters'][23][1]['fee']: 2000000 ===> 192125",
            "root['parameters'][23][1]['price_per_kbyte']: 10 ===> 192125",
            "root['parameters'][24][1]['fee']: 100000 ===> 192125",
            "root['parameters'][25][1]['fee']: 100000 ===> 192125",
            "root['parameters'][26][1]['fee']: 100000 ===> 13723269",
            "root['parameters'][27][1]['fee']: 2000000 ===> 0",
            "root['parameters'][27][1]['price_per_kbyte']: 10 ===> 192125",
            "root['parameters'][28][1]['fee']: 0 ===> 137232692",
            "root['parameters'][29][1]['fee']: 500000000 ===> 137232692",
            "root['parameters'][30][1]['fee']: 2000000 ===> 192125",
            "root['parameters'][31][1]['fee']: 100000 ===> 13723269",
            "root['parameters'][32][1]['fee']: 100000 ===> 137232692",
            "root['parameters'][33][1]['fee']: 2000000 ===> 192125",
            "root['parameters'][34][1]['fee']: 500000000 ===> 137232692",
            "root['parameters'][35][1]['fee']: 100000 ===> 2744653",
            "root['parameters'][35][1]['price_per_kbyte']: 10 ===> 192125",
            "root['parameters'][36][1]['fee']: 100000 ===> 13723269",
            "root['parameters'][38][1]['fee']: 2000000 ===> 137232692",
            "root['parameters'][38][1]['price_per_kbyte']: 10 ===> 192125",
            "root['parameters'][39][1]['fee']: 500000 ===> 8233961",
            "root['parameters'][39][1]['price_per_output']: 500000 ===> 5763773",
            "root['parameters'][41][1]['fee']: 500000 ===> 5763773"
        ]
    }
    ================================================================================
    Set broadcast to 'True' if the transaction shall be broadcast!

# Verify proposal

Verify the proposal with your local (or the proposer's) settings.

    $ python3 verify.py
    Proposal: 1.10.0
     - [Warning] membership_lifetime_fee price for account_upgrade differs by -0.886327% (97.567339 instead of 100)
     - [Warning] symbol4 price for asset_create differs by -8.863272% (975.673387 instead of 1000)
     - [Warning] symbol3 price for asset_create differs by -31.021451% (3414.856855 instead of 3500)
     - [Warning] The operation blind_transfer is not defined in your set of native fees!
     - [Warning] The operation asset_claim_fees is not defined in your set of native fees!

