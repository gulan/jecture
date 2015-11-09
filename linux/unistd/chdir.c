#include "../dbg.h"
#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/* cd to /tmp and return */
int
chdir_test(void) {
  char saved_path[PATH_MAX];
  char current_path[PATH_MAX];
  
  check (getcwd(saved_path, PATH_MAX), "getcwd");

  check (chdir("/tmp") == 0, "chdir(/tmp)");
  check (getcwd(current_path, PATH_MAX), "getcwd");

  check (chdir(saved_path) == 0, "chdir()");
  check (getcwd(current_path, PATH_MAX), "getcwd");
  
  puts("chdir_test ok");
  return 1;
 error:
  return 0;
}

/* Try to stuff fullpath into a short buffer: FAIL */
int
chdir_test_shortbuf(void) {
  char saved_path[PATH_MAX];
  
  check (getcwd(saved_path, 2), "*** Failure Expected ***");
  return 0;

 error:
  puts("chdir_test_shortbuf ok");
  return 1;
}


/* int */
/* main (void) { */
/*   assert (chdir_test()); */
/*   assert (chdir_test_shortbuf()); */
/*   exit(EXIT_SUCCESS); */
/* } */
