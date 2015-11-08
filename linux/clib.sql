
create table desc (
    desc_id integer primary key,
    name text not null,
    dtext text not null);

create table intro (
    desc_id references desc,
    tag text not null);

insert into desc values (0,"assert","Contains the assert macro, used to assist with detecting logical errors and other types of bug in debugging versions of a program.");
insert into desc values (1,"complex","A set of functions for manipulating complex numbers.");
insert into desc values (2,"ctype","Defines set of functions used to classify characters by their types or to convert between upper and lower case in a way that is independent of the used character set (typically ASCII or one of its extensions, although implementations utilizing EBCDIC are also known).");
insert into desc values (3,"errno","For testing error codes reported by library functions.");
insert into desc values (4,"fenv","Defines a set of functions for controlling floating-point environment.");
insert into desc values (5,"float","Defines macro constants specifying the implementation-specific properties of the floating-point library.");
insert into desc values (6,"inttypes","Defines exact width integer types.");
insert into desc values (7,"iso646","Defines several macros that implement alternative ways to express several standard tokens. For programming in ISO 646 variant character sets.");
insert into desc values (8,"limits","Defines macro constants specifying the implementation-specific properties of the integer types.");
insert into desc values (9,"locale","Defines localization functions.");
insert into desc values (10,"math","Defines common mathematical functions.");
insert into desc values (11,"setjmp","Declares the macros setjmp and longjmp, which are used for non-local exits.");
insert into desc values (12,"signal","Defines signal handling functions.");
insert into desc values (13,"stdalign","For querying and specifying the alignment of objects.");
insert into desc values (14,"stdarg","For accessing a varying number of arguments passed to functions.");
insert into desc values (15,"stdatomic","For atomic operations on data shared between threads.");
insert into desc values (16,"stdbool","Defines a boolean data type.");
insert into desc values (17,"stddef","Defines several useful types and macros.");
insert into desc values (18,"stdint","Defines exact width integer types.");
insert into desc values (19,"stdio","Defines core input and output functions");
insert into desc values (20,"stdlib","Defines numeric conversion functions, pseudo-random numbers generation functions, memory allocation, process control functions");
insert into desc values (21,"stdnoreturn","For specifying non-returning functions.");
insert into desc values (22,"string","Defines string handling functions.");
insert into desc values (23,"tgmath","Defines type-generic mathematical functions.");
insert into desc values (24,"threads","Defines functions for managing multiple Threads as well as mutexes and condition variables.");
insert into desc values (25,"time","Defines date and time handling functions");
insert into desc values (26,"uchar","Types and functions for manipulating Unicode characters.");
insert into desc values (27,"wchar","Defines wide string handling functions.");
insert into desc values (28,"wctype","Defines set of functions used to classify wide characters by their types or to convert between upper and lower case");
insert into intro values (1,"C99");
insert into intro values (4,"C99");
insert into intro values (6,"C99");
insert into intro values (7,"NA1");
insert into intro values (13,"C11");
insert into intro values (15,"C11");
insert into intro values (16,"C99");
insert into intro values (18,"C99");
insert into intro values (21,"C11");
insert into intro values (23,"C99");
insert into intro values (24,"C11");
insert into intro values (26,"C11");
insert into intro values (27,"NA1");
insert into intro values (28,"NA1");
