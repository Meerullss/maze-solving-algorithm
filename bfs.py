from pyamaze import maze,agent,textLabel,COLOR
from collections import deque
from timeit import timeit

def breadthF(b,run=None):
    if run is None:
        run=(b.rows,b.cols)
    unexp = deque()
    unexp.append(run)
    pathB = {}
    exp = [run]
    searchB=[]

    while len(unexp)>0:
        bigCell=unexp.popleft()
        if bigCell==b._goal:
            break
        for d in 'ESNW':
            if b.maze_map[bigCell][d]==True:
                if d=='E':
                    smaCell=(bigCell[0],bigCell[1]+1)
                elif d=='W':
                    smaCell=(bigCell[0],bigCell[1]-1)
                elif d=='S':
                    smaCell=(bigCell[0]+1,bigCell[1])
                elif d=='N':
                    smaCell=(bigCell[0]-1,bigCell[1])
                if smaCell in exp:
                    continue
                unexp.append(smaCell)
                exp.append(smaCell)
                pathB[smaCell] = bigCell
                searchB.append(smaCell)
  
    expB={}
    cell=b._goal
    while cell!=(b.rows,b.cols):
        expB[pathB[cell]]=cell
        cell=pathB[cell]
    return searchB,pathB,expB
    
if __name__=='__main__':
    b=maze(10,10)
    b.CreateMaze(loopPercent=10,theme='dark')
   

    searchB,pathB,expB=breadthF(b)
    q=agent(b,footprints=True,color=COLOR.blue,filled=True)
    w=agent(b,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(b.rows,b.cols))
    e=agent(b,footprints=True,color=COLOR.red)
    timeB=timeit(stmt='breadthF(b)',number=1000,globals=globals())

    b.tracePath({q:searchB},delay=100)
    b.tracePath({w:pathB},delay=100)
    b.tracePath({e:expB},delay=100)
    
    l=textLabel(b,'Paths BFS searched:',len( searchB))
    l=textLabel(b,'Distance for BFS path:',len(expB)+1)
    textLabel(b,'Tiabe BFS took:',timeB)

    b.run()