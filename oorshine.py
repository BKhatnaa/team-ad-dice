coor = [[1,1],[1,4],[4,1]]
point = [2,4]
si = []
le = []
zov = []
coor.append(coor[0])
from shapely.geometry import Polygon
for i in coor:
    zov.append(i)
def findarea(coordinate):
    for i in range(len(coordinate)-1):
        si.append((coordinate[i][0]*coordinate[i+1][1])-(coordinate[i][1]*coordinate[i+1][0]))
        area = abs((sum(si)) / 2.0)
    print(area)
    return area
mid = []

for i in  range(len(coor)-1):
    midx = (coor[i][0]+coor[i+1][0])/2 
    midy = (coor[i][1]+coor[i+1][1])/2
    mid.append([midx,midy])

for i in range(len(coor)-1):
    leng = (((point[0]-mid[i][0])**2) + ((point[1]-mid[i][1])**2)**0.5)
    le.append(leng)
for i in range(len(le)):
    if min(le) == le[i]:
        zov.insert(i+1,point)
        break
ehniih = findarea(coor)
daraa = findarea(zov)
print(coor)
print(zov)
daraa = daraa - ehniih

if ehniih > daraa:
    print('dotor')
else:
    print('gadaa')