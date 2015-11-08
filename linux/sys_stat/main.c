#include "../dbg.h"
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

int
main (int argc, char *argv[]) {
  struct stat sb;
  
  check(argc == 2, "Usage: %s <pathname>", argv[0]);
  check(stat(argv[1], &sb) != -1, "stat(%s)", argv[1]);
  
  printf("{\n");
  printf("    \"arg\": \"%s\", \n", argv[1]);
  printf("    \"devId\": {\n");
  printf("        \"major\": %d, \n", (int) major(sb.st_dev));
  printf("        \"minor\": %d\n", (int) minor(sb.st_dev));
  printf("     },\n");
  printf("    \"inodeNumber\": %ld, \n", (long) sb.st_ino);
  printf("    \"fileType\": ");
  switch (sb.st_mode & S_IFMT) {
  case S_IFBLK:  printf("\"block device\",\n");            break;
  case S_IFCHR:  printf("\"character device\",\n");        break;
  case S_IFDIR:  printf("\"directory\",\n");               break;
  case S_IFIFO:  printf("\"FIFO/pipe\",\n");               break;
  case S_IFLNK:  printf("\"symlink\",\n");                 break;
  case S_IFREG:  printf("\"regular file\",\n");            break;
  case S_IFSOCK: printf("\"socket\",\n");                  break;
  default:       sentinel("unknown file type");
  }
  printf("    \"mode\": %lo, \n", (unsigned long) sb.st_mode);
  printf("    \"linkCount\": %ld, \n", (long) sb.st_nlink);
  printf("    \"uid\": %ld, \n", (long) sb.st_uid);
  printf("    \"gid\": %ld, \n", (long) sb.st_gid);
  printf("    \"preferredIOBblockSize\": %ld, \n", (long) sb.st_blksize);
  printf("    \"fileSize\": %lld, \n", (long long) sb.st_size);
  printf("    \"blocksAllocated\": %lld, \n", (long long) sb.st_blocks);
  printf("    \"times\": {\n");
  printf("        \"change\": %ld, \n", (long) &sb.st_ctime);
  printf("        \"access\": %ld, \n", (long)&sb.st_atime);
  printf("        \"modification\": %ld\n", (long)&sb.st_mtime);
  printf("    }\n");
  printf("}\n");
  
  exit(EXIT_SUCCESS);

 error:
  exit(EXIT_FAILURE);
}










    ///////////////

  /* printf("File type:                "); */
  /* switch (sb.st_mode & S_IFMT) { */
  /* case S_IFBLK:  printf("block device\n");            break; */
  /* case S_IFCHR:  printf("character device\n");        break; */
  /* case S_IFDIR:  printf("directory\n");               break; */
  /* case S_IFIFO:  printf("FIFO/pipe\n");               break; */
  /* case S_IFLNK:  printf("symlink\n");                 break; */
  /* case S_IFREG:  printf("regular file\n");            break; */
  /* case S_IFSOCK: printf("socket\n");                  break; */
  /* default:       sentinel("unknown file type"); */
  /* } */
  /* printf("I-node number:            %ld\n", (long) sb.st_ino); */
  /* printf("Mode:                     %lo (octal)\n", (unsigned long) sb.st_mode); */
  /* printf("Link count:               %ld\n", (long) sb.st_nlink); */
  /* printf("Ownership:                UID=%ld   GID=%ld\n", (long) sb.st_uid, (long) sb.st_gid); */
  /* printf("Preferred I/O block size: %ld bytes\n", (long) sb.st_blksize); */
  /* printf("File size:                %lld bytes\n", (long long) sb.st_size); */
  /* printf("Blocks allocated:         %lld\n", (long long) sb.st_blocks); */
  /* printf("Last status change:       %s", ctime(&sb.st_ctime)); */
  /* printf("Last file access:         %s", ctime(&sb.st_atime)); */
  /* printf("Last file modification:   %s", ctime(&sb.st_mtime)); */
