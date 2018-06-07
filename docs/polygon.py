
def olon(filename):
	import json
	from shapely.geometry import Polygon
	with open(filename) as s:
        	data = json.load(s)
	c = data['coordinates']
	pnt = data['check']
	v=[]
	d = []
	pp = Polygon(c)
	a = pp.is_valid
	for i in range(len(c)):
		if(c[i-1][1] == c[i][1]):
			d.append("1")
	if(a == False):
		return "Ogtoltsol"
	else:
		for i in range(len(c)-len(d)-1):
			if(c[i][0] == pnt[0] and c[i][1] == pnt[1]):
				return "oroin tseg"
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
				#tsegiin x ees ih ogtoltsliin tsegiig shalgah
				if(sh >= pnt[0]):
					#Shalgah heseg
					if(c[i+len(d)+1][1] > pnt[1] and c[i-1][1] < pnt[1] or c[i-1][1] > pnt[1] and c[i+len(d)+1][1] < pnt[1]) or (c[i+1][1] >= pnt[1] and c[i][1] <= pnt[1] or c[i+1][1] <= pnt[1] and c[i][1] >= pnt[1]):	
						v.append("1")
		print(len(v))						
		if(len(v) % 2 == 0):
			return "outside"
		else:
			return "inside"

olon('pg1.json')
