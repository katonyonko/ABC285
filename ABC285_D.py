import io
import sys

_INPUT = """\
6
2
b m
m d
3
a b
b c
c a
5
aaa bbb
yyy zzz
ccc ddd
xxx yyy
bbb ccc
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop,heappush
  def TopologicalSort(G):
    G2=[set() for _ in range(len(G))]
    for i in range(len(G)):
      for v in G[i]:
        G2[v].add(i)
    res=[]
    h=[]
    for i in range(len(G)):
      if len(G2[i])==0:
        heappush(h,i)
    while len(h):
      x=heappop(h)
      res.append(x)
      for y in G[x]:
        G2[y].remove(x)
        if len(G2[y])==0:
          heappush(h,y)
    if len(res)==len(G):
      return res
    else:
      return -1

  N=int(input())
  d={}
  G=[]
  idx=0
  for i in range(N):
    s,t=input().split()
    if s not in d:
      d[s]=idx
      G.append([])
      idx+=1
    if t not in d:
      d[t]=idx
      G.append([])
      idx+=1
    G[d[s]].append(d[t])
  if TopologicalSort(G)==-1: print('No')
  else: print('Yes')