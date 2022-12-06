import parser as par
def changeGlob(x,v):
    globals()[x] = v
changeGlob("syntax",{"names":["heads","subHeads","tops","type","stateMutability","precedence","globalVariables"],
                      "heads":['contract','library','interface','abstract','constructor'],
                      "subHeads":['function','modifier','event'],
                      "tops":['SPDX','pragma'],
                      "type":['uint','address','bytes','string','bool'],
                      "stateMutability":["public","private","external","internal","pure","view","payable","constant","immutable","anonymous","indexed","virtual","override"],
                      "precedence":["assert","block","coinbase","difficulty","number","block;number","timestamp","block;timestamp","msg","data","gas","sender","value","gas price","origin","revert","require","keccak256","ripemd160","sha256","ecrecover","addmod","mulmod","cryptography","this","super","selfdestruct","balance","codehash","send"],
                      "globalVariables":['abi.decode(bytes memory encodedData, (...)) returns (...)', 'abi.encode(...) returns (bytes memory)', 'abi.encodePacked(...) returns (bytes memory)',  'abi.encodeWithSelector(bytes4 selector, ...) returns (bytes memory)', 'abi.encodeCall(function functionPointer, (...)) returns (bytes memory)','abi.encodeWithSelector(functionPointer.selector, (...))', 'abi.encodeWithSignature(string memory signature, ...) returns (bytes memory)', 'to abi.encodeWithSelector(bytes4(keccak256(bytes(signature)), ...)', 'bytes.concat(...) returns (bytes memory)', 'arguments to one byte array<bytes-concat>`', 'string.concat(...) returns (string memory)', 'arguments to one string array<string-concat>`', 'block.basefee (uint)', 'block.chainid (uint)', 'block.coinbase (address payable)', 'block.difficulty (uint)', 'block.gaslimit (uint)', 'block.number (uint)', 'block.timestamp (uint)', 'gasleft() returns (uint256)', 'msg.data (bytes)', 'msg.sender (address)', 'msg.sig (bytes4)', 'msg.value (uint)', 'tx.gasprice (uint)', 'tx.origin (address)', 'assert(bool condition)', 'require(bool condition)', 'for malformed input or error in external component)', 'require(bool condition, string memory message)', 'condition is false (use for malformed input or error in external component). Also provide error message.', 'revert()', 'revert(string memory message)', 'blockhash(uint blockNumber) returns (bytes32)', 'keccak256(bytes memory) returns (bytes32)', 'sha256(bytes memory) returns (bytes32)', 'ripemd160(bytes memory) returns (bytes20)', 'ecrecover(bytes32 hash, uint8 v, bytes32 r, bytes32 s) returns (address)', 'the public key from elliptic curve signature, return zero on error', 'addmod(uint x, uint y, uint k) returns (uint)', 'arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', 'mulmod(uint x, uint y, uint k) returns (uint)', 'with arbitrary precision and does not wrap around at 2**256. Assert that k != 0 starting from version 0.5.0.', "this (current contract's type)", 'super', 'selfdestruct(address payable recipient)', '<address>.balance (uint256)', '<address>.code (bytes memory)', '<address>.codehash (bytes32)', '<address payable>.send(uint256 amount) returns (bool)', 'returns false on failure', '<address payable>.transfer(uint256 amount)', 'type(C).name (string)', 'type(C).creationCode (bytes memory)', 'type(C).runtimeCode (bytes memory)', 'type(I).interfaceId (bytes4)', 'type(T).min (T)', 'type(T).max (T)'],"sectionHeader":['contract','library','interface','abstract contract'],"allVars":['contract','library','pragma solidity','import','interface','abstract contract','constructor','function','modify','SPDX-License-Identifier']})
def makeABI(x):
    lines = par.parseIt(x)
    for i in range(0,len(lines)):
        for c in range(0,len(lines[i])):
            curr = lines[i][c]
            input(curr)
makeABI('/home/bigrugz/Desktop/finalParser/NeFiFeeManager.sol')