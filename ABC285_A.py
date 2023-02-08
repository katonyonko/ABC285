import io
import sys

_INPUT = """\
6
1 2
2 8
14 15
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  a,b=map(int,input().split())
  if b//2==a: print('Yes')
  else: print('No')