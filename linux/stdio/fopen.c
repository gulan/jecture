#include <assert.h>
#include <stdio.h>

int
fopen_t01 (void) {
  FILE *f;

  // printf("t01 - open for write\n");
  f = fopen("t01", "w");
  if (f == NULL) {
    perror("fopen");
    return 0;
  }
  fclose(f);
  return 1;
}

int
fopen_t02 (void) {
  FILE *f;

  // printf("t02 - (bad) open for write\n");
  f = fopen("t0/2", "w");
  if (f == NULL) {
    perror("fopen");
    return 1;
  }
  fclose(f);
  return 0;
}

int
fopen_main () {
  assert(fopen_t01());
  assert(fopen_t02());
  printf("fopen ok\n");
  return 0;
}
