from astar import aStar
from bfs import breadthF
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

ab=maze(10,10)
ab.CreateMaze(loopPercent=10,theme='dark')

searchA,pathA,expA=aStar(ab)
searchB,pathB,expB=breadthF(ab)

a=agent(ab,footprints=True,color=COLOR.green,filled=True)
b=agent(ab,footprints=True,color=COLOR.blue)

ab.tracePath({a:expB},delay=100)
ab.tracePath({b:expA},delay=100)

timeA=timeit(stmt='aStar(ab)',number=1000,globals=globals())
timeB=timeit(stmt='breadthF(ab)',number=1000,globals=globals())

textLabel(ab,'Paths A* searched:',len(searchA)+1)
textLabel(ab,'Distance for A* path:',len(expA)+1)
textLabel(ab,'Time A* took:',timeA)

textLabel(ab,'Paths BFS searched:',len(searchB)+1)
textLabel(ab,'Distance for BFS path:',len(expB)+1)
textLabel(ab,'Time BFS took:',timeB)

ab.run()