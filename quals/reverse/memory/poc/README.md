# memory POC

POC updated to `memory-v2` binary.

1. Terdapat binary Rust. Pertama, temukan fungsi dalam scope `memory` bernama `main`
![image](https://github.com/user-attachments/assets/33d04b63-d27c-4f95-bf8d-25d699e8561b)

2. Saat kita graphing fungsi `main`, terdapat 1 loop dengan 1 nested-loop
![image](https://github.com/user-attachments/assets/5d6943c6-031f-425d-8f25-f82958ff3733)

3. Siapkan scaffolding dari flow programnya
![image](https://github.com/user-attachments/assets/57d5941b-a258-4e93-8a01-0d768cfeb964)

4. Pada Rust binary decompilation di Ghidra, berikut beberapa perbedaan essensial dengan source codenya:
<table>
  <tr>
    <td>Decompilation</td>
    <td>Source Code</td>
  </tr>
  <tr>
  <td>

![image](https://github.com/user-attachments/assets/fe4816d8-363c-4dc8-9fe5-31e6f9a945bc)

  </td>
  <td>

```rust
println!("Hello...");
```

  </td>
  </tr>
  <tr>
  <td>

![image](https://github.com/user-attachments/assets/42207ae6-a601-499b-a248-d9f0e57af65e)
    
  </td>
  <td>

```rust
let mut input = String::new();
```
    
  </td>
  </tr>
</table>

5. Berikut transpilasi dari C++ pseudocode menjadi Python
<table>
  <tr>
    <td>Pseudocode</td>
    <td>Python</td>
  </tr>
  <tr>
  <td>

```c++
std::io::stdio::stdin();
std::io::stdio::Stdin::read_line();
core::ptr::drop_in_place<>(&local_90);
alloc::string::String::pop(&local_e0);
```
      
  </td>
  <td>

```python
local_90 = input()[:-1]
```
    
  </td>
  </tr>
  <tr>
  <td>

```c++
&Var6 = alloc::string::deref(&local_e0);
pat.length = 4;
pat.data_ptr = &DAT_0014b310;
bVar1 = core::str::starts_with<&str>(&Var6,pat);
```
      
  </td>
  <td>

```python
pat = "ARA6"
# Pelajari sistem ownership Rust untuk tahu kenapa `local_90` bukan `local_e0`
# dan karena ini Python, kita pakainya `local_90`
bVar1 = local_90.startswith(pat)
```
    
  </td>
  </tr>
  <tr>
  <td>

```c++
if (((bVar1 ^ 0xffU) & 1) == 0) {
  &Var6 = alloc::string::deref(&local_e0);
  local_70 = (Iter<u8>)core::str::chars(&Var6);
  local_74 = core::iter::traits::iterator::Iterator::nth<>((Chars *)&local_70,4);
  bVar1 = core::option::eq<char>(&local_74,(Option<char> *)&DAT_0014b314);
```
      
  </td>
  <td>

```python
if bVar:
  bVar1 = local_90[4] == '}'
```
    
  </td>
  </tr>
  <tr>
  <td>

```c++
if (((bVar1 ^ 0xffU) & 1) == 0) {
  local_5c = 5;
  local_56 = 0;
  bVar5 = local_56;
  do {
    local_56 = bVar5;
    local_55 = 0;

    // ...

    bVar5 = local_56 + 1;
    if (0xfe < local_56) {
                /* WARNING: Subroutine does not return */
      core::panicking::panic_const::panic_const_add_overflow();
    }
  } while( true );
}
```
      
  </td>
  <td>

```python
if bVar1:
  local_5c = 5
  local_56 = 0
  while True:
    local_55 = 0
    # ...
    local_56 += 1

    # nested-labelled-loop in Rust
    if breakToEnd:
      break
```
    
  </td>
  </tr>
  <tr>
  <td>

```c++
while (true) {
  if (CARRY1(local_56,local_55) != false) {
            /* WARNING: Subroutine does not return */
    core::panicking::panic_const::panic_const_add_overflow();
  }
  bVar5 = (byte)(local_56 + local_55) % 0x1a;
  OVar2._0_1_ = bVar5 + 0x40;
  if (0xbf < bVar5) {
            /* WARNING: Subroutine does not return */
    core::panicking::panic_const::panic_const_add_overflow();
  }
  OVar2._1_3_ = 0;
  local_25 = OVar2._0_1_;
  local_24 = OVar2;
  &Var6 = alloc::string::deref(&local_e0);
  IVar7 = (Iter<u8>)core::str::chars(&Var6);
  local_50 = IVar7;
  local_54 = core::iter::traits::iterator::Iterator::nth<>
                        ((Chars *)&local_50,(ulong)local_5c);
  local_40 = OVar2;
  bVar1 = core::cmp::PartialEq::ne<>(&local_54,&local_40);
  if (bVar1) {
    no();
    goto LAB_00109655;
  }
  bVar5 = local_55 + 1;
  if (0xfe < local_55) {
            /* WARNING: Subroutine does not return */
    core::panicking::panic_const::panic_const_add_overflow();
  }
  uVar3 = local_5c + 1;
  local_55 = bVar5;
  if (0xfffffffe < local_5c) {
            /* WARNING: Subroutine does not return */
    core::panicking::panic_const::panic_const_add_overflow();
  }
  local_5c = uVar3;
  if (bVar5 == 0xf) break;
  if (local_56 == 4) {
    // ..
  }
}

LAB_00109655:
  core::ptr::drop_in_place<>(&local_e0);
  return;
```
      
  </td>
  <td>

```python
while True:
  bVar5 = (local_56 + local_55) % 0x1a
  bVar5 += 0x40
  # atau:
  # bVar5 -= 1
  # bVar5 += ord('A')
  
  if ord(local_90[local_5c]) != bVar5:
    no()
    break
  
  # bukan bVar5 kecuali jika bVar5 = local_55 + 1
  local_5c += 1
  local_55 += 1

  if local_55 == 15:
    break
  if local_56 == 4:
    breakToEnd = True
    break
```
    
  </td>
  </tr>
  <tr>
  <td>

```c++
local_3c[0] = alloc::string::String::pop(&local_e0);
bVar1 = core::option::eq<char>(local_3c,(Option<char> *)&DAT_0014b318);
if (((bVar1 ^ 0xffU) & 1) == 0) {
  uVar4 = alloc::string::String::len(&local_e0);
  if (0xfffffffffffffffe < uVar4) {
        /* WARNING: Subroutine does not return */
    core::panicking::panic_const::panic_const_add_overflow();
  }
  if (uVar4 == 0x42) {
    yes();
    core::ptr::drop_in_place<>(&local_e0);
    return;
  }
  no();
}
else {
  no();
}
goto LAB_00109655;
```
      
  </td>
  <td>

```python
ender = local_90.pop()
if ender == '}':
  if len(local_90) == 66:
    yes()
    exit()
  else:
    no()
else:
  no()
```
    
  </td>
  </tr>
</table>

```python
# Pelengkap
def yes():
  print("Nice")
  exit()

def no():
  print("No")
  exit()

######################################################################################
local_90 = input()[:-1]

pat = "ARA6"
# Pelajari sistem ownership Rust untuk tahu kenapa `local_90` bukan `local_e0`
# dan karena ini Python, kita pakainya `local_90`
bVar1 = local_90.startswith(pat)

if bVar:
  bVar1 = local_90[4] == '}'

if bVar1:
  local_5c = 5
  local_56 = 0
  while True:
    local_55 = 0
    
    while True:
      bVar5 = (local_56 + local_55) % 0x1a
      bVar5 += 0x40
      # atau:
      # bVar5 -= 1
      # bVar5 += ord('A')
      
      if ord(local_90[local_5c]) != bVar5:
        no()
        break
      
      # bukan bVar5 kecuali jika bVar5 = local_55 + 1
      local_5c += 1
      local_55 += 1

      if local_55 == 15:
        break
      if local_56 == 4:
        breakToEnd = True
        break

    local_56 += 1

    # nested-labelled-loop in Rust
    if breakToEnd:
      break

ender = local_90.pop()
if ender == '}':
  if len(local_90) == 66:
    yes()
  else:
    no()
else:
  no()
```

6. Solver
```python
flag = "ARA6{"

i = 0
brekall = False
while not brekall:
  j = 0
  while True:
    builder = 0x40 + ((i + j) % 0x1a)
    flag += chr(builder)
    j += 1
    if j == 15:
      break
    if i == 4:
      brekall = True
      break
  i += 1

flag += '}'
print(flag)
```

Flag: `ARA6{@ABCDEFGHIJKLMNABCDEFGHIJKLMNOBCDEFGHIJKLMNOPCDEFGHIJKLMNOPQD}`
