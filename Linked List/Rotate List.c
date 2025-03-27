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