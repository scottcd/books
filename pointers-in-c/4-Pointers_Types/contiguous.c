#include <stdio.h>
int main(void)
{
  int a[] = { 1, 2, 3, 4, 5 };
  int n = sizeof a / sizeof *a;
  // get a pointer to the beginning of a
  int *ip = a;
  char *cp = (char *)a;
  for (int i = 0; i < n; i++) {
    printf("a[%d] sits at %p / %p / %p\n",
           i, (void *)&a[i], (void *)(ip + i),
           (void *)(cp + i * sizeof *a));
  }
  return 0;
}