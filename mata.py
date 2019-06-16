import copy,time
# import pyqt

POSALL = [[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2]]
N = 0
def mata(a,x,y,i=1):
	global N
	N += 1
	if a[x][y] == 0:
		a[x][y] = i
	else:
		return False
	if i == 64:
		return a
	# for x1,y1 in POSALL:
	# 	if x+x1<8 and x+x1>-1 and y+y1<8 and y+y1>-1:
	# 		t = mata(a,x+x1,y+y1,i+1)
	# 		if t:
	# 			return t
	if x-1>=0 and y+2<8:
		t = mata(a,x-1,y+2,i+1)
		if t:
			return t
	if x-2>=0 and y+1<8:
		t = mata(a,x-2,y+1,i+1)
		if t:
			return t
	if x-2>=0 and y-1>=0:
		t = mata(a,x-2,y-1,i+1)
		if t:
			return t
	if x-1>=0 and y-2>=0:
		t = mata(a,x-1,y-2,i+1)
		if t:
			return t
	if x+1<8 and y-2>=0:
		t = mata(a,x+1,y-2,i+1)
		if t:
			return t
	if x+2<8 and y-1>=0:
		t = mata(a,x+2,y-1,i+1)
		if t:
			return t
	if x+2<8 and y+1<8:
		t = mata(a,x+2,y+1,i+1)
		if t:
			return t
	if x+1<8 and y+2<8:
		t = mata(a,x+1,y+2,i+1)
		if t:
			return t
	a[x][y] = 0
	return False

def mata_fdd():
	a = [[0]*8 for i in range(8)]
	b = [[0]*8 for i in range(8)]
	x = 0
	y = 0
	POSALL = [[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2]]
	i = 0
	i1 = 0
	x1 = 0
	y1 = 0
	while i <= 63:
		x += x1
		y += y1
		# print(i,x,y,x1,y1,b[x][y])
		n = b[x][y]
		
		for x1,y1 in POSALL[b[x][y]:]:
			n += 1
			if x+x1<8 and x+x1>-1 and y+y1<8 and y+y1>-1:
				if a[x+x1][y+y1] != 0:
					continue
				else:
					i += 1
					a[x+x1][y+y1] = i
					b[x+x1][y+y1] = n
					for i2 in a:
						print(i2)
					print()
					# print(i,b[x+x1][y+y1])
					break
		if a[x+x1][y+y1] == 0:
			i -= 1
			# a[x][y] = 0
			b[x][y] = 0
			x1 = -x1
			y1 = -y1

ti = time.time()
print(mata_fdd())
print(time.time()-ti,N)
