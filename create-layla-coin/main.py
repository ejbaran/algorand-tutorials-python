#Imports
from config import *
from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk.future.transaction import write_to_file
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn
from util import sign_and_send, balance_formatter
from algosdk.future.transaction import AssetTransferTxn


# Client
# client = algod.AlgodClient(algod_token, algod_address)
client = algod.AlgodClient("", algod_address, headers={'User-Agent': 'DoYouLoveMe?'})

# Create function.
# Returns an unsigned txn object and writes the unsigned transaction object to a file for offline signing. 
# Uses current network params.
def create(passphrase=None):
	params = client.suggested_params()
	txn = AssetConfigTxn(creator_address, params, **asset_details)
	if passphrase:
		txinfo = sign_and_send(txn, passphrase, client)
		asset_id = txinfo.get('asset-index')
		print("Asset ID: {}".format(asset_id))
	else:
		write_to_file([txn], "create_coin.txn")

# Creates an unsigned opt-in transaction for the specified asset id and address. 
# Uses current network params.
def optin(passphrase=None):
	params = client.suggested_params()
	txn = AssetTransferTxn(sender=receiver_address, sp=params, receiver=receiver_address, amt=0, index=asset_id)
	if passphrase:
		txinfo = sign_and_send(txn, passphrase, client)
		print("Opted in to asset ID: {}".format(asset_id))
	else:
		write_to_file([txns], "optin.txn")

# Creates an unsigned transfer transaction for the specified asset id, to the specified address, for the specified amount.
#def transfer(passphrase=None):
	#amount = 6000
	#params = client.suggested_params()
	#txn = AssetTransferTxn(sender=creator_address, sp=params, receiver=receiver_address, amt=amount, index=asset_id)
	#if passphrase:
		#txinfo = sign_and_send(txn, passphrase, client)
		#formatted_amount = balance_formatter(amount, asset_id, client)
		#print("Transferred {} from {} to {}".format(formatted_amount, 
			#creator_address, receiver_address))
		#print("Transaction ID Confirmation: {}".format(txinfo.get("tx")))
	#else:
		#write_to_file([txns], "transfer.txn")

def transfer(passphrase=None):

    amount = 6000
    params = client.suggested_params()
    txn = AssetTransferTxn(sender=creator_address, sp=params, receiver=receiver_address, amt=amount, index=asset_id)
    if passphrase:
        txinfo = sign_and_send(txn, passphrase, client)
        formatted_amount = balance_formatter(amount, asset_id, client)
        print("Transferred {} from {} to {}".format(formatted_amount, 
            creator_address, receiver_address))
        print("Transaction ID Confirmation: {}".format(txinfo.get("tx")))
    else:
        write_to_file([txns], "transfer.txn")

# Checks the asset balance for the specific address and asset id.
def check_holdings(asset_id, address):
	account_info = client.account_info(address)
	assets = account_info.get("assets")
	for asset in assets:
		if asset['asset-id'] == asset_id:
			amount = asset.get("amount")
			print("Account {} has {}.".format(address, balance_formatter(amount, asset_id, client)))
			return
	print("Account {} must opt-in to Asset ID {}.".format(address, asset_id))


# Creates an unsigned opt-in transaction for the specified asset id and address. 
# Uses current network params.
def optin(passphrase=None):
    params = client.suggested_params()
    txn = AssetTransferTxn(sender=receiver_address, sp=params, receiver=receiver_address, amt=0, index=asset_id)
    if passphrase:
        txinfo = sign_and_send(txn, passphrase, client)
        print("Opted in to asset ID: {}".format(asset_id))
    else:
        write_to_file([txns], "optin.txn")
	
from util import balance_formatter

# Checks the asset balance for the specific address and asset id.
def check_holdings(asset_id, address):
    account_info = client.account_info(address)
    assets = account_info.get("assets")
    for asset in assets:
        if asset['asset-id'] == asset_id:
            amount = asset.get("amount")
            print("Account {} has {}.".format(address, balance_formatter(amount, asset_id, client)))
            return
    print("Account {} must opt-in to Asset ID {}.".format(address, asset_id))


# Creates an unsigned transfer transaction for the specified asset id, to the specified address, for the specified amount.
def transfer(passphrase=None):

    amount = 6000
    params = client.suggested_params()
    txn = AssetTransferTxn(sender=creator_address, sp=params, receiver=receiver_address, amt=amount, index=asset_id)
    if passphrase:
        txinfo = sign_and_send(txn, passphrase, client)
        formatted_amount = balance_formatter(amount, asset_id, client)
        print("Transferred {} from {} to {}".format(formatted_amount, 
            creator_address, receiver_address))
        print("Transaction ID Confirmation: {}".format(txinfo.get("tx")))
    else:
        write_to_file([txns], "transfer.txn")