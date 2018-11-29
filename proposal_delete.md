begin_builder_transaction

//this will return an integer label for this builder transaction

add_operation_to_builder_transaction (label from above) [  24,{    "fee": {      "amount": 200000,      "asset_id": "1.3.0"    },    "fee_paying_account": "1.2.(your id)",    "using_owner_authority": false,    "proposal": "1.10.(proposal to delete)",    "extensions": []  }]

// so for example if I wanted to delete proposal 1.10.50 and the builder transaction label was 0 I would.

// add_operation_to_builder 0 [  24,{    "fee": {      "amount": 200000,      "asset_id": "1.3.0"    },    "fee_paying_account": "1.2.1191",    "using_owner_authority": false,    "proposal": "1.10.50",    "extensions": []  }]

propose_builder_transaction2 (label from above) (account name) (experation time) (review period) true

// to broadcast this builder transaction as a proposal that will expire on January 12th at 12 noon, and be in reveiw for one hour I would

// propose_builder_transaction2 0 "dele-puppy" "20160112T120000" "3600" true
