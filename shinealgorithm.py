coor = [[1,1],[1,4],[3,4],[3,2],[4,3],[5,2],[6,2],[6,3],[7,3],[7,1]]
point = [2,2]
si = []
le = []
zov = []
coor.append(coor[0])
for i in coor:
    zov.append(i)
def findarea(coordinate):
    for i in range(len(coordinate)-1):
        si.append((coordinate[i][0]*coordinate[i+1][1])-(coordinate[i][1]*coordinate[i+1][0]))
        area = abs((sum(si)) / 2.0)
    print(area)
    return area
for i in range(len(coor)-1):
    leng = (((point[0]-coor[i][0])**2) + ((point[1]-coor[i][1])**2)**0.5)
    le.append(leng)
for i in range(len(le)-1):
    if min(le)==le[i]:
        if le[i+1] > le[i-1]:
            zov.insert(i-1,point)
            break
        else:
            zov.insert(i+1, point)
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