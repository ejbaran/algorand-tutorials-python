import util
import main
import config

## Create New Accounts
# from util import generate_new_account
# generate_new_account()

## Hash image
# from util import hash_file_data
# hash_file_data('LaylaGyoza.jpg')
# hash_file_data('LaylaGyoza.jpg', 'base64')

## Create Asset
from main import create
from config import creator_passphrase

create(creator_passphrase)