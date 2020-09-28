pragma solidity =0.5.16;

import '../EZZCERC20.sol';

contract EZZC is EZZCERC20 {
    constructor(uint _totalSupply) public {
        _mint(msg.sender, _totalSupply);
    }
}
