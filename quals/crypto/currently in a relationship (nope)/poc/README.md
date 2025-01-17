# currently in a relationship (nope) POC

## Main Phase

1. flag1.enc is the PNG flag encrypted normally with RSA, but flag2.enc is the result of a modification through a simple linear equation.
2. Knowing this, we can determine that this scheme is vulnerable to the Franklin-Reiter related message attack for RSA cryptosystems.
3. Reconstruct the attack with sage (preferably) and adjust according to the challenge, ex: block_size = 192, decrypted_message.zfill(382) since this is a PNG file.
4. If the solver was created successfully, we now have access to flag.png, which is the second phase of this challenge.

## Secondary Phase

1. Simple enough, notice that the password length is either 16 / 24 / 32 which means we can use any designated wordlist in a pretty fast manner to find the used password.
2. Either small_rockyou or rockyou could work with this, and then we just brute-force every valid password which if the solver was created successfully, would find that the correct password is "withintempation" and should run very fast (takes like 1 sec on my machine). Afterwards just decrypt as normal and the flag will be found.

```
ARA6{fr4nkl1n_r3173r_70_r0cky0u_qu35710n_m4rk_0n_my_cryp706r4phy_ch4ll3n63_qu35710n_m4rk}
```