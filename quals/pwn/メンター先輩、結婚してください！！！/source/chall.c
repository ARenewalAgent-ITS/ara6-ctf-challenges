#include <linux/seccomp.h>
#include <sys/prctl.h>
#include <sys/syscall.h>
#include <seccomp.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/mman.h>
#include <string.h>

void setup()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

char uwu[] = "\x48\x31\xc0\x48\x31\xdb\x48\x31\xc9\x48\x31\xd2\x48\x31\xf6\x48\x31\xff"
            "\x48\x31\xed\x48\x31\xe4\x4d\x31\xc0\x4d\x31\xc9\x4d\x31\xd2\x4d\x31\xdb"
            "\x4d\x31\xe4\x4d\x31\xed\x4d\x31\xf6\x4d\x31\xff";

void seccomp_setup()
{
    for (int i = 0; i < 1000; i++)
    {
        close(i);
    }

    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(preadv2), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(getdents), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(socket), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(connect), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(sendto), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
    seccomp_load(ctx);
    seccomp_release(ctx);
}

void solve()
{
    setup();
    puts("Yet another sandbox challenge...");
    fflush(stdout);
    char *buf = mmap(0, 0x100, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    memcpy(buf, uwu, sizeof(uwu) - 1);
    read(0, buf + 48, 0x100);
    seccomp_setup();
    ((void (*)())buf)();
}

int main(int argc, char const *argv[])
{
    int t = 1;
    while (t--)
    {
        solve();
    }

    _exit(0);
}
