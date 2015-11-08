CC=gcc
CFLAGS=-Wall -I.

all: test

main.o: main.c
	$(CC) -c $< $(CFLAGS)

sysstat: main.o
	$(CC) -o $@ main.o $(CFLAGS)

test: sysstat
	./sysstat sysstat | python -mjson.tool >result.json

clean:
	rm -f sysstat *~ *.o result.json

