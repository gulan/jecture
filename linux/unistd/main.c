#include "access.h"
#include "chdir.h"
#include <assert.h>
#include <stdlib.h>

int
main (void) {
  assert (chdir_test());
  assert (chdir_test_shortbuf());
  assert (access_test());
  exit(EXIT_SUCCESS);
}
