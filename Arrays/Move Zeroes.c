#include <stdio.h>

void moveZeroes(int* nums, int numsSize) {
    int i = 0;
    for (int j = 0; j < numsSize; j++) {
        if (nums[j] != 0) {
            nums[i++] = nums[j];
        }
    }
    for (int j = i; j < numsSize; j++) {
        nums[j] = 0;
    }
}

int main() {
    int numsSize;
    scanf("%d", &numsSize);
    int nums[numsSize];
    for (int i = 0; i < numsSize; i++) {
        scanf("%d", &nums[i]);
    }

    moveZeroes(nums, numsSize);

    for (int i = 0; i < numsSize; i++) {
        printf("%d ", nums[i]);
    }

    return 0;
}
