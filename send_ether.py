from web3 import Web3

bsc = "https://bsc-dataseed2.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

#Send to my account
account_1 = "Account1 address"
acc1_key = "Account1 key"

account_2 = "Account2 address"

#Get account1 nonce
nonce = web3.eth.getTransactionCount(account_1)

#Amount of bnb you want to transfer
send_bnb = web3.toWei('1', 'ether')

#Build transaction
token_tx = {
            'nonce': nonce,
            'to': account_2,
            'value': send_bnb,
            'gas': 21000,
            'gasPrice': web3.toWei('5', 'gwei')
        }

#Sign and send tx
signed_tx = web3.eth.account.signTransaction(token_tx, acc1_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(f'{send_bnb} bnb sent')
print(web3.toHex(tx_hash))