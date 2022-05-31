from pyamaze import maze,agent,textLabel,COLOR

def depthF(df,run=None):
    if run is None:
        run=(df.rows,df.cols)
        
    exp=[run]
    unexp=[run]
    pathD={}
    searchD=[]
    while len(unexp)>0:
        bigCell=unexp.pop()
        searchD.append(bigCell)
        if bigCell==df._goal:
            break
        lc=0
        for d in 'ESNW':
            if df.maze_map[bigCell][d]==True:
                if d =='E':
                    smaCell=(bigCell[0],bigCell[1]+1)
                if d =='W':
                    smaCell=(bigCell[0],bigCell[1]-1)
                if d =='N':
                    smaCell=(bigCell[0]-1,bigCell[1])
                if d =='S':
                    smaCell=(bigCell[0]+1,bigCell[1])
                if smaCell in exp:
                    continue
                lc+=1
                exp.append(smaCell)
                unexp.append(smaCell)
                pathD[smaCell]=bigCell
        if lc>1:
            df.markCells.append(bigCell)

    expD={}
    cell=df._goal
    while cell!=run:
        expD[pathD[cell]]=cell
        cell=pathD[cell]
    return searchD,pathD,expD

if __name__=='__main__':
    df=maze(10,10) 
    df.CreateMaze(loopPercent=10,theme='dark') 

    searchD,pathD,expD=depthF(df) 
    a=agent(df,footprints=True,color=COLOR.green)
    b=agent(df,footprints=True,filled=True)
    c=agent(df,5,1,footprints=True,color=COLOR.yellow)
    
    df.tracePath({a:searchD},showMarked=True)
    df.tracePath({b:pathD})
    df.tracePath({c:expD})

    df.run()