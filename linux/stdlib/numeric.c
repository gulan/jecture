#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
main (int argc, char *argv[]) {

  // int atoi(const char *nptr);
  assert (atoi("0") == 0);
  assert (atoi("1") == 1);
  assert (atoi("123") == 123);
  assert (atoi("123 456") == 123);
  assert (atoi("-1") == -1);
  assert (atoi("-0") == 0);

  // long atol(const char *nptr);
  // long long atoll(const char *nptr);
  // long long atoq(const char *nptr);
  printf("numeric ok\n");
  return 0;
}
