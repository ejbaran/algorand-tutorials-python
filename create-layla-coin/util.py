import hashlib
import base64
from algosdk import account, mnemonic

def generate_new_account():
	"""
	Generate a new Algorand account and print the public address
	and private key mnemonic.
	"""
	private_key, public_address = account.generate_account()
	passphrase = mnemonic.from_private_key(private_key)
	print("Address: {}\nPassphrase: \"{}\"".format(public_address, passphrase))

def wait_for_confirmation(client, transaction_id, timeout):
    """
	https://developer.algorand.org/docs/build-apps/hello_world/#wait-for-confirmation
    Wait until the transaction is confirmed or rejected, or until 'timeout'
    number of rounds have passed.
    Args:
        transaction_id (str): the transaction to wait for
        timeout (int): maximum number of rounds to wait    
    Returns:
        dict: pending transaction information, or throws an error if the transaction
            is not confirmed or rejected in the next timeout rounds
    """
    start_round = client.status()["last-round"] + 1;
    current_round = start_round

    while current_round < start_round + timeout:
        try:
            pending_txn = client.pending_transaction_info(transaction_id)
        except Exception:
            return 
        if pending_txn.get("confirmed-round", 0) > 0:
            return pending_txn
        elif pending_txn["pool-error"]:  
            raise Exception(
                'pool error: {}'.format(pending_txn["pool-error"]))
        client.status_after_block(current_round)                   
        current_round += 1
    raise Exception(
        'pending tx not found in timeout rounds, timeout value = : {}'.format(timeout))

def hash_file_data(filename, return_type="bytes"):
	"""
	Takes any byte data and returns the SHA512/256 hash in base64.
	"""
	filebytes = open(filename, 'rb').read()
	h = hashlib.sha256()
	h.update(filebytes)
	if return_type == "bytes":
		return h.digest()
	elif return_type == "base64":
		return base64.b64encode(h.digest())

def sign_and_send(txn, passphrase, client):
	"""
	Signs and sends the transaction to the network.
	Returns transaction info.
	"""
	private_key = mnemonic.to_private_key(passphrase)
	stxn = txn.sign(private_key)
	txid = stxn.transaction.get_txid()
	client.send_transaction(stxn)
	wait_for_confirmation(client, txid, 5)
	print('Confirmed TXID: {}'.format(txid))
	txinfo = client.pending_transaction_info(txid)
	return txinfo

def balance_formatter(amount, asset_id, client):
	"""
	Returns the formatted units for a given asset and amount. 
	"""
	asset_info = client.asset_info(asset_id)
	decimals = asset_info['params'].get("decimals")
	unit = asset_info['params'].get("unit-name")
	formatted_amount = amount/10**decimals
	return "{} {}".format(formatted_amount, unit)
	