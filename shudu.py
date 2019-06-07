import random
YY = 0

def sheng_shudu():

	def shudu(x,y,a,b,c):
		if x == 8:
			x = 0
			y += 1
		else:
			x += 1
		n = [1,2,3,4,5,6,7,8,9]
		random.shuffle(n)
		for i in n:
			if i in a[x] or i in b[y] or i in c[int(x/3)+int(y/3)*3]:
				continue
			else:
				a[x][y] = i
				b[y][x] = i
				c[int(x/3)+int(y/3)*3][x-int(x/3)*3+(y-int(y/3)*3)*3] = i
				if x == 8 and y == 8:
					return a
				t = shudu(x,y,a,b,c)
				if t:
					return t
		a[x][y] = 0
		b[y][x] = 0
		c[int(x/3)+int(y/3)*3][x-int(x/3)*3+(y-int(y/3)*3)*3] = 0
		return False

	a = [[0]*9 for i in range(9)]
	b = [[0]*9 for i in range(9)]
	c = [[0]*9 for i in range(9)]
	r = shudu(-1,0,a,b,c)	
	return r


def zuo_jie_shudu():
	a = sheng_shudu()
	for i in a:
		print(i)
	print()
	n = list(range(81))
	random.shuffle(n)
	for i in range(random.randint(60,60)):
		a[int(n[i]/9)][n[i]%9] = 0
	return a

def jie_shudu(jie):
	def shudu(x,y,a,b,c):
		global YY
		YY += 1
		if x == 8:
			x = 0
			y += 1
		else:
			x += 1
		if a[x][y] != 0:
			return(shudu(x,y,a,b,c))

		n = list({1,2,3,4,5,6,7,8,9}-set(a[x])-set(b[y])-set(c[int(x/3)+int(y/3)*3]))
		for i in n:
			if i in a[x] or i in b[y] or i in c[int(x/3)+int(y/3)*3]:
				continue
			else:
				a[x][y] = i
				b[y][x] = i
				c[int(x/3)+int(y/3)*3][x-int(x/3)*3+(y-int(y/3)*3)*3] = i
				if x == 8 and y == 8:
					return a
				t = shudu(x,y,a,b,c)
				if t:
					return t
		a[x][y] = 0
		b[y][x] = 0
		c[int(x/3)+int(y/3)*3][x-int(x/3)*3+(y-int(y/3)*3)*3] = 0
		return False

	a = [[0]*9 for i in range(9)]
	b = [[0]*9 for i in range(9)]
	c = [[0]*9 for i in range(9)]
	for i in range(8):
		for i1 in range(8):
			a[i][i1] = jie[i][i1]
			b[i1][i] = jie[i][i1]
			c[int(i/3)+int(i1/3)*3][i-int(i/3)*3+(i1-int(i1/3)*3)*3] = jie[i][i1]


	r = shudu(-1,0,a,b,c)	
	return r

def ma():
	ti = zuo_jie_shudu()
	jie = jie_shudu(ti)
	for i in ti:
		print(i)
	print()
	for i in jie:
		print(i)
	print(YY)

if __name__ == '__main__':
	ma()
