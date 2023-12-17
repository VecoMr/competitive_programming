#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
    int n = atoi(av[1]);
    int i, j, k;
    int **a = malloc(n * sizeof(int *));
    for (i = 0; i < n; i++)
        a[i] = malloc(n * sizeof(int));
    for (i = 0; i < n; i++)
        a[i][0] = a[0][i] = 1;
    for (i = 1; i < n; i++)
        for (j = 1; j < n; j++)
            a[i][j] = a[i - 1][j] + a[i][j - 1];
    printf("%d\n", a[n - 1][n - 1]);
    return 0;
}