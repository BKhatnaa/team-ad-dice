import json

with open('pg.json') as s:
        data = json.load(s)
c = data['coordinates']

pnt = [1,1]
v = []
for i in range(len(c)-1):
	if(c[i][0] == pnt[0] and c[i][1] == pnt[1]):
		print("oroin tseg")
	else:
		if(c[i][0]-c[i+1][0] == 0):
			if(c[i][1] >= pnt[1] and c[i+1][1] <= pnt[1] or c[i+1][1] >= pnt[1] and c[i][1] <= pnt[1]):
				sh = c[i][0]
			else:
				sh = 0
		else:
			slope = (c[i][1]-c[i+1][1])/(c[i][0]-c[i+1][0])
			if slope == 0:
				sh = 0
			else:
				#intersection point x
				sh = (pnt[1]-c[i][1]+ (slope * c[i][0]))/slope
				if(sh >=c[i][0] and sh <= c[i+1][0] or sh <= c[i][0] and sh >=c[i+1][0]):
					sh = (pnt[1]-c[i][1]+ (slope * c[i][0]))/slope
				else: 
					sh = 0
		#Check point		
		if(sh == pnt[0] and pnt[1] == c[i][1]):
			v.append("1")
		elif(sh >= pnt[0]):
			v.append("1")
print(c)
print(len(v))
#Check inside or outside		
if(len(v) % 2 == 0):
	print("outside")
else:
	print("inside")
