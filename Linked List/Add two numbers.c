/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummy=(struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->next=NULL;
    struct ListNode* res=dummy;
    int carry=0;
    while(l1!=NULL|| l2!=NULL){
        int sum=carry;
        if(l1!=NULL){
            sum+=l1->val;
            l1=l1->next;
        }
        if(l2!=NULL){
            sum+=l2->val;
            l2=l2->next;
        }
        carry=sum/10;
        struct ListNode* newNode=(struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->next=NULL;
        newNode->val=sum%10;
        res->next=newNode;
   
     
        res=res->next;
    }
    if (carry!=0){
        struct ListNode* newNode=(struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->next=NULL;
        newNode->val=carry;
        res->next=newNode;


    }
    return dummy->next;

    
}