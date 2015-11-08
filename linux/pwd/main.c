#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <pwd.h>
#include <sys/types.h>

static void
prt_passwd(struct passwd *pw) {
  printf("name=%s\n", pw->pw_name);
  printf("passwd=%s\n", pw->pw_passwd);
  printf("uid=%d\n", pw->pw_uid);
  printf("gid=%d\n", pw->pw_gid);
  printf("gecos=\"%s\"\n", pw->pw_gecos);
  printf("dir=%s\n", pw->pw_dir);
  printf("shell=%s\n\n", pw->pw_shell);
}

void
user_by_uid (uid_t uid) {
  struct passwd *pw;
  pw = getpwuid(uid);
  if (pw==NULL) {
    fprintf(stderr, "No entry found. -u %d\n", (int)uid);
    exit(-1);
  };
  prt_passwd(pw);
}

void
user_by_name (const char *name) {
  struct passwd *pw;
  pw = getpwnam(name);
  if (pw==NULL) {
    fprintf(stderr, "No entry found. -u %s\n", name);
    exit(-1);
  };
  prt_passwd(pw);
}

void
list_passwd () {
  struct passwd *pw;

  while (1) {
    pw = getpwent();
    if (pw == NULL) 
      break;
    prt_passwd(pw);
  }
  endpwent();
}

int
main (int argc, char *argv[]) {
  list_passwd();
  user_by_uid(0);
  user_by_name("games");
  printf("pwd ok\n");
  return 0;
}

