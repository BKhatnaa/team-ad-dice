poly = [[0,1],[0,4],[2,4],[1,2],[3,2],[3,3],[4,2],[4,1]]
pnt = [1,3]
c = []
v = []
for i in range(len(poly)):
    if(poly[i][0] >= pnt[0]):
        c.append(poly[i])
for i in range(len(c)-1):
	slope = (c[i][1]-c[i+1][1])/c[i][0]-c[i+1][0]
	if slope == 0:
		sh = 0
	else:
		sh = (pnt[1]-c[i][1]+ (slope * c[i][0]))/slope
	if(c[i][0] <= sh and sh <= c[i+1][0] or c[i+1][0] <= sh and sh <=c[i][0]):
		if poly[i][1] != pnt[1]:
			v.append("1")
print(c)		
if(len(v) % 2 == 0):
	print("outside")
else:
	print("inside")
