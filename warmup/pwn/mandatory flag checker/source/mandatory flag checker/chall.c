#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void ara6_logo()
{
	printf("       d8888 8888888b.         d8888       .d8888b.       .d8888b.        .d8888b. 88888888888 8888888888 \n      d88888 888   Y88b       d88888      d88P  Y88b     d88P  Y88b      d88P  Y88b    888     888        \n     d88P888 888    888      d88P888      888            888    888      888    888    888     888        \n    d88P 888 888   d88P     d88P 888      888d888b.      888    888      888           888     8888888    \n   d88P  888 8888888P\"     d88P  888      888P \"Y88b     888    888      888           888     888        \n  d88P   888 888 T88b     d88P   888      888    888     888    888      888    888    888     888        \n d8888888888 888  T88b   d8888888888      Y88b  d88P d8b Y88b  d88P      Y88b  d88P    888     888        \nd88P     888 888   T88b d88P     888       \"Y8888P\"  Y8P  \"Y8888P\"        \"Y8888P\"     888     888        \n\n");
}

void print_flag() 
{
	FILE *f;
	char flag[128];

	if (!(f = fopen("flag.txt","r"))) sprintf(flag, "ARA6{ERR_FLAG_NOT_FOUND}");
	else fscanf(f,"%s",flag);

	printf("[+] Correct! %s\n", flag);
}

void pwnme() 
{
	int number = 0;
	char flag[32];

	ara6_logo();

	printf("[+] Welcome to ARA 6.0 CTF!\n");
	printf("[+] Insert flag here: ");
	scanf("%s",flag);

	printf("[%] Processing flag...\n");
	sleep(5);

	if (number == 1337) print_flag();
	else printf("[!] Wrong flag!\n");

	exit(0);
}

void main() 
{
	setbuf(stdout,0);
	pwnme();
}
