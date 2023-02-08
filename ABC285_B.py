import io
import sys

_INPUT = """\
6
6
abcbac
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  for i in range(N-1):
    l=0
    while l<N-i-1 and S[l]!=S[l+i+1]:
      l+=1
    print(l)