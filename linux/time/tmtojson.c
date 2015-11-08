#include "../dbg.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

long int NOW = 1446565017;

void
print_tm_fields(struct tm *ltime) {
  printf("sec=%d\n", ltime->tm_sec);
  printf("mon=%d\n", ltime->tm_min);
  printf("hour=%d\n", ltime->tm_hour);
  printf("mday=%d\n", ltime->tm_mday);
  printf("mon=%d\n", ltime->tm_mon);
  printf("year=%d\n", ltime->tm_year);
  printf("wday=%d\n", ltime->tm_wday);
  printf("yday=%d\n", ltime->tm_yday);
  printf("isdst=%d\n", ltime->tm_isdst);
}

void
json_tm_fields(struct tm *ltime) {
  char buffer[80];
  int j;
  
  puts("{");
  j = sprintf(buffer, "    \"%s\": ", "sec");
  sprintf(buffer+j, "%d", ltime->tm_sec);
  printf("%s,\n", buffer);

  j = sprintf(buffer, "    \"%s\": ", "min");
  sprintf(buffer+j, "%d", ltime->tm_min);
  printf("%s,\n", buffer);

  j = sprintf(buffer, "    \"%s\": ", "hour");
  sprintf(buffer+j, "%d", ltime->tm_hour);
  printf("%s,\n", buffer);

  j = sprintf(buffer, "    \"%s\": ", "mday");
  sprintf(buffer+j, "%d", ltime->tm_mday);
  printf("%s,\n", buffer);

  j = sprintf(buffer, "    \"%s\": ", "mon");
  sprintf(buffer+j, "%d", ltime->tm_mon);
  printf("%s,\n", buffer);

  j = sprintf(buffer, "    \"%s\": ", "year");
  sprintf(buffer+j, "%d", ltime->tm_year);
  printf("%s,\n", buffer);

  j = sprintf(buffer, "    \"%s\": ", "wday");
  sprintf(buffer+j, "%d", ltime->tm_wday);
  printf("%s,\n", buffer);

  j = sprintf(buffer, "    \"%s\": ", "yday");
  sprintf(buffer+j, "%d", ltime->tm_yday);
  printf("%s,\n", buffer);
  
  j = sprintf(buffer, "    \"%s\": ", "isdst");
  sprintf(buffer+j, "%d", ltime->tm_isdst);
  printf("%s\n", buffer);
  puts("}");
}

/*
int
main() {
  struct tm *ltime;

  ltime = localtime((time_t *)&NOW);
  check(ltime != NULL, "localtime");
  json_tm_fields(ltime);
  exit(EXIT_SUCCESS);

 error:
  exit(EXIT_FAILURE);

}
*/
