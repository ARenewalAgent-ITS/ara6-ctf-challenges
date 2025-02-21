#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int choice;

void setup()
{
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

int get_num()
{
    char buf[0x10];
    fgets(buf, 0x10, stdin);
    return atoi(buf);
}

void print_menu()
{
    // * add, view, delete, exit
    puts("1. 📝");
    puts("2. 🔍");
    puts("3. 🗑️");
    puts("4. 🚪");
}

void add_note(void **ptr)
{
    char buf[0x10];
    puts("Ely is here to help you write your plans for today! (✿◕‿◕)♡");
    printf(">> ");

    if (read(0, ptr, 0x30) <= 0)
    {
        puts("Oh no! Something went wrong! (╥﹏╥)");
        _exit(1);
    }

    ptr[3] = strdup((char *)ptr);
    if (!ptr[3])
    {
        puts("Oh no! Something went wrong! (╥﹏╥)");
        _exit(1);
    }

    puts("Anything else you want to add? (´｡• ◡ •｡`) ♡");
    fgets(buf, 0x10, stdin);
    if (strcmp(buf, "yes") == 0)
    {
        puts("Oh! Okay! Ely is here to help you! (✿◕‿◕)♡");
        printf(">> ");
        if (read(0, ptr[3], 0x30) <= 0)
        {
            puts("Oh no! Something went wrong! (╥﹏╥)");
            _exit(1);
        }
    }

    puts("Yay! Your note has been saved with Elysia's love! (♡˙︶˙♡)");
    return;
}

void view_note(char *note)
{
    if (!note || !*note)
    {
        puts("Ely can't find any notes to view! (｡•́︿•̀｡)");
        return;
    }

    printf("Ely found your note! (´｡• ◡ •｡`) ♡\n%s\n", note);
    return;
}

void delete_note(char **note)
{
    if (!note || !*note)
    {
        puts("Ely can't find any notes to delete! (｡•́︿•̀｡)");
        return;
    }

    free(*note);
    *note = NULL;
    puts("Ah? Any other plans with Ely today? (´｡• ◡ •｡`) ♡");
}

void solve()
{
    char *v6 = NULL;
    void *ptr[3];

    while (1)
    {
        print_menu();
        printf(">> ");
        choice = get_num();
        switch (choice)
        {
        case 1:
            add_note(ptr);
            break;
        case 2:
            view_note(v6);
            break;
        case 3:
            delete_note(&v6);
            break;
        case 4:
            puts("You're leaving Ely today? (´｡• ◡ •｡`) ♡");
            printf(">> ");
            getchar();
            read(0, ptr, 0x30);
            if (strcmp((char *)ptr, "yes") == 0)
            {
                puts("Bye bye! Do know that Ely loves you so much! (๑>◡<๑)♡");
                return 0;
            }
            break;
        default:
            puts("Eehh? What are you trying to do?! ( > ⤙ < )♡\n");
            break;
        }
    }
}

int main()
{
    setup();
    puts("Elysia's note taking app (˶˃ ᵕ ˂˶)♡");
    solve();
    return 0;
}
