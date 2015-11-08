CC=gcc
CFLAGS=-Wall -I.

all: test

main.o: main.c
	$(CC) -c $< $(CFLAGS)

sscanf.o: sscanf.c sscanf.h
	$(CC) -c $< $(CFLAGS)

fopen.o: fopen.c fopen.h
	$(CC) -c $< $(CFLAGS)

stdio: main.o fopen.o sscanf.o
	$(CC) -o $@ main.o fopen.o sscanf.o $(CFLAGS)

test: stdio
	./stdio 2>testmsg

clean:
	rm -f stdio *~ *.o t01 testmsg

