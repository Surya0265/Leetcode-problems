/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head==NULL){
        return NULL;
    }
    int n=1;

    struct ListNode* tail=head;
    while(tail->next!=NULL){
        tail=tail->next;
        n+=1;

    }
    k=k%n;
    if(k==0){
        return head;
    }
    struct ListNode* curr=head;
    for(int i=0;i<n-k-1;i++){
           curr=curr->next;
    }
    struct ListNode* newhead=curr->next;
    curr->next=NULL;
    tail->next=head;

    return newhead;
}
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to build linked list from a list of numbers
def build_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Function to reverse the linked list
def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# -------------------------------
# Get input from user
nums = list(map(int, input("Enter list elements separated by space: ").split()))

# Build linked list
head = build_linked_list(nums)

print("Original list:")
print_linked_list(head)

# Reverse linked list
reversed_head = reverseList(head)

print("Reversed list:")
print_linked_list(reversed_head)


