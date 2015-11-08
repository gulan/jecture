#include <assert.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int
t01 (void) {
  mode_t mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;
  int fd;

  fd = creat("/tmp/file1", mode);
  if (fd == -1) {
    perror("creat");
    return 0;
  }
  close(fd);
  return 1;
}

int
t02 (void) {
  mode_t mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;
  int fd;

  fd = creat("/tmp/fi/le1", mode);
  if (fd == -1) {
    perror("creat");
    return 1;
  }
  close(fd);
  return 0;
}

/* The overloaded return value of write() bugs me, but I suppose I
should just get used to this style for C programming. */
void
writer (int fd, char *data, int *count, int *error) {
  int orig = *count;
  int rc;

  rc = write(fd, data, orig);
  if (rc == -1) {
    *error = 1;
    *count = 0;
  } else {
    *error = 0;  /* unchanged */
    *count = orig - rc;
  }
}

int
t03 (void) {
  #define N 12
  int fd;
  // Each data entry is len(N) - 2
  char *data[] = {"abcd one  \n", "efgh two  \n", "ijkl three\n"};
  int i, j, count, error;
  char buf[N];
  
  // Write some data
  fd = creat("/tmp/file2", S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
  if (fd == -1) {
    perror("creat");
    return 0;
  }
  for (i=0; i<3; i++) {
    count = strlen(data[i]);
    error = 0;
    while (!error && count > 0)
      writer(fd, data[i], &count, &error);
  }
  if (count == -1) {
    perror("write");
    return 0;
  }
  fsync(fd);
  close(fd);
  
  // Read it back and compare
  fd = open("/tmp/file2", S_IRUSR);
  if (fd == -1) {
      perror("open");
      return 0;
  }
  for (i=0; i<N; i++) buf[i] = 0;
  j = 0;
  count = read(fd,buf,N-1);
  while (count > 0) {
    assert (strcmp(data[j], buf) == 0);
    for (i=0; i<N; i++) buf[i] = 0;
    j++;
    count = read(fd,buf,N-1);
  }
  if (count == -1) {
    perror("read");
    return 0;
  }
  close(fd);

  return 1;
}

int
main (int argc, char *argv[]) {
  assert (t01());
  assert (t02());
  assert (t03());
  printf("ok\n");
  return 0;
}

/*   
 O_APPEND
 O_ASYNC
 O_CLOEXEC
 O_CREAT
 O_DIRECT
 O_DIRECTORY
 O_EXCL
 O_LARGEFILE
 O_NDELAY
 O_NOATIME
 O_NOCTTY
 O_NOFOLLOW
 O_NONBLOCK
 O_PATH
 O_SYNC
 O_TRUNC
*/
