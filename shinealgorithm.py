coor = [[0,1],[1,3],[2,1]]
point = [1,2]
zov = []
l = []
first = coor[0]
le = []
coor.append(first)
for i in coor:
    zov.append(i)
def findarea(coordinate):
    for i in range(len(coordinate)-1):
        sig = (coordinate[i][0]*coordinate[i+1][1] - coordinate[i][1]*coordinate[i+1][0])
        l.append(sig)
        area = abs(sum(l) / 2)
    print(area)
for i in range(len(coor)-1):
    leng = (((point[0]-coor[i][0])**2) + ((point[1]-coor[i][1])**2)**0.5)
    le.append(leng)
for i in range(len(le)):
    if min(le)==le[i]:
        zov.insert(i+1,point)
        break
ehniih = findarea(coor)
daraa = findarea(zov)
print(coor)
print(zov)
if ehniih > daraa:
    print('dotor')
else:
    print('gadaa')