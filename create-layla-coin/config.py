# Modify this file as you run through the tutorial

creator_address = ""
creator_passphrase = ""
receiver_address = ""
receiver_passphrase = ""

# Credentials to connect through an algod client
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# Details of the asset creation transaction
asset_details = {
	"asset_name": "DogCoin",
	"unit_name": "Woof",
	"total": 888888888,
	"decimals": 2,
	"default_frozen": False,
	"manager": creator_address,
	"reserve": creator_address,
	"freeze": creator_address,
	"clawback": creator_address,
	"url": "LaylaGyoza.jpg",
	"metadata_hash": b'O\x88\xfd\xf2\xd1\xfe\xee\x96+\xf9\xf0\xb6\xb2\x8d\r\xb5\xced)#\x9bV\xce\xa4\x81\xa6\xb9\xbd\x0e\xf7al'
}

metadata_file = "LaylaGyoza.jpg"
metadatahash_b64 = "T4j98tH+7pYr+fC2so0Ntc5kKSObVs6kgaa5vQ73YWw="

# The asset ID is available after the asset is created.
asset_id = 0 # change this