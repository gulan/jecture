#include "chdir.h"
#include <assert.h>
#include <stdlib.h>

int
main (void) {
  assert (chdir_test());
  assert (chdir_test_shortbuf());
  exit(EXIT_SUCCESS);
}
