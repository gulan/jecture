CC=gcc
CFLAGS=-Wall -I.

all: test

main.o: main.c
	$(CC) -c $< $(CFLAGS)

strftime.o: strftime.c strftime.h
	$(CC) -c $< $(CFLAGS)

strptime.o: strptime.c strptime.h
	$(CC) -c $< $(CFLAGS)

main: main.o strftime.o strptime.o
	$(CC) -o $@ main.o strftime.o strptime.o $(CFLAGS)

test: main
	./main 2>testmsg

clean:
	rm -f main *~ *.o testmsg

