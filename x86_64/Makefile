start-exit : start-exit.o
	ld -o $@ $<

start-exit.o : start-exit.asm
	nasm -f elf64 -l start-exit.listing -gdwarf $<

test : start-exit
	./tests.sh

clean :
	rm -f start-exit *.o *.listing

