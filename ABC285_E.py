import io
import sys

_INPUT = """\
6
7
10 10 1 1 1 1 1
10
200000000 500000000 1000000000 800000000 100000000 80000000 600000 900000000 1 20
20
38 7719 21238 2437 8855 11797 8365 32285 10450 30612 5853 28100 1142 281 20537 15921 8945 26285 2997 14680
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  tmp=[0]
  for i in range(N-1): tmp.append(tmp[-1]+A[i//2])
  dp=[0]*N
  for i in range(N-1):
    for j in range(1,N-i):
      dp[i+j]=max(dp[i+j],dp[i]+tmp[j-1])
  print(max([dp[i]+tmp[N-1-i] for i in range(N)]))