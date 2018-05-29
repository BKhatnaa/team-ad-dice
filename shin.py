poly = [[1,2],[3,-1],[-1,-2]]
pnt = [2,-0.5]

c = poly
v = []
l = []
for i in range(len(c)-1):
	if (c[i][0] - c[i+1][0]) == 0:
		slope = 0
	else:
		slope = (c[i][1]-c[i+1][1])/(c[i][0]-c[i+1][0])
	if slope == 0:
		sh = 0
	else:
		sh = (pnt[1]-c[i][1]+ (slope * c[i][0]))/slope
	if (c[i][0] <= sh and sh <= c[i+1][0] or c[i+1][0] <= sh and sh <= c[i][0]):
		if not ((poly[i][1] != pnt[1]) and (poly[i+1][1] >= pnt[1] and poly[i-1][1] >= pnt[1]) or (poly[i+1][1] <= pnt[1] and poly[i-1][1] <= pnt[1])):
			v.append("1")

if(len(v) % 2 == 0):
	print("outside")
else:
	print("inside")
