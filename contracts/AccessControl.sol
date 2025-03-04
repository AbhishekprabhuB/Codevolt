// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AccessControl {
    address public owner;
    mapping(address => bool) public accessList;

    event AccessGranted(address indexed user);
    event AccessRevoked(address indexed user);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function grantAccess(address user) public onlyOwner {
        accessList[user] = true;
        emit AccessGranted(user);
    }

    function revokeAccess(address user) public onlyOwner {
        accessList[user] = false;
        emit AccessRevoked(user);
    }

    function checkAccess(address user) public view returns (bool) {
        return accessList[user];
    }
}
