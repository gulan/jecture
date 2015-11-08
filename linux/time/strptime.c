#define _XOPEN_SOURCE
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void
strptime_test (void) {
  struct tm tm;

  memset(&tm, 0, sizeof(struct tm));
  strptime("2015-11-08 07:42:31", "%Y-%m-%d %H:%M:%S", &tm);
  assert (tm.tm_sec == 31);
  assert (tm.tm_min == 42);
  assert (tm.tm_hour == 7);
  assert (tm.tm_mday == 8);
  assert (tm.tm_mon == 10);    // Jan is 0
  assert (tm.tm_year == 115);
  assert (tm.tm_wday == 0);    // Sunday is 0
  assert (tm.tm_yday == 311);  // shell: 1 less than `date +%j`
  assert (tm.tm_isdst == 0);
  puts("strptime ok");
}

/*
int
main(void) {
  strptime_test();
  exit(EXIT_SUCCESS);
}
*/

