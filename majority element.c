#include <stdio.h>

int findMajorityElement(int arr[], int n) {
    int count = 0, candidate = -1;
    for (int i = 0; i < n; i++) {
        if (count == 0) {
            candidate = arr[i];
        }
        count += (arr[i] == candidate) ? 1 : -1;
    }
    count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == candidate) {
            count++;
        }
    }
    return (count > n / 2) ? candidate : -1;
}

int main() {
    int arr[] = {3, 3, 4, 2, 4, 4, 2, 4, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = findMajorityElement(arr, n);
    if (result != -1) {
        printf("The majority element is %d\n", result);
    } else {
        printf("No majority element found\n");
    }
    return 0;
}
