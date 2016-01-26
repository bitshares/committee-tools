""" Connection settings to the wallet
"""
wallet_host           = "localhost"
wallet_port           = 8092

""" Connection settings to a witness node (websocket)
"""
# witness_url           = "wss://bitshares.openledger.info/ws"
witness_url           = "ws://testnet.bitshares.eu/ws"

""" This defines the market to take the price from. The second parameter should
    really be the core asset (BTS, MUSE, TEST, ...)
"""
# watch_markets         = ["USD:BTS"]
watch_markets         = ["PEG.FAKEUSD:TEST"]

""" The proposer pays the fee for proposing the change to the committee
"""
proposer = "xeroc"

""" If this flag is 'False' no proposal will be broadcast (for testing)
"""
broadcast = False

""" The proposal shall expire in x seconds

    60 * 60 * 24 * 14 = 14 days
"""
expires_from_now = 60 * 60 * 24 * 15

""" What tolerance (in percent) is ok when comparing/verifying an active
    proposal?
"""
tolerance_percentage = 5  # %

""" The actual fees denoted in the first asset given in 'watch_markets'.
    E.g. USD
"""
native_fees = {#
               # REGULAR OPERATIONS
               #
               "balance_claim": {},
               "transfer": {
                   "fee": 0.10,
                   "price_per_kbyte": 0.07
               },
               #
               # ORDER OPERATIONS
               #
               "limit_order_cancel": {
                   "fee": 0.001
               },
               "call_order_update": {
                   "fee": 0.001
               },
               "limit_order_create": {
                   "fee": 0.03
               },
               "fill_order": {},
               #
               # ASSET OPERATIONS
               #
               "asset_create": {
                   "long_symbol": 20,
                   "symbol3": 3500,
                   "symbol4": 1000,
                   "price_per_kbyte": 0.007
               },
               "asset_issue": {
                   "fee": 0.10,
                   "price_per_kbyte": 0.007
               },
               "asset_update": {
                   "fee": 1,
                   "price_per_kbyte": 0.007,
               },
               "asset_fund_fee_pool": {
                   "fee": 0.007
               },
               "asset_reserve": {
                   "fee": 0.1
               },
               "asset_settle": {
                   "fee": 5
               },
               "asset_global_settle": {
                   "fee": 5
               },
               "asset_claim_fees": {
                   "fee": 0.072,
               },
               "asset_update_feed_producers": {
                   "fee": 5
               },
               "asset_publish_feed": {
                   "fee": 0.0001
               },
               "asset_update_bitasset": {
                   "fee": 5
               },
               #
               # ACCOUNT OPERATIONS
               #
               "account_upgrade": {
                   "membership_annual_fee": 100 / 12,
                   "membership_lifetime_fee": 100
               },
               "account_whitelist": {
                   "fee": 0.05
               },
               "account_transfer": {
                   "fee": 5
               },
               "account_update": {
                   "fee": 0.001,
                   "price_per_kbyte": 0.007
               },
               "account_create": {
                   "basic_fee": 0.3,
                   "premium_fee": 15,
                   "price_per_kbyte": 0.007
               },
               #
               # VESTING OPERATIONS
               #
               "vesting_balance_create": {
                   "fee": 5
               },
               "vesting_balance_withdraw": {
                   "fee": 0.007
               },
               #
               # WORKER OPERATIONS
               #
               "worker_create": {
                   "fee": 5
               },
               #
               # WITNESS OPERATIONS
               #
               "witness_create": {
                   "fee": 50
               },
               "witness_update": {
                   "fee": 1
               },
               #
               # PROPOSAL OPERATIONS
               #
               "proposal_create": {
                   "fee": 0.15,
                   "price_per_kbyte": 0.07
               },
               "proposal_delete": {
                   "fee": 0.007
               },
               "proposal_update": {
                   "fee": 0.007,
                   "price_per_kbyte": 0.007
               },
               #
               # COMMITTEE OPERATIONS
               #
               "committee_member_create": {
                   "fee": 5
               },
               "committee_member_update_global_parameters": {
                   "fee": 0.50
               },
               "committee_member_update": {
                   "fee": 0.007
               },
               #
               # BLIND/STEALTH OPERATIONS
               #
               "blind_transfer": {
                   "fee": 0.018,
                   "price_per_output": 0.018,
               },
               "transfer_from_blind": {
                   "fee": 3 * 0.07
               },
               "transfer_to_blind": {
                   "fee": 3 * 0.10,
                   "price_per_output": 3 * 0.07
               },
               #
               # WITHDRAW PERMISSION OPERATIONS
               #
               "withdraw_permission_update": {
                   "fee": 0.5
               },
               "withdraw_permission_delete": {
                   "fee": 5
               },
               "withdraw_permission_claim": {
                   "fee": 0.0,
                   "price_per_kbyte": 0.007
               },
               "withdraw_permission_create": {
                   "fee": 0.007
               },
               #
               # CUSTOM/OTHER OPERATIONS
               #
               "custom": {
                   "fee": 0.10,
                   "price_per_kbyte": 0.007
               },
               "assert": {
                   "fee": 0.5
               },
               "override_transfer": {
                   "fee": 5,
                   "price_per_kbyte": 0.007
               },
            }
