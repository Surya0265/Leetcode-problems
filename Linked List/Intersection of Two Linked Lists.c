struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *p=headA;
    struct ListNode *q=headB;
    if(p==NULL||q==NULL)return NULL;
    while(p!=q){
        p=(p==NULL)?headB:p->next;
        q=(q==NULL)?headA:q->next;
    }
    return p;
    
}