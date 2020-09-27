import json
from web3 import Web3
from brownie import EZZC,accounts
rpc_url = "http://localhost:8545"

web3 = Web3(Web3.HTTPProvider(rpc_url))
ac0 = accounts[0]
ac1 = accounts[1]
ac2 = accounts[2]
ac3 = accounts[3]
ac4 = accounts[4]
ac5 = accounts[5]
ac6 = accounts[6]
ezzc =  EZZC.deploy(3000,{'from':accounts[0]})

def main():
    print(ezzc.balance())
    
if __name__ == '__main__':
    main()


