pragma solidity ^0.8.0;

contract Helper {
	address owner;

	constructor() {
		owner = msg.sender;
	}

	fallback() external {
		assembly {
			mstore(0, sload(0))
			return(0x00, 0x20)
		}
	}
}