colnum = 6
tavg = [] 
tobs = []
delimiter = " " 
with open('EVV Weather Obs.txt') as f: 
    tavg.append(f.readline().split(delimiter)[colnum]) 
    print(tavg)