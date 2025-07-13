import itertools
cards=input()
res=[]
def rank_value(r):
     if r=='A':
          return 14
     elif r=='K':
          return 13
     elif r=='Q':
          return 12
     elif r=='J':
          return 11
     else:
          return int(r)
          
def is_straight(ranks):
     values=sorted([rank_value(r) for r in ranks])
     for i in range(4):
          if values[i+1]-values[i]!=1:
               return False
     return True
def parse(hand):
     ranks=[]
     suits=[]
     for card in hand:
          if len(card)==3:
               ranks.append('10')
               suits.append(card[2])
          else:
               ranks.append(card[0])
               suits.append(card[1])
hands=list(itertools.combinations(cards,5))
def is_flush(suits):
     return len(set(suits))==1
for hand in hands:
    res.classify(hand)
def classify(hand):
     ranks,suits=parse(hand)
     ranks_counts={r:ranks.count(r) for r in ranks}
     counts=sorted(ranks_counts.values(),reverse=True)
     straight=is_straight(ranks)
     flush=is_flush(suits)
     if straight and flush:
          return 'Straight Flush'
     elif 4 in counts:
          return "Four of a Kind"
     elif 3 in counts and 2 in counts:
          return "Full House"
     elif flush:
          return 'Flush'
     elif straight:
          return 'Straight'
     elif counts.count(2)==2:
             return 'Two pair'
     elif 2 in counts:
          return 'One Pair'
     else:
          return "High card"
