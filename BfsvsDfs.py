from bfs import breadthF
from dfs import depthF
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

bd=maze(10,10)
bd.CreateMaze(loopPercent=10,theme='dark')

searchD,pathD,expD=depthF(bd)
searchB,pathB,expB=breadthF(bd)

a=agent(bd,footprints=True,color=COLOR.cyan,filled=True)
b=agent(bd,footprints=True,color=COLOR.yellow)
bd.tracePath({a:expB},delay=100)
bd.tracePath({b:expD},delay=100)

timeB=timeit(stmt='breadthF(bd)',number=1000,globals=globals())
timeD=timeit(stmt='depthF(bd)',number=1000,globals=globals())

textLabel(bd,'Paths BFS searched:',len(searchB)+1)
textLabel(bd,'Distance for BFS path:',len(expB)+1)
textLabel(bd,'Time BFS took:',timeB)

textLabel(bd,'Paths DFS searched:',len(searchD)+1)
textLabel(bd,'Distance for DFS path:',len(expD)+1)
textLabel(bd,'Time DFS took:',timeD)

bd.run()