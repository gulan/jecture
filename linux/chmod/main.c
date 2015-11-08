#define N 80

#include "../dbg.h"
#include <assert.h>
#include <dirent.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

/*
             json = doc-begin + result-section + doc-end 
        doc-begin = '{\n'
   result-section = result-begin + result-body + result-end
     result-begin = in4 + '"results": [\n'
      result-body = first-result + remaining-results
       result-end = '\n' + in4 + ']'
     first-result = in8 + primary
remaining-results = secondary*
        secondary = ',\n' + in8 + primary
          doc-end = '\n}\n'
          primary = '{"fname": "tfile-%s", "octalMode": %o}'
        secondary = ',\n' + in8 + primary
              in4 = '    '
              in8 = in4 + in4
*/

void doc_begin(void) { printf("{\n"); }
void doc_end(void) { printf("\n}\n"); }
void result_begin(void) { printf("    \"results\": [\n"); }
void result_end(void) { printf("\n    ]"); }

void
primary(char const *fname, int perms, char *buffer) {
  char *template = "{\"fname\": \"%s\", \"octalMode\": %o}";
  sprintf(buffer, template, fname, perms);
}

void
first(char const *fname, int perms) {
  char buf[N-1];
  char buf2[N-1];
  
  for (int i=0; i<N; i++) buf[i] = 0;
  primary(fname, perms, buf);
  for (int i=0; i<N; i++) buf2[i] = 0;
  sprintf(buf2, "        %s", buf);
  printf("%s", buf2);
}

void
second(char const *fname, int perms) {
  char buf[N-1];
  char buf2[N-1];
  
  for (int i=0; i<N; i++) buf[i] = 0;
  primary(fname, perms, buf);
  for (int i=0; i<N; i++) buf2[i] = 0;
  sprintf(buf2, ",\n        %s", buf);
  printf("%s", buf2);
}

int
main (int argc, char *argv[]) {
  char buf[N-1];
  int j;
  int fd;
  doc_begin();
  result_begin();
  j = 0;
  for (int i=0; i<N; i++) buf[i] = 0;
  sprintf(buf, "tfile-%3.3d", j);
  fd = creat(buf, j);
  check(fd != -1, "creat(%s) failed", buf);
  first(buf,j);
  close(fd);
  for (j=1; j<256; j++) {
    for (int i=0; i<N; i++) buf[i] = 0;
    sprintf(buf, "tfile-%3.3d", j);
    fd = creat(buf, j);
    check(fd != -1, "creat(%s) failed", buf);
    second(buf,j);
    close(fd);
  }
  result_end();
  doc_end();
  return 0;

 error:
  return 1;
}
