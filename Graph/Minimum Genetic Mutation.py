class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set=set(bank)
        map_m={'A':'CTG','C':'ATG','T':'ACG','G':'ATC'}
        queue=deque([(startGene,0)])
        while queue:
             cur_seq,step=queue.popleft()
             if cur_seq==endGene:
                   return step
             for i,gene in enumerate(cur_seq):
               for mutation in map_m[gene]:
                         next_seq=cur_seq[:i]+mutation+cur_seq[i+1:] 
                         if next_seq in bank_set:

                               queue.append((next_seq,step+1))
                               bank_set.remove(next_seq)
        return -1
                                   
        