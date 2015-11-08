#include <assert.h>
#include <stdio.h>

void
succeed(void) {
  assert(1);
  assert('a');
  assert("hello");
  assert(1.0);
}

void
fail(void) {
  // any of
  assert(0);
  assert(0.0);
}

int
main () {
  succeed();
  // fail();
  printf("ok\n");
  return 0;
}
