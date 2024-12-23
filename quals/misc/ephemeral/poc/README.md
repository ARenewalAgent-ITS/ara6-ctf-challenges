# ephemeral POC

1. Initial connection setup
```sh
python3 pow.py # copy the result
nc server port
```
2. Get the challenge address
3. `forge init`
4. Put `Helper.sol` at `src/`
5. `forge build`
6. Inspect and copy the bytecode of `Helper` contract by `cat out/Helper.sol/Helper.json` (use the `bytecode.object` value)
7. Deploy `Helper` contract and copy the newly deployed contract address
```sh
cast send --chain 39438141 --private-key 0x... --rpc-url http://... --create BYTECODE
```
8. send `getOwnership`
```sh
cast send --chain 39438141 --private-key 0x... --rpc-url http://... CHAL_ADDR "getOwnership(address)" HELPER_ADDR
```
9. Use verifiyer to get flag
```sh
ARA6{sh0u7_out_70_3ph3me24l_prov1d3r5}
```
