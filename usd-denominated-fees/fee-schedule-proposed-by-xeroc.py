####################################################################
# Overview
####################################################################
#
# Rational:
#
# 1.) The transfer of value (any token) is a core functionality of many crypto
#     currencies and business like dwolla and paypal. In order to be competitive,
#     we need a lower over all cost associated with that operation/transaction.
#     Furthermore, the costs associated with that operation are rather low because
#     only account ids, asset ids and an amount are involved. Optional memos can be
#     set a higher fee. The transfer operation is considered a *core* functionality
#     of BitShares and its used should be incentivized. This way, we can
#     even attract more businesses that are looking for micropayment
#     solutions.
#
# 2.) Another *core* functionality and major *value proposition* is the
#     decentralized exchange (DEX) which is associated with a different set of feed.
#     Currently, the fees are flat fees for order creation, cancellation and update,
#     and are independent of the amount actually traded. Hence, small volume orders
#     pay the same fee as large volume orders. Taking a closer look at any
#     competitor reveals that this should certainly chance. Instead of asking for a
#     rather high flat fee to compensate the costs of the DEX (storing and matching
#     orders), I here propose to reduce the flat fee drastically to an amount that
#     mostly to prevents spam and instead set a percentage trading fee for every
#     committee-owned asset. The advantages are that the committee (read: DAC) could
#     earn more fees from matching orders. Since cancellation of orders results in a
#     refund of the creation fee, this should also encourage traders to bring
#     liquidity. A disadvantage is that the DAC earns less from trading of assets
#     that are not owned by the committee, such as OPEN.BTC, TRADE.MUSE etc. because
#     the flat fees are reduced and the percentage market fees go to the
#     corresponding issuer. Anyway, this approach should result in more traders
#     using the DEX and an increase of liquidity.
#
#     What percentage should be used? Since we are using a fixed percentage
#     independent of an individuals volume, we should choose a percentage that is
#     lower than the highest fee asked for by big exchanges such as Kraken,
#     Coinbase, etc. Furthermore, regional difference should be taken into account
#     eventually. For now I propose a fee of
#
#                             0.15%
#
#     of the matched volume which is less than most centralized competitors even
#     though we offer an increased security over them. This fee may be considered as
#     a welcome package and may probably be increased to something close to 0.05% to
#     reflect the decentralized and trust-free nature of the DEX.
#
# 3.) Now that we have reduced the fees for our two core functionalities, how can we
#     rescue the referral program that pays the registrar/affiliate a fraction of
#     the payed fee from referrers? The transfer and trading fees certainly don't
#     motive business to bring in more users if they don't get paid!
#
#     The solution is rather simple: The above mentioned transfer and trade
#     operations are only two out of many operations that can be used by customers
#     to make full use of BitShares. There is also the creation of assets,
#     withdrawal permissions as well as worker, committee member creation and
#     proposals. These fees can be used to let the referral program benefit from
#     customers.
#
#     So, we distinguish power users from regular users. Power users should be
#     encouraged to upgrade their account to a life-time membership (or annual
#     membership) to reduce their fees by 80% (receive cashback). The regular users
#     rarely creates new assets and uses it frequently, as well as use more advanced
#     features of the network, but if he does, we can ask for a comparably high fee
#     since there are only few competitors with these functionalities, if at all.
#     A power users that wants to see constantly reduced fees and benefit from
#     cheaper advanced features should be asked to pay a higher fee to upgrade his
#     account.
#
# In short: The referral program should only receive minor benefit from the core
# value proposition (transfers and trades) of the DEX but instead make
# its profit from the advanced features of the network, such as:
#
#     * memberships for reduced fees
#     * individual assets
#     * withdrawal permissions
#     * proposals
#     * prediction market
#     * among others
#
# Important factors:
#
# - All flat fees here are basic member fees. For LTM, most fees get cur
#   by 80%
#
# - The flat fees below are denoted in USD even though the network asks for fees
#   in BTS. This means that the BTS fees have to be adjusted from time to time
#   to follow BTS' volatility. This can be achieved by scripting easily.
#
# - In order to show stability to investors, businesses, and customers, the flat
#   USD denoted fees should not be changed for an interval of AT LEAST 6 months.
#   Hence, we should find a consensus for a USD-denoted fee schedule and
#   stick with it.
#
# - All fees in this document are proposals, ands thus not final. They further
#   require committee's approval.
#
# - It makes sense to incorporate the opinions and requirements of businesses
#   running on top of BitShares as far as possible. We need them! Hence, we should
#   talk to:
#
#       * OpenLedger
#       * metaexchange
#       * bitcash
#       * transwiser
#       * freebie
#       * bunkerchainlabs
#       * peermit
#
#   Centralized exchanges are not part of this list since they mainly benefit from
#   reduced transfer fees and don't run a business *whithin* BitShares (i.e. no
#   referral program, no use of special blockchain capabilities)
#
# Conclusion:
#
# The proposal above as well as the flat fees below try to find a balance
# between cheaper transfers and improving the liquidity of the DEX while still
# having marketers benefit from the referral program. This is achieved by
# reducing the flat fees of the core transfer and trading operations, adding a
# percentage market fee and increasing the fees associated with operations that
# are special to BitShares alone and have only fee competitors. In order to
# attract people to the DEX, we need to be competing with centralized exchanges
# in terms of fees in the beginning and once people realize the power of
# decentralized trading, the fees could potentially be raised slightly.
#
#
#
#
#
native_fees = {#####################################################
               # REGULAR OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Balance Claims are used to claim funds from the genesis
               #     block, i.e. BTS 1. Hence this operation will always be
               #     fee free.
               #
               "balance_claim": {},
               #####################################################
               #
               # Description:
               #
               #     Transfer of any asset that use the flat fee model pay
               #     this fee.
               #
               # Rational:
               #
               #     * Transactions are stored indefinitely on the blockchain
               #     * Most competitors have a fee of about $1c
               #     * Transfers are a core product of BTS
               #       Most people in crypto space use crypto tokens mostly to
               #       transfer value and they are not interested in other
               #       features.
               #     * Businesses based on the Referral program depend on
               #       income from their customers operations
               #     * Too high fee is hinders user-adoption
               #
               # Current Stats:
               #
               #     * 150-200 transfers per day
               #     * current fee: 30 BTS
               #     * makes: 4500-6000 BTS per day
               #     * that makes 3600-4800 BTS per day per user for the
               #       referral program
               #     * in dollars, this is 14.40-19.20 USD per user
               #
               # Compared to Bitcoin:
               #
               #     * BitShares is capable to run way more transactions than Bitcoin
               #     * 220.000 transactions/transfers per day
               #     * result in 19k USD transaction fees (payed to miners)
               #
               #     Assuming 220k transfers per day on bitshares:
               #     * 220000 * 30BTS * 0.004 USD/BTS = 26k USD
               #
               # Conclusion:
               #
               #     * At BTC load, BTS income from transfers would be 40% above BTC's
               #     * Thus, fees can be reduced by 40% to compete with BTC
               #     * Reducing by another 40% to incentivized people to use BTS instead of BTC
               #     * Proposed transfer fee:
               #           30 * (1-80%) = 6 BTS (approx $2.4c)
               #     * Let Referral program businesses make more profit from
               #       other features that are considered less 'core'-ish
               #     * price_per_kbyte relatively high in order to:
               #          * prevent people from storing raw data in transfers and thus the blockchain
               #          * still allow long memos:
               #               1 char  =  1 byte
               #              32 chars = 32 bytes (should be sufficient to cover most use cases)
               #              32 bytes / 1024 bytes per kbyte * 0.01 = 0.0031 USD = $0.31c (extra for the memo)
               #
               "transfer": {
                   "fee": 0.024,
                   "price_per_kbyte": 0.01
               },
               #####################################################

               #####################################################
               # ORDER OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Limit orders are the operations required to place orders
               #     in the DEX that have a price and an amount. Thus, this
               #     represent the core operation required to operate in the
               #     decentralized exchange.
               #
               # Rational:
               #
               #     * these represent a core feature of BitShares
               #     * a fee set to high will hinder market makers and thus liquidity
               #     * with less liquidity we cannot attract users
               #     * a fee that is too low has two issues:
               #         * open up a spam attack vector
               #         * does more harm than good to the blockchain
               #     * a compromise has to be found
               #     * in contrast to other exchanges:
               #          * if an order is not matched, only the cancellation
               #            fee will be applied and the creation fee will be
               #            refunded
               #          * depending on the asset, there is no percentage
               #            market fee, but a flat fee
               #
               # Other exchanges:
               #
               #     * percentage trading fee 0.1%-0.25% fee on market orders
               #       (maker/taker)
               #     * no flat fees for orders
               #     * Assuming a daily volume of 2,500,000 $ (Kraken) this
               #       makes them an income of 6,500 USD daily
               #     * no status about number of trades are available
               #     * Assuming an average trade amount of $500, we get 25k
               #       trades
               #
               #     Assuming 25k orders per day in bitshares:
               #     * 25k * 10 BTS * 0.004 USD/BTS = 1000 USD per day (only from
               #       flat fees, independent of whether the trade has been filled or
               #       not)
               #     * Currently 0% trading fee on most bitAssets (committee-owned)
               #
               # Conclusion
               #
               #     * The dex is VERY cheap already considering only filled orders
               #     * Since cancellation is almost for free, liquidity
               #       providers shouldn't worry at all
               #     * Having a trading fee that is higher than transfer makes
               #       no sense and people would stick with trading on external
               #       exchanges
               #     * As we cannot distinguish maker from taker yet (MAKER
               #       proposal), we charge a flat fee for the operations, which
               #       hurts market makers and liquidity providers as they pre-pay
               #       the fees even if their orders are not filled.
               #     * Instead of benefiting from the flat fees, we should encourage
               #       liquidity providers by very low flat fees and raise the
               #       percentage trading fee for all committee-owned assets (as
               #       described in the introduction).
               #     * Regional differences can be made to distinguish CNY from USD,
               #       GOLD and EUR.
               #     * I thus propose a $0.001c flat fee and rising the percentage
               #       trading fee to 0.15% per filled trade.
               #
               "limit_order_create": {
                   "fee": 0.001
               },
               #####################################################
               #
               # Description:
               #
               #     Cancellation of orders has to cost a fee because otherwise,
               #     the network can be spammed by opening and closing unfilled
               #     orders easily.
               #
               # Conclusion:
               #
               #     Since the purpose of this fee is merely to prevent spam
               #     attacks, we can set it at its bare minimum. Assuming an
               #     attacker can be allowed to put 10k transactions at a price
               #     of $10, we get a fee of 0.001.
               #
               "limit_order_cancel": {
                   "fee": 0.001
               },
               #####################################################
               #
               # Description:
               #
               #     Call orders are orders that are created when borrowing
               #     MPAs from the network given collateral.
               #
               # Conclusion:
               #
               #     Since this operation is crucial for liquidity in
               #     bitassets, we should set it to the bare minimum.
               #
               "call_order_update": {
                   "fee": 0.001
               },
               #####################################################
               #
               # Description:
               #
               #     Fill orders are virtual orders that cannot be created, nor
               #     can they pay a fee.
               #
               "fill_order": {},
               #####################################################

               #####################################################
               # ASSET OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Asset create distinguishes its fee depending on the length
               #     of the symbol.
               #
               # Rational:
               #
               #     * Assets are created rarely in general
               #     * Assets, even though they seem to be a core product of
               #       BitShares, the creation of them is not a core operation
               #     * Creating an asset is a one-time fee
               #     * Depending on whether the shareholders would like to see
               #       many, many more assets, even the longer symbol assets
               #       shouldn't be too cheap.
               #     * Businesses that refer others to BitShares that are
               #       interested in creating new tradable assets, should
               #       benefit from it and see this as a core value
               #       proposition.
               #     * Symbols can only be registered once
               #     * We need to prevent squatting of premium symbols
               #
               # Conclusion
               #
               #     * Premium symbols should be considered very expensive and
               #       only given away for people that what to establish REAL
               #       business. Those should certainly be able to afford some
               #       higher fee.
               #     * The price of long symbols can be rather cheap to allow
               #       individuals that have certain plans to register an asset.
               #     * Since the fixed fees are preventing spam and abuse of
               #       the blockchain as storage, the price per kbyte can be left
               #       rather low to allow lengthy descriptions:
               #          1 page of text description is about 1kb of data and
               #          should cost about $1c extra
               #
               "asset_create": {
                   "long_symbol": 50,
                   "symbol4": 2000,
                   "symbol3": 8000,
                   "price_per_kbyte": 0.01
               },
               #####################################################
               #
               # Description:
               #
               #     Every created asset comes with zero issued shares. This
               #     operation can issue new shares to any account.
               #
               # Rational:
               #
               #     * Assets have been registered for a rather high fee already
               #     * existing assets shouldn't be allowed to issue new shares for free
               #     * issuing new shares should be considered a rare operation
               #     * the referral program shouldn't benefit more from it
               #       since the asset_creation has already paid into the program
               #
               # Conclusion:
               #
               #     * Any fee between $0.50-$5 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_issue": {
                   "fee": 1,
                   "price_per_kbyte": 0.007
               },
               #####################################################
               #
               # Description:
               #
               #     Any asset can change change most of its parameters such as
               #     description, permissions, etc.
               #
               # Rational:
               #
               #     * most assets will probably never need to change at all
               #     * prediction market assets should change to be re-used after settlement
               #
               # Conclusion:
               #
               #     * Any fee between $0.50-$5 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_update": {
                   "fee": 2,
                   "price_per_kbyte": 0.007,
               },
               #####################################################
               #
               # Description:
               #
               #     Funding the fee pool is an essential operation by the
               #     issuer to allow fee payments in any native asset.
               #
               # Rational:
               #
               #     * User experience is improved by the fee pool
               #     * The issuer presumable payed for creating the asset
               #       already
               #     * This operation is considered a rare operation
               #     * Not much money can be made from this operation
               #     * This fee can easily be forwarded to the users/traders of
               #       the asset by a percentage market fee.
               #
               # Conclusion:
               #
               #     * Any fee between $0.10-$2 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_fund_fee_pool": {
                   "fee": 0.50
               },
               #####################################################
               #
               # Description:
               #
               #     User Issued Assets can be returned to the issuer by this
               #     operation
               #
               # Rational:
               #
               #     * This is considered a rare operation
               #     * Not many reasons can currently be given to use this
               #       operation at all
               #     * This fee can be reconsidered once a business makes use
               #       of it
               #
               # Conclusion:
               #
               #     * Any fee between $0.10-$5 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_reserve": {
                   "fee": 1
               },
               #####################################################
               #
               # Description:
               #
               #     Market Pegged Assets can be settled at the feed price to
               #     obtain collateral of shorts that are backed the least.
               #
               # Rational:
               #
               #     * This operation should be discouraged to bring people
               #       to use the actual order books and provide liquidity.
               #     * This operation should be considered a rare operation.
               #     * People seeking immediate liquidation should pay extra to
               #       use this feature
               #
               # Conclusion:
               #
               #     * Any fee between $2-$50 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_settle": {
                   "fee": 10
               },
               #####################################################
               #
               # Description:
               #
               #     Global Settlement is used by prediction markets to settle a bet.
               #
               # Rational:
               #
               #     * This is considered a regular operation for prediction markets
               #     * every prediction market should run this operation at least once
               #     * reuse of assets for prediction markets allow to settle
               #       it more often (needs clarification)
               #     * Issuers presumably profit from running a prediction
               #       market can can pay a few dollars fee.
               #
               # Conclusion:
               #
               #     * Any fee between $1-$10 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_global_settle": {
                   "fee": 5
               },
               #####################################################
               #
               # Description:
               #
               #     Used to transfer accumulated fees back to the issuer's balance.
               #
               # Rational:
               #
               #     * This is considered a rare operation
               #     * every issuer that either uses percentage market fees or
               #       the fee pool may eventually use this operation
               #     * Making a profit out of using the decentralized exchange
               #       may require a higher fee
               #
               # Conclusion:
               #
               #     * Any fee between $1-$10 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_claim_fees": {
                   "fee": 1,
               },
               #####################################################
               #
               # Description:
               #
               #     Feed producers for non-witness and non-committee feed
               #     provider assets can change the fee producers.
               #
               # Rational:
               #
               #     * This is considered a rare operation
               #     * many issuers of MPA that either uses percentage market
               #       fees or the fee pool may eventually use this operation
               #     * Making a profit out of using the decentralized exchange
               #       may require a higher fee
               #
               # Conclusion:
               #
               #     * Any fee between $1-$10 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_update_feed_producers": {
                   "fee": 5
               },
               #####################################################
               #
               # Description:
               #
               #     Feeds need to be published on the chain to allow settlement
               #     and margin calls as well as to resolve a prediction market.
               #
               # Rational:
               #
               #     * prediction markets rarely publish (and thus settle)
               #       their assets
               #     * market pegged assets require a frequent update of the
               #       feed to follow external market sentiments
               #     * even though witnesses get paid to publish feeds for
               #       smartcoins, they should not be discouraged to provide a
               #       high frequent and reliable fee
               #     * those that use this operation on a regular basis
               #       (witnesses), do not contribute to the referral program
               #
               # Conclusion:
               #
               #     Anything above the bare minimum is considered harmful!
               #
               "asset_publish_feed": {
                   "fee": 0.0001
               },
               #####################################################
               #
               # Description:
               #
               #     Bitassets can be updated to change settlement parameters etc.
               #
               # Rational:
               #
               #     * This is considered a very rare operation
               #     * Most MPA will never be updated if they have been created
               #       correctly
               #
               # Conclusion:
               #
               #     * Any fee between $1-$10 seems to be reasonable considering
               #       the above arguments.
               #
               "asset_update_bitasset": {
                   "fee": 5
               },
               #####################################################

               #####################################################
               # ACCOUNT OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Account upgrades to lifetime membership or annual
               #     membership to reduce their own fees
               #
               # Rational:
               #
               #     * Motivation to upgrade the account is reduced fees in future
               #     * Mostly interesting for power that already know the mechanics
               #     * Break even points for traders and transfer-users (payment) differ
               #     * Once a users is upgraded, ties to the referrer are cut
               #     * Businesses in the Referral Program seek revenue from their users
               #     * Hence, this operation is the last hurdle for customers
               #       to reduce fees and opt-out of the referral program
               #
               # Conclusion:
               #
               #     * Since transfer fees have been reduced, increasing the
               #       upgrade fee is reasonable
               #     * For traders, the break even point is reached after 1000
               #       filled orders, or 20,000 canceled unfilled orders
               #     * For transfers, the break even point is reached after 830
               #       transfers (assuming no memo)
               #
               "account_upgrade": {
                   "membership_annual_fee": 20,
                   "membership_lifetime_fee": 150
               },
               #####################################################
               #
               # Description:
               #
               #     An asset using whitelists requires holders to be
               #     whitelisted in order to hold or move the asset.
               #
               # Rational:
               #
               #     * This feature is mostly of interest to businesses
               #     * Depending on the business, this is considered a rather
               #       frequent operation
               #     * each account to whitelist has to have its own operation
               #     * no business uses this operation yet
               #     * has to be reconsidered once usage increases
               #     * someone leveraging this feature can probably forward the
               #       costs
               #
               # Conclusion:
               #
               #     * Any fee between $0.10-$1 seems to be reasonable considering
               #       the above arguments.
               #
               "account_whitelist": {
                   "fee": 0.10
               },
               #####################################################
               #
               # Description:
               #
               #     To transfer accounts to another owner, a separated operation exists.
               #
               # Rational:
               #
               #     * In my opinion, this operation has no use at all and the
               #       same can be achieved by the account_update_operation
               #
               # Conclusion:
               #
               #     * Anything can be used here
               #
               "account_transfer": {
                   "fee": 5
               },
               #####################################################
               #
               # Description:
               #
               #     Account updates are used to change settings of an account
               #
               # Rational:
               #
               #     * the governance mechanics require accounts to change in
               #       order to cast a vote
               #     * having a high fee will lead to less votes being cast or changed
               #
               # Conclusion:
               #
               #     * This operation should be as cheap as possible
               #     * The price per kbyte fee should mostly prevent spam
               #
               "account_update": {
                   "fee": 0.001,
                   "price_per_kbyte": 0.007
               },
               #####################################################
               #
               # Description:
               #
               #      Accounts are created by this operation. Depending on the
               #      name being premium or not the fee changes.
               #
               # Rational:
               #
               #     * Business in the referral program will make use of this feature
               #     * squatters should pay more to get a premium name
               #     * this operation is not included in the referral program
               #     * most businesses in the referral program will allow only
               #       basic account names
               #     * premium names will probably only be bought by LTM themselves
               #
               # Conclusion:
               #
               #     * the basic fee should be low to incentivize the referral business
               #     * the premium fee can be quite high to prevent squatters
               #       and make a profit for the rare namespace
               #     * The price per kbyte fee should mostly prevent spam
               #
               "account_create": {
                   "basic_fee": 0.10,
                   "premium_fee": 5,
                   "price_per_kbyte": 0.007
               },
               #####################################################

               #####################################################
               # VESTING OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     The chain allows a user to create a vesting balance.
               #     Normally, vesting balances are created automatically as
               #     part of cashback and worker operations.
               #
               # Rational:
               #
               #     * There is no reason for an end user to use this operation
               #       at all (currently).
               #
               # Conclusion:
               #
               #     * The fee could be anything
               #
               "vesting_balance_create": {
                   "fee": 5
               },
               #####################################################
               #
               # Description:
               #
               #     This operation is used to withdraw worker/witness pay and
               #     the cashback balance.
               #
               # Rational:
               #
               #     * This operation should be considered relatively rare
               #     * Worker and witnesses get payed by the chain anyway and
               #       can ask for higher pay to compensate
               #     * Cashback users make use of the referral program and can
               #       share a flat fee of their income made from the network
               #
               # Conclusion:
               #
               #     * Any fee between $0.10-$5 seems to be reasonable considering
               #       the above arguments.
               #
               "vesting_balance_withdraw": {
                   "fee": 2
               },
               #####################################################

               #####################################################
               # WORKER OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Workers can be created in order to get payed by the blockchain
               #
               # Rational:
               #
               #     * workers that get approved can easily offset this fee by
               #       a higher pay
               #     * workers that do not get approved should be encouraged to
               #       improve their proposal
               #     * this operation is considered a rare operation
               #     * this operation does not participate in the referral
               #       program
               #
               # Conclusion:
               #
               #     * Any fee between $2-$50 seems to be reasonable considering
               #       the above arguments.
               #
               "worker_create": {
                   "fee": 5
               },
               #####################################################

               #####################################################
               # WITNESS OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Block producers have been created by this operation
               #
               # Rational:
               #
               #     * witnesses need to have a proposal to convince shareholders
               #     * witnesses get elected by shareholders
               #     * witnesses are highly honored entities that get paid for
               #       block production
               #     * proposals not considered serious enough are not elected
               #       and can't offset the fee
               #     * a high fee reduces spam and encourages people to take
               #       the business serious
               #     * this operation does not participate in the referral
               #       program
               #     * a too high fee could be perceived as gate-keeping
               #
               # Conclusion
               #
               #     * This fee should be considered a motivation for new
               #       witnesses to prepare good proposal to convince
               #       shareholders.
               #
               "witness_create": {
                   "fee": 50
               },
               #####################################################
               #
               # Description:
               #
               #     The sole purpose of this operation is to change the owner
               #     of a witness.
               #
               # Rational:
               #
               #     * This operation is considered a very rare operation
               #     * May be used to run backup witness servers
               #
               # Conclusion:
               #
               #     Anything above the bare minimum is considered harmful!
               #
               "witness_update": {
                   "fee": 2
               },
               #####################################################

               #####################################################
               # PROPOSAL OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Proposals are used to secure funds against
               #     loss/corruption or theft of private keys as well as
               #     for making committee decisions.
               #
               # Rational:
               #
               #     * proposals are an integral part of account security
               #     * eventually, we will see a lot of proposals being
               #       created from users
               #     * expensive proposals might hinder businesses but will
               #       most certainly hold users back from using it
               #     * since it is a potentially frequent operation, some
               #       profit can be made
               #
               # Remark:
               #
               #     * since the author of this file is launching a business
               #       around proposals, non of what is said here should be
               #       taken for a fact!
               #
               # Conclusion:
               #
               #     * Given above arguments,
               #     * The price per kbyte fee should mostly prevent spam since
               #       the proposed operations themselves will pay another fee
               #     * on the other hand, invalid (or not approved proposals)
               #       could be used to put arbitrary operations with arbitrary
               #       data on the blockchain for the cost of the proposal only.
               #     * thus we could have a cheap flat fee and a rather high
               #       kbyte fee
               #
               "proposal_create": {
                   "fee": 0.15,
                   "price_per_kbyte": 0.05
               },
               #####################################################
               #
               # Description:
               #
               #     Proposals can be deleted before their expire.
               #
               # Rational:
               #
               #     * This can be considered a rare operation
               #     * Mostly interesting for committee and governance actions
               #
               # Conclusion:
               #
               #     * Any fee between $0.10-$2 seems to be reasonable considering
               #       the above arguments.
               #
               "proposal_delete": {
                   "fee": 0.50
               },
               #####################################################
               #
               # Description:
               #
               #     Proposals can be approved or approvals can be removed.
               #     Both perform a proposal_update operation.
               #
               # Rational:
               #
               #     * this operation is a requirement for the success of any
               #       proposal.
               #
               # Conclusion:
               #
               #     * Since adding/removing approvals is an integral part of
               #       proposal, which already pays a fee, we can have a lower
               #       one here
               #     * no real data be added except for valid public keys,
               #       hence the per kbyte fee is rather low
               #
               "proposal_update": {
                   "fee": 0.005,
                   "price_per_kbyte": 0.007
               },
               #####################################################

               #####################################################
               # COMMITTEE OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Committee members are created with this operation
               #
               # Rational:
               #
               #     * this should be considered a rather rare operations
               #     * committee members need to have a proposal to convince
               #       shareholders
               #     * committee members get elected by shareholders
               #     * a high fee reduces spam and encourages people to take
               #       the business serious
               #     * this operation does not participate in the referral
               #       program
               #     * a too high fee could be perceived as gate-keeping
               #     * committee members have more influence on business
               #       decisions on BitShares
               #     * some committee members may run their own business in
               #       BitShares
               #
               # Conclusion
               #
               #     * This fee should be considered a motivation for new
               #       committee members to prepare good proposal to convince
               #       shareholders.
               #
               "committee_member_create": {
                   "fee": 5
               },
               #####################################################
               #
               # Description:
               #
               #     Global parameters, such as bock size and confirmation
               #     interval can be changed with this operation.
               #
               # Rational:
               #
               #     * this should be considered a extremely rare operations
               #     * the fee is always going to be paid by the
               #       committee-account
               #     * It doesn't really matter what fee is chosen here. If the
               #       committee sees the need for a change, then they will pay
               #       it.
               #     * this operation is so rare, it will probably be executed
               #       at most 1 a year
               #     * this operation does not pay to the referral program
               #
               # Conclusion:
               #
               #     * We can set anything over here, it doesn't really matter.
               #
               "committee_member_update_global_parameters": {
                   "fee": 5
               },
               #####################################################
               #
               # Description:
               #
               #     Similar to witness update, allows to change the owning
               #     account of a committee member.
               #
               # Rational:
               #
               #     * Assuming that shareholders accept the handing over of a
               #       committee position, this operation shouldn't be
               #       recommended at all.
               #     * thus, this is considered a rare operation
               #     * the correct way to get hand on a committee position is
               #       to create a committee account and have it elected.
               #
               # Conclusion:
               #
               #     * To prevent misuse, this operation should cost at least
               #       the fee of creating a new committee account, probably
               #       more.
               "committee_member_update": {
                   "fee": 10
               },
               #####################################################

               #####################################################
               # BLIND/STEALTH OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Blind transfers are in the STEALTH program. This operation
               #     is for blind->blind transfers.
               #
               # Rational:
               #
               #     * a percentage of this fee goes to the FBA STEALTH
               #     * the privacy mode is an integral part of BitShares
               #     * this is considered to be a highly used operation
               #     * the costs for the end user are predefined from the
               #       STEALTH proposal as 3 times the transfer fee
               #
               # Conclusion:
               #
               #     * Not much can be discussed here as the STEALTH worker has
               #       been approved by shareholders including the rule for a 3
               #       times the transfer fee requirement.
               #
               "blind_transfer": {
                   "fee": 3 * 0.024,
                   "price_per_kbyte": 3 * 0.01
               },
               #####################################################
               #
               # Description:
               #
               #     Transfer from a blinded/privacy account. This operation is
               #     for blind->non-blind transfers
               #
               # Rational:
               #
               #     * any funds in a private account may eventually be
               #       transfered by this operation.
               #     * if the fee is set high, people are discouraged to move
               #       funds back to a public account
               #     * fee should be 3x the transfer fee
               #     * this transfer has no price per kbyte as it does not
               #       carry a memo.
               #
               # Conclusion:
               #
               #     * Not much can be discussed here as the STEALTH worker has
               #       been approved by shareholders including the rule for a 3
               #       times the transfer fee requirement.
               #
               "transfer_from_blind": {
                   "fee": 3 * 0.024,
               },
               #####################################################
               #
               # Description:
               #
               #     Transfer from a blinded/privacy account. This operation is
               #     for non-blind->blind transfers
               #
               # Rational:
               #
               #     * any funds in a private account may eventually be
               #       transfered by this operation.
               #     * if the fee is set high, people are discouraged to move
               #       funds back to a public account
               #     * fee should be 3x the transfer fee
               #
               # Conclusion:
               #
               #     * Not much can be discussed here as the STEALTH worker has
               #       been approved by shareholders including the rule for a 3
               #       times the transfer fee requirement.
               #
               "transfer_to_blind": {
                   "fee": 3 * 0.024,
                   "price_per_kbyte": 3 * 0.01
               },
               #####################################################

               #####################################################
               # WITHDRAW PERMISSION OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     Withdraw permission are used for the recurring payments
               #     program. This op allows someone else to withdraw funds up
               #     to a limit from your account.
               #
               # Rational:
               #
               #     * Given that this feature can be used for scheduled
               #       payments, it should be considered a core feature
               #     * Since competitors (banks) allow withdrawals for almost
               #       free the fee should be rather high.
               #     * Given that you can here define an upper limit for
               #       withdrawals, the extra functionality should be paid by the
               #       user.
               #     * withdraw permissions are assumed to be rather rare.
               #
               # Conclusion:
               #
               #     * Given that this feature adds more functionality to your
               #       account than a regular bank account, we can ask for a
               #       little fee here. Anything from $0.10 to $5 might be
               #       considered fair.
               #
               "withdraw_permission_create": {
                   "fee": 1
               },
               #####################################################
               #
               # Description:
               #
               #     Withdraw permissions can be updated to reflect real-world
               #     changes.
               #
               # Rational:
               #
               #     * Since the creation of a withdraw permission has already
               #       paid a fee, updating a permission should be at least
               #       less than the cost for deleting and creating a new one.
               #
               # Conclusion:
               #
               #     * Given that this is a rare operation, and want to
               #       encourage people to use it, we cannot ask for more than
               #       $10c.
               #
               "withdraw_permission_update": {
                   "fee": 0.10
               },
               #####################################################
               #
               # Description:
               #
               #     Withdraw permissions do not automatically transfer funds.
               #     Instead, they need to be claimed by the to-be-paid party.
               #
               # Rational:
               #
               #     * This operation might appear one every day/week/month for
               #       every withdrawal permission, hence it is assumed to be
               #       used frequently.
               #     * The payee will probably forward any costs to the payer
               #       thus discourage the use of withdrawal permissions.
               #
               # Conclusion:
               #
               #     * We set a minimum flat fee and have spam prevention from
               #     a medium price per kbyte.
               #
               "withdraw_permission_claim": {
                   "fee": 0.001,
                   "price_per_kbyte": 0.007
               },
               #####################################################
               #
               # Description:
               #
               #     Withdraw permission can be deleted of course.
               #
               # Rational:
               #
               #     * this order corresponds to the update operation and is
               #       considered a rare operation
               #     * we should not discourage the use of this feature by
               #       having an expensive cancellation fee
               #
               # Conclusion:
               #
               #     * Given that this is a rare operation, and want to
               #       encourage people to use it, we cannot ask for more than
               #       $10c.
               #
               "withdraw_permission_delete": {
                   "fee": 0.10
               },
               #####################################################

               #####################################################
               # CUSTOM/OTHER OPERATIONS
               #####################################################
               #
               # Description:
               #
               #     The custom operation can be used to store arbitrary data
               #     on the blockchain that is not validated by the blockchain
               #     protocol.
               #
               # Rational:
               #
               #     * The purpose of this operation is to use BitShares as
               #       underlying data storage layer
               #     * mainly the data should be hashes only to not bloat the
               #       blockchain
               #     * flat fee is to prevent spamming with small custom operations
               #     * per kbyte fee is used to prevent spamming with huge
               #       amounts of data
               "custom": {
                   "fee": 0.10,
                   "price_per_kbyte": 0.01
               },
               #####################################################
               #
               # Description:
               #
               #     assert that some conditions are true. This operation
               #     performs no changes to the database state, but can but
               #     used to verify pre or post conditions for other
               #     operations.
               #
               # Note:
               #
               #     Until we figured out what we can do with this operation,
               #     it should probably be rather expensive.
               #
               "assert": {
                   "fee": 10
               },
               #####################################################
               #
               # Description:
               #
               #     Allows the issuer of an asset to transfer an asset from
               #     any account to any account if they have
               #     override_authority.
               #
               # Rational:
               #
               #     * The main purposes of this operation are:
               #        a) legal compliance
               #        b) allow to reuse prediction markets (needs clarification)
               #     * this is considered a rather rare event
               #     * in the case of prediction markets, the issuer has
               #       probably made some profit from percentage market fees
               #       that he is able to share with the shareholders by means
               #       of this fee.
               #
               # Conclusion:
               #
               #     * Flat fees of $0.50 to $5 seem reasonable
               #     * kbyte price is required to prevent data spamming.
               #
               "override_transfer": {
                   "fee": 1,
                   "price_per_kbyte": 0.007
               },
               #####################################################
               }

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
expires_from_now = 60 * 60 * 24 * 2

""" What tolerance (in percent) is ok when comparing/verifying an active
    proposal?
"""
tolerance_percentage = 5  # %
