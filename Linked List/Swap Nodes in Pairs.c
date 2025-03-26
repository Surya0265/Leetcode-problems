/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
 
     dummy->val=0;
     dummy->next=head;
     struct ListNode* curr=head;
     struct ListNode* newNode;
     struct ListNode* prev=dummy;
     while(curr!=NULL && curr->next!=NULL){
          newNode=curr->next;
          curr->next=newNode->next;
          newNode->next=curr;
          prev->next=newNode;
          prev=curr;
          curr=curr->next;
 
 
     }
     return dummy->next;
 
 
     
 }