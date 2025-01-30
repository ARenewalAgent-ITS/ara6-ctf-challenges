# Solution
1. Analyze the whole program 

> There will be some incomplete functions and errors on the program. You could see the main flow of the whole program is just to bypass a password check to get a key for another function's condition in revealing the flag 
>
> FUNCTIONS FUNCTIONALITIES: 
> 1. rotate_or_shift: shifting characters in a string by {key} much
> 2. group_rotate_or_shift: calling rotate_or_shift functions for shifting multiple strings at once
> 3. password_check: literally for checking password with simple if conditions
> 4. summation: to generate a passkey for pass_check function
> 5. pass_check: to generate potential flags according to the passkey inputted



2. Fix the program

> The main issue with the program is that the pass_check function doesn't work. You can easily fix this function by adding the proper name for key variables (e.g. a --> key_a) and then alter the program just the way you want it to be as long as it gives the proper flag at the end. (check solve.cpp for my version)

3. Run the program

> For easier time in tracing back the code steps, just use the given program functions to solve it. If you want you could just try it one by one using brute force to get the proper answer from the obfuscation. But, it's easier to edit the program by changing little things here and there and the run the program to get the flag.

**Check my solution at [solve.cpp](./solve.cpp) to see how I did it**
