// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import {Challenge} from "./Challenge.sol";

interface IChallenge {
	function owner() external view returns (address);
}

contract Setup {
	address public owner;
	mapping(address => address) public playersInstanceMapping;

	constructor() {
		owner = msg.sender;
	}

	function register() external payable {
		require(playersInstanceMapping[msg.sender] == address(0), "Already registered");
		playersInstanceMapping[msg.sender] = address(new Challenge());
	}

	function getChallenge() external view returns (address) {
		return playersInstanceMapping[msg.sender];
	}

	function isSolved(address player) external view returns (bool) {
		return IChallenge(playersInstanceMapping[player]).owner() == player;
	}
}