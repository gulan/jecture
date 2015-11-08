#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

int
sscanf_t01 (void) {
  int rc;
  int a,b,c,d;
  long int e;
  
  rc = sscanf("-123", "%d", &a);
  assert(rc == 1);
  assert(a == -123);

  rc = sscanf("321", "%d", &a);
  assert(rc == 1);
  assert(a == 321);

  // max positive int: 2**31 - 1
  rc = sscanf("2147483647", "%d", &a);
  assert(rc == 1);
  assert(a == 2147483647);

  // max positive int + 1 is negative
  rc = sscanf("2147483648", "%d", &a);
  assert(rc == 1);
  assert(a == -2147483648);

  // max positive int + 2 is moving towards 0
  rc = sscanf("2147483649", "%d", &a);
  assert(rc == 1);
  assert(a == -2147483647);
 
  // not neg if long
  rc = sscanf("2147483648", "%ld", &e);
  assert(rc == 1);
  assert(e == 2147483648);
 
  // 3 fields
  rc = sscanf("0 1 2", "%d%d%d", &a, &b, &c);
  assert(rc == 3);
  assert(a == 0);
  assert(b == 1);
  assert(c == 2);

  // limit field length
  rc = sscanf("  12345678 999", "%3d%3d%d%d", &a, &b, &c, &d);
  assert(rc == 4);
  assert(a == 123);
  assert(b == 456);
  assert(c == 78);
  assert(d == 999);

  // match hex int
  rc = sscanf("abc", "%x", &a);
  assert(rc == 1);
  assert(a == 2748);

  return 0;
}

int
sscanf_t02 (void) {
  // int i;
  int rc;
  // int N = 7;
  char a,b,c;
  char *pa;

  rc = sscanf("abc", "%c", &a);
  assert(rc == 1);
  assert(a == 'a');
  
  // match 3 characters
  rc = sscanf("abcdef", "%c%c%c", &a, &b, &c);
  assert(rc == 3);
  assert(a == 'a');
  assert(b == 'b');
  assert(c == 'c');

  // * to suppress assignment
  b = 'X';
  rc = sscanf("def", "%c%*c%c", &a, &c);
  assert(rc == 2);
  assert(a == 'd');
  assert(b == 'X');
  assert(c == 'f');

  // * match literal Z
  a = 'X';
  c = 'X';
  rc = sscanf("dZf", "%cZ%c", &a, &c);
  assert(rc == 2);
  assert(a == 'd');
  assert(c == 'f');

  // * match whitespace
  a = 'X';
  c = 'X';
  rc = sscanf("d     f", "%c %c", &a, &c);
  assert(rc == 2);
  assert(a == 'd');
  assert(c == 'f');

  // let sscan allocate
  rc = sscanf("123456", "%mc", &pa);
  assert(rc == 1);
  assert(*pa == '1');
  free((void *)pa);
  return 0;
}

int
sscanf_main () {
  sscanf_t01();
  sscanf_t02();
  printf("sscanf ok\n");
  return 0;
}


// gcc main.c ; ./a.out
