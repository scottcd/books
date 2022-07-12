#include <stdio.h>

void doesnt_mutate(int i)
{
    i += 9;
}

void mutate(int* i)
{
    *i += 9;
}

int main()
{
    int i = 0;
    doesnt_mutate(i);
    printf("%d\n",i);
    mutate(&i);
    printf("%d\n",i);
}