import json
from web3 import Web3
from brownie import UniswapV2Factory,UniswapV2Pair,EZZC,accounts
rpc_url = "http://localhost:8545"

web3 = Web3(Web3.HTTPProvider(rpc_url))
ac0 = accounts[0]
ac1 = accounts[1]
ac2 = accounts[2]
ac3 = accounts[3]
ac4 = accounts[4]
ac5 = accounts[5]
ac6 = accounts[6]
tkA =  EZZC.deploy(3000,{'from':ac1})
tkB =  EZZC.deploy(3000,{'from':ac2})
ezPair = UniswapV2Pair.deploy({'from':ac0})
ezFactory = UniswapV2Factory.deploy(ac3,{'from':ac4})
ezPair.token0 = tkA
ezPair.token1 = tkB
ezPair.factory = ezFactory

def main():
    print('token A totalsupply:')
    print(tkA.totalSupply())
    print('token A balance Of with ac1:')
    print(tkA.balanceOf(ac1))
    print('token A balance Of with ac2:')
    print(tkA.balanceOf(ac2))
    print('token A balance of ezPair:')
    print(tkA.balanceOf(ezPair.address))
    tkA.transfer(ezPair.address,100)
    print('token A balance of ezPair:')
    print(tkA.balanceOf(ezPair.address))
    print('token B balance of ezPair:')
    print(tkB.balanceOf(ezPair.address))
    tkB.transfer(ezPair.address,500)
    print('token B balance of ezPair:')
    print(tkB.balanceOf(ezPair.address))
    tkB.transfer(ezPair.address,2200)
    print(tkB.balanceOf(ezPair.address))
#    tkB.transfer(ezPair.address,500)
#    print(tkB.balanceOf(ezPair.address))

    
if __name__ == '__main__':
    main()


