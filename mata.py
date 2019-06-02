import copy,time

POSALL = [[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2]]
N = 0
def mata(a,x,y,i=1):
	global N
	N += 1
	# a = a1[:]
	# a = copy.deepcopy(a1)
	# if (x,y) in a:
	# 	return False
	# else:
	# 	a.append((x,y))
	# for i1 in a:
		# print(i1)
	# print()
	# time.sleep(0.1)
	if a[x][y] == 0:
		a[x][y] = i
	else:
		return False
		# print(a)
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
# a = []
a = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
x = 7
y = 4
ti = time.time()
print(mata(a,x,y))
print(time.time()-ti,N)
