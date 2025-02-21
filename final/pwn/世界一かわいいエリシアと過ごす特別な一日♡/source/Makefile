CC = gcc
CFLAGS = -Wl,-z,relro,-z,now -O0
SRC = chall.c
OUT = chall

all:
	$(CC) $(CFLAGS) $(SRC) -o $(OUT)

clean:
	rm -f $(OUT)
