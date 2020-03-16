#/usr/bin/python3
from liz import *
from algosdk import algod
from algosdk import account, mnemonic
from algosdk.transaction import write_to_file
from algosdk.transaction import AssetConfigTxn, AssetTransferTxn
from util import add_network_params, sign_and_send, balance_formatter


client = algod.AlgodClient(algod_token, algod_address)

def create(passphrase=None):
	"""
	Returns an unsigned txn object and writes the unsigned transaction
	object to a file for offline signing. Uses current network params.
	"""

	data = add_network_params(asset_details, client)
	txn = AssetConfigTxn(**data)
	if passphrase:
		txinfo = sign_and_send(txn, passphrase, client)
		print("Create asset confirmation, txid: {}".format(txinfo.get('tx')))
		asset_id = txinfo['txresults'].get('createdasset')
		print("Asset ID: {}".format(asset_id))
	else:
		write_to_file([txn], "create_coin.txn")

def optin(passphrase=None):
	"""
	Creates an unsigned opt-in transaction for the specified asset id and 
	address. Uses current network params.
	"""
	optin_data = {
		"sender": receiver_address,
		"receiver": receiver_address,
		"amt": 0,
		"index": asset_id
	}
	data = add_network_params(optin_data, client)
	txn = AssetTransferTxn(**data)
	if passphrase:
		txinfo = sign_and_send(txn, passphrase, client)
		print("Opted in to asset ID: {}".format(asset_id))
		print("Transaction ID Confirmation: {}".format(txinfo.get("tx")))
	else:
		write_to_file([txns], "optin.txn")

def transfer(passphrase=None):
	"""
	Creates an unsigned transfer transaction for the specified asset id, to the 
	specified address, for the specified amount.
	"""
	amount = 6000
	transfer_data = {
		"sender": creator_address,
		"receiver": receiver_address,
		"amt": amount,
		"index": asset_id
	}
	data = add_network_params(transfer_data, client)
	txn = AssetTransferTxn(**data)
	if passphrase:
		txinfo = sign_and_send(txn, passphrase, client)
		formatted_amount = balance_formatter(amount, asset_id, client)
		print("Transferred {} from {} to {}".format(formatted_amount, 
			creator_address, receiver_address))
		print("Transaction ID Confirmation: {}".format(txinfo.get("tx")))
	else:
		write_to_file([txns], "transfer.txn")

def check_holdings(asset_id, address):
	"""
	Checks the asset balance for the specific address and asset id.
	"""
	account_info = client.account_info(address)
	assets = account_info.get("assets")
	if assets:
		asset_holdings = account_info["assets"]
		asset_holding = asset_holdings.get(str(asset_id))
		if not asset_holding:
			print("Account {} must opt-in to Asset ID {}.".format(address, asset_id))
		else:
			amount = asset_holding.get("amount")
			print("Account {} has {}.".format(address, balance_formatter(amount, asset_id, client)))
	else:
		print("Account {} must opt-in to Asset ID {}.".format(address, asset_id))
