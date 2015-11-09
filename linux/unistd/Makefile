CC=gcc
CFLAGS=-Wall -I.

all: test

main.o: main.c
	$(CC) -c $< $(CFLAGS)

chdir.o: chdir.c chdir.h
	$(CC) -c $< $(CFLAGS)

main: main.o chdir.o
	$(CC) -o $@ main.o chdir.o $(CFLAGS)

test: main
	./main 2>testmsg

clean:
	rm -f main *~ *.o testmsg

