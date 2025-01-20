#include <stdio.h>
#include <string.h>

struct {
	char bcd[4];
	int num;
	int num1;
	char hi;
} child = {{'h', 'i', 'm', 'o'}, 0x21796d, 0x6d7921};

// ARA6{51x_t3n}

int main(int argc, char** argv) {
	if (strlen(argv[1]) != 13) return 1;
	if (argv[1][12] != '}') return 1;

	char *final = &child;
	for (int i = 0; i < 13; i++) {
		final[i] ^= argv[1][i];
	}
	final[13] = 0;
	printf("%s", final);
	return 0;
}
