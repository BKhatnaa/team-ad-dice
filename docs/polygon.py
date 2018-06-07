
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
	if(a == False):
		return "Ogtoltsol"
	else:
		for i in range(len(c)-1):
			if(c[i][0] == pnt[0] and c[i][1] == pnt[1]):
				return "oroin tseg"
			else:
				if(c[i][0]-c[i+1][0] == 0):
					sh = c[i][0]
				else:
					slope = (c[i][1]-c[i+1][1])/(c[i][0]-c[i+1][0])
					if slope == 0:
						sh = c[i][0]
					else:
						#intersection point x
						sh = (pnt[1]-c[i][1]+ (slope * c[i][0]))/slope
						#if(sh >=c[i][0] and sh <= c[i+1][0] or sh <= c[i][0] and sh >=c[i+1][0]):
							#sh = (pnt[1]-c[i][1]+ (slope * c[i][0]))/slope
						#else: 
							#sh = 0
				#Check point
				#tsegiin x ees ih ogtoltsliin tsegiig shalgah
				if(sh >= pnt[0]): 
					if(c[i][1] == pnt[1]):
						if(c[i][1] == c[i+1][1]):
							d.append('o')
							d.append('o')
						if(c[i][1] < c[i-1][1]):
							d.append('u')
							d.append('o')
						if(c[i][1] < c[i+1][1]):
							d.append('o')
							d.append('u')
						if(c[i][1] > c[i-1][1]):
							d.append('d')
							d.append('o')
						if(c[i][1] > c[i+1][1]):
							d.append('o')
							d.append('d')
				
					if(c[i][1] > pnt[1] and c[i+1][1] < pnt[1]):
						d.append('u')
						d.append('d')
					if(c[i][1] < pnt[1] and c[i+1][1] > pnt[1]):	
						d.append('d')
						d.append('u')
		d=[x for x in d if x != 'o']
		for i in range(len(d)-2):
			if(d[i] == d[i+1]):
				d.remove(d[i])
		print(d)
		if(len(d) % 2 == 0):
			return "inside"
		else:
			return "outside"

olon('pg1.json')
