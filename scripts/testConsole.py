import json
from web3 import Web3
from brownie import EZZC,accounts
rpc_url = "http://localhost:8545"

def main():
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    ezzc =  EZZC.deploy(3000,{'from':accounts[1]})

if __name__ == '__main__':
    main()


