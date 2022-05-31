from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
from timeit import timeit

def h(cellx, celly):

    x1, y1 = cellx
    x2, y2 = celly

    return (abs(x1 - x2) + abs(y1 - y2))
    
def aStar(a,discover=None):
    if discover is None:
        discover=(a.rows,a.cols)
    explore = PriorityQueue()
    explore.put((h(discover, a._goal), h(discover, a._goal), discover))
    pathA = {}
    gPoint = {row: float("inf") for row in a.grid}
    gPoint[discover] = 0
    fPoint = {row: float("inf") for row in a.grid}
    fPoint[discover] = h(discover, a._goal)
    searchA=[discover]

    while not explore.empty():
        bigCell = explore.get()[2]
        searchA.append(bigCell)
        if bigCell == a._goal:
            break        
        for d in 'ESNW':
            if a.maze_map[bigCell][d]==True:
                if d=='E':
                    smaCell=(bigCell[0],bigCell[1]+1)
                elif d=='W':
                    smaCell=(bigCell[0],bigCell[1]-1)
                elif d=='N':
                    smaCell=(bigCell[0]-1,bigCell[1])
                elif d=='S':
                    smaCell=(bigCell[0]+1,bigCell[1])

                testgP = gPoint[bigCell] + 1
                testfP = testgP + h(smaCell, a._goal)

                if testfP < fPoint[smaCell]:   
                    pathA[smaCell] = bigCell
                    gPoint[smaCell] = testgP
                    fPoint[smaCell] = testgP + h(smaCell, a._goal)
                    explore.put((fPoint[smaCell], h(smaCell, a._goal), smaCell))


    expA={}
    cell=a._goal
    while cell!=discover:
        expA[pathA[cell]]=cell
        cell=pathA[cell]
    return searchA,pathA,expA

if __name__=='__main__':
    a=maze(10,10)
    a.CreateMaze(loopPercent=10,theme='dark')
   

    searchA,pathA,expA=aStar(a)
    q=agent(a,footprints=True,color=COLOR.blue,filled=True)
    w=agent(a,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(a.rows,a.cols))
    e=agent(a,footprints=True,color=COLOR.red)
    timeA=timeit(stmt='aStar(a)',number=1000,globals=globals())


    a.tracePath({q:searchA},delay=100)
    a.tracePath({w:pathA},delay=100)
    a.tracePath({e:expA},delay=100)
    
    l=textLabel(a,'Distance for A* path:',len(searchA))
    l=textLabel(a,'A Star Path Length',len(expA)+1)
    textLabel(a,'Time A* took:',timeA)

    a.run()
