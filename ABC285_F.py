import io
import sys

_INPUT = """\
6
6
abcdcf
4
2 1 3
2 2 6
1 5 e
2 2 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class BIT:
    def __init__(self, n):
      self._n = n
      self.data = [0] * n
    def add(self, p, x):
      assert 0 <= p < self._n
      p += 1
      while p <= self._n:
        self.data[p - 1] += x
        p += p & -p
    #合計にはrを含まない
    def sum(self, l, r):
      assert 0 <= l <= r <= self._n
      return self._sum(r) - self._sum(l)
    def _sum(self, r):
      s = 0
      while r > 0:
        s += self.data[r - 1]
        r -= r & -r
      return s
    #pの位置をxという値にセット
    def set(self, p, x):
      self.add(p, -self.sum(p, p+1) + x)

  N=int(input())
  S=input()
  S=[ord(S[i])-ord('a') for i in range(N)]
  ordered=BIT(N-1)
  char=[BIT(N) for _ in range(26)]
  for i in range(N-1):
    if S[i]>S[i+1]: ordered.add(i,1)
  for i in range(N):
    char[S[i]].add(i,1)
  Q=int(input())
  for _ in range(Q):
    query=input().split()
    if query[0]=='1':
      x,c=query[1:]
      x=int(x)-1
      c=ord(c)-ord('a')
      if x>0:
        if S[x-1]>c: ordered.set(x-1,1)
        else: ordered.set(x-1,0)
      if x<N-1:
        if c>S[x+1]: ordered.set(x,1)
        else: ordered.set(x,0)
      char[S[x]].add(x,-1)
      char[c].add(x,1)
      S[x]=c
    else:
      l,r=map(int,query[1:])
      l-=1
      ans=0
      if ordered.sum(l,r-1)>0: ans=1
      else:
        for i in range(S[l]+1,S[r-1]):
          if char[i].sum(l,r)<char[i].sum(0,N): ans=1
      if ans==0: print('Yes')
      else: print('No')