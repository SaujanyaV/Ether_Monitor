from web3 import Web3

bsc = "https://bsc-dataseed2.binance.org/" #Put relevant RPC server here according to Mainnet
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

check_address = "Put your address here"

bnb_available = web3.fromWei(web3.eth.get_balance(check_address), 'ether')
print(f'BNB: {bnb_available}')