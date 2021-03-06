#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

long int NOW = 1446565017;

time_t
now() {
  time_t t;
  t = time(NULL);
  return t;
}

void
strftime_test (void) {
  struct tm *ltime;
  char outstr[200];

  ltime = localtime((time_t *)&NOW);
  if (ltime == NULL) {
    perror("localtime");
    exit(EXIT_FAILURE);
  }
  
  // Abbreviated weekday
  if (strftime(outstr, sizeof(outstr), "%a", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr,"Tue") == 0);

  // Full weekday
  if (strftime(outstr, sizeof(outstr), "%A", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr,"Tuesday") == 0);

  // Abbreviated month
  if (strftime(outstr, sizeof(outstr), "%b", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr,"Nov") == 0);

  // Full month
  if (strftime(outstr, sizeof(outstr), "%B", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr,"November") == 0);

  // locale date and time
  if (strftime(outstr, sizeof(outstr), "%c", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr,"Tue Nov  3 07:36:57 2015") == 0);

  // century digits (20, not 21)
  if (strftime(outstr, sizeof(outstr), "%C", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr,"20") == 0);

  // day of month
  if (strftime(outstr, sizeof(outstr), "%d", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr,"03") == 0);

  // American date format
  if (strftime(outstr, sizeof(outstr), "%D", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr,"11/03/15") == 0);

  // month with leading space instead of zero
  if (strftime(outstr, sizeof(outstr), "%e", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr," 3") == 0);

  // month with leading space instead of zero
  if (strftime(outstr, sizeof(outstr), "%e", ltime) == 0) {
    fprintf(stderr, "strftime returned 0");
    exit(EXIT_FAILURE);
  }
  assert (strcmp(outstr," 3") == 0);
  
  // %H     The hour as a decimal number using a 24-hour clock (range 00 to 23).
  strftime(outstr, sizeof(outstr), "%H", ltime);
  assert (strcmp(outstr,"07") == 0);

  //  %I     The hour as a decimal number using a 12-hour clock (range 01 to 12).
  strftime(outstr, sizeof(outstr), "%I", ltime);
  assert (strcmp(outstr,"07") == 0);

  //  %j     The day of the year as a decimal number (range 001 to 366).
  strftime(outstr, sizeof(outstr), "%j", ltime);
  assert (strcmp(outstr,"307") == 0);

  //  %k The hour (24-hour clock) as a decimal number (range 0 to 23);
  //  %single digits are preceded by a blank.  (See also %H.)  (TZ)
  strftime(outstr, sizeof(outstr), "%k", ltime);
  assert (strcmp(outstr," 7") == 0);

  //  %l The hour (12-hour clock) as a decimal number (range 1 to 12);
  //  %single digits are preceded by a blank.  (See also %I.)  (TZ)
  strftime(outstr, sizeof(outstr), "%l", ltime);
  assert (strcmp(outstr," 7") == 0);

  //  %m     The month as a decimal number (range 01 to 12).
  strftime(outstr, sizeof(outstr), "%m", ltime);
  assert (strcmp(outstr,"11") == 0);

  //  %M     The minute as a decimal number (range 00 to 59).
  strftime(outstr, sizeof(outstr), "%M", ltime);
  assert (strcmp(outstr,"36") == 0);

  //  %n     A newline character. (SU)
  strftime(outstr, sizeof(outstr), "%n", ltime);
  assert (strcmp(outstr,"\n") == 0);

  //  %p Either "AM" or "PM" according to the given time value, or the
  //  %corresponding strings for the current locale.  Noon is treated
  //  %as "PM" and midnight as "AM".
  strftime(outstr, sizeof(outstr), "%p", ltime);
  assert (strcmp(outstr,"AM") == 0);

  //  %P Like %p but in lowercase: "am" or "pm" or a corresponding
  //  %string for the current locale. (GNU)
  strftime(outstr, sizeof(outstr), "%P", ltime);
  assert (strcmp(outstr,"am") == 0);

  //  %r The time in a.m. or p.m. notation.  In the POSIX locale this
  //  %is equivalent to %I:%M:%S %p.  (SU)
  strftime(outstr, sizeof(outstr), "%r", ltime);
  assert (strcmp(outstr,"07:36:57 AM") == 0);

  //  %R The time in 24-hour notation (%H:%M).  (SU) For a version
  //  %including the seconds, see %T below.
  strftime(outstr, sizeof(outstr), "%R", ltime);
  assert (strcmp(outstr,"07:36") == 0);

  //  %s The number of seconds since the Epoch, 1970-01-01 00:00:00
  //  %+0000 (UTC). (TZ)
  strftime(outstr, sizeof(outstr), "%s", ltime);
  assert (strcmp(outstr,"1446565017") == 0);

  //  %S The second as a decimal number (range 00 to 60).  (The range
  //  %is up to 60 to allow for occasional leap seconds.)
  strftime(outstr, sizeof(outstr), "%S", ltime);
  assert (strcmp(outstr,"57") == 0);

  //  %t A tab character. (SU)
  strftime(outstr, sizeof(outstr), "%t", ltime);
  assert (strcmp(outstr,"\t") == 0);

  //  %T     The time in 24-hour notation (%H:%M:%S).  (SU)
  strftime(outstr, sizeof(outstr), "%T", ltime);
  assert (strcmp(outstr,"07:36:57") == 0);
  printf("strftime ok\n");
}

/*
int
main (int argc, char *argv[]) {
  strftime_test();
  return 0;
}
*/

