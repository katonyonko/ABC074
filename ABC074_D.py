from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="074"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc083_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  import copy
  N=int(input())
  A=[list(map(int,input().split())) for _ in range(N)]
  ans=sum([sum(A[i]) for i in range(N)])
  used=[[False]*N for _ in range(N)]
  cost=copy.deepcopy(A)
  INF=10**20
  for k in range(N):
    for i in range(N):
        for j in range(N):
          cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
          if used[i][j]==False and k!=i and k!=j and cost[i][j] == cost[i][k] + cost[k][j]: ans-=cost[i][j]; used[i][j]=True
  ans//=2
  for i in range(N):
    for j in range(N):
      if A[i][j]!=cost[i][j]:
        ans=-1
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])