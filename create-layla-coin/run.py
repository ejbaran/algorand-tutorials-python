# LaylaCoin Tutorial
# Single Script Executable

# Imports
import util
import main
import config

# 1. Generate the LaylaCoin Creator and Receiver Accounts
# Create New Accounts
from util import generate_new_account
generate_new_account()

# 2. Define the LaylaCoin Parameters
# Hash image
from util import hash_file_data
hash_file_data('LaylaGyoza.jpg')
hash_file_data('LaylaGyoza.jpg', 'base64')

# 3. Create LaylaCoin
# Create Asset
from main import create
from config import creator_passphrase
create(creator_passphrase)

# 4. Opt-In to Receive LaylaCoin
# Opt-in
from main import optin
from config import receiver_passphrase
optin(receiver_passphrase)

# 5. Read the LaylaCoin Balance
# Balance
from config import receiver_address, asset_id
from main import check_holdings
check_holdings(asset_id, receiver_address)

# 6. Transfer LaylaCoin to the Receiver Account
# Transfer
from config import asset_id, creator_passphrase
from main import transfer
transfer(creator_passphrase)

# Confirm
from config import creator_address, receiver_address
from main import check_holdings
