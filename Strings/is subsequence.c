bool isSubsequence(char* s, char* t) {
    int j=0;
   for(int i=0;i<strlen(t);t++){
           if(s[j]==t[i]){
                 j++;
           }
      
   }
   if(j==strlen(s)){
         return true;
   }
   return false;
}