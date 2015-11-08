#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char
randchar () {
  return random() % 26 + 'A';
}

int
main (int argc, char *argv[]) {

  int i;
  char *offset;
  char s[26] = "abcDefghijklmnopDzzzz";
  // char t[26];
  char buf[26];
  char *t;
  
  // char *index(const char *s, int c);
  offset = index(s, 'D');
  assert (strcmp("DefghijklmnopDzzzz", offset) == 0);
  
  offset = index(s, 'x');
  assert (offset == NULL);

  // char *rindex(const char *s, int c);
  offset = rindex(s, 'D');
  assert (strcmp("Dzzzz", offset) == 0);
  
  // char *strchr(const char *s, int c);
  offset = strchr(s, 'D');
  assert (strcmp("DefghijklmnopDzzzz", offset) == 0);

  offset = strchr(s, 'x');
  assert (offset == NULL);

  // char *strrchr(const char *s, int c);
  offset = strrchr(s, 'D');
  assert (strcmp("Dzzzz", offset) == 0);
  
  // char *stpcpy(char *dest, const char *src);
  for (i=0; i<26; i++)
    buf[i] = 0;
  t = buf;
  t = stpcpy(t, "bat");
  t = stpcpy(t, "dig");
  assert (strcmp("batdig", buf) == 0);

  // char *strcpy(char *dest, const char *src);
  for (i=0; i<26; i++)
    buf[i] = 0;
  offset = strcpy(buf, "catdog");
  assert (strcmp("catdog", offset) == 0);
  // printf("%s\n", offset);
  
  // char *strcat(char *dest, const char *src);
  for (i=0; i<26; i++)
    buf[i] = 0;
  t = buf;
  t = strcat(t, "bat");
  t = strcat(t, "dig");
  assert (strcmp("batdig", buf) == 0);
  
  // char *strncat(char *dest, const char *src, size_t n);
  for (i=0; i<26; i++)
    buf[i] = 0;
  t = buf;
  t = strcat(t, "12345678901234567890");
  t = strncat(t, "abcdefghijklmn", 5);
  assert (strcmp("12345678901234567890abcde", buf) == 0);
  // printf("%s\n", buf);
  printf("ok\n");
  return 0;
}

/*


char *strdup(const char *s);
char *strfry(char *string);
char *strpbrk(const char *s, const char *accept);
char *strsep(char **stringp, const char *delim);
char *strstr(const char *haystack, const char *needle);
char *strtok(char *s, const char *delim);
int strcasecmp(const char *s1, const char *s2);
int strcmp(const char *s1, const char *s2);
int strcoll(const char *s1, const char *s2);
int strncasecmp(const char *s1, const char *s2, size_t n);
int strncmp(const char *s1, const char *s2, size_t n);
size_t strcspn(const char *s, const char *reject);
size_t strlen(const char *s);
size_t strspn(const char *s, const char *accept);
size_t strxfrm(char *dest, const char *src, size_t n);

char *strncpy(char *dest, const char *src, size_t n);
*/

