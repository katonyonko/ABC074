from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="074"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc083_a".format(times, problem)) as res:
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
  A,B,C,D,E,F=map(int,input().split())
  dp=[[False]*(F+1) for _ in range(F+1)]
  dp[0][0]=True
  ans=(100*A,0)
  for i in range(F+1):
    for j in range(F+1):
      if dp[i][j]==True:
        if i+100*A<=F: dp[i+100*A][j]=True
        if i+100*B<=F: dp[i+100*B][j]=True
        if j+C<=F: dp[i][j+C]=True
        if j+D<=F: dp[i][j+D]=True
      if dp[i][j]==True and i+j<=F and j<=E*i//100 and ans[1]*(i+j)<ans[0]*j:
        ans=(i+j,j)
  print(*ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])