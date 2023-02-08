import io
import sys

_INPUT = """\
6
AB
C
BRUTMHYHIIZP
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  tmp=[]
  for i in range(14):
    tmp.append(26**i)
  print(sum(tmp[:len(S)])+sum([(ord(S[i])-ord('A'))*26**(len(S)-i-1) for i in range(len(S))]))