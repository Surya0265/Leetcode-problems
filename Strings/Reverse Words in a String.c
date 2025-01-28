void reverse(char *s,int start,int end){
    while(start<end){
       char temp=s[start];
       s[start]=s[end];
       s[end]=temp;
       end--;
       start++;
    }

}

char* reverseWords(char* s) {
    int n=strlen(s);
    int i=0;
    int j=0;
    while(s[i]==' ') i++;

    char temp[n+1];
    int k=0;
    for(;i<n;i++){
       if(s[i]!=' '||(k>0&&temp[k-1]!=' ')){
        temp[k++]=s[i];

    }

    }
    while(k>0&&temp[k-1]==' ') k--;

    temp[k]='\0';

    reverse(temp,0,k-1);
    for(int i=0;i<=k;i++){
        if(temp[i]==' '||temp[i]=='\0'){
            reverse(temp,j,i-1);
            j=i+1;
        }
    }
    strcpy(s,temp);
    
   return s;
    
}

