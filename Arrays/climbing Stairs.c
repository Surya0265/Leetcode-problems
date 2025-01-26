#include <stdio.h>

int climbStairs(int n) {
    int a = 1;
    int b = 2;
    int c;
    if (n == 1 || n == 2) return n;

    for (int i = 3; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }

    return c;
}

int main() {
    int n;
    printf("Enter the number of stairs - ");
    scanf("%d", &n);

    int ways = climbStairs(n);
    printf("Number of ways to climb %d stairs is: %d\n", n, ways);

    return 0;
}
