CFLAGS=-Wall -std=c99

all: test

test: main
	rm -f tfile*
	./main | python -mjson.tool >results

clean:
	rm -f main tfile* results

