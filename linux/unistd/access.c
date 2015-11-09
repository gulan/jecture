#include <assert.h>
#include <errno.h>
#include <stdio.h>
#include <unistd.h>

/* Access should not be used as it invites race conditions. There is
no danger in running these tests, though.*/

int
access_test(void) {
  assert (access("/etc/hosts", F_OK) == 0);
  assert (access("/etc/hosts", R_OK) == 0);
  assert (access("/etc/hosts", W_OK) == -1);
  assert (errno == 13);
  errno = 0;
  assert (access("/etc/hosts", X_OK) == -1);
  assert (errno == 13);
  puts("access_test ok");
  return 1;
}

/*
int
main (void) {
  access_test();
  exit(EXIT_SUCCESS);
}
*/
