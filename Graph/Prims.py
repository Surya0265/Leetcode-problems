import sys



def minkey(key,mstset,V):
      min_index=-1
      mini=sys.maxsize
      for v in range(V):
            if key[v]<mini and not mstset[v]:
                  mini=key[v]
                  min_index=v
      return min_index






def prims(graphs,V):
      key=[sys.maxsize]*V
      mstset=[None]*False
      parent=[None]*V

      key[0]=0
      parent[0]=-1

      u=minkey(key,mstset,V)
      for v in range(V):
            if graphs[u][v]>0 and not mstset[v] and key[v]>graphs[u][v]:
                  key[v]=graphs[u][v]
                  