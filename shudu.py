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
				c[int(x/3)+int(y/3)*3][x%3+(y%3)*3] = i
				if x == 8 and y == 8:
					return a
				t = shudu(x,y,a,b,c)
				if t:
					return t
		a[x][y] = 0
		b[y][x] = 0
		c[int(x/3)+int(y/3)*3][x%3+(y%3)*3] = 0
		return False

	a = [[0]*9 for i in range(9)]
	b = [[0]*9 for i in range(9)]
	c = [[0]*9 for i in range(9)]
	r = shudu(-1,0,a,b,c)	
	return r

def shudu1():
	a = [[0]*9 for i in range(9)]
	b = [[0]*9 for i in range(9)]
	c = [[0]*9 for i in range(9)]
	d = [[[]]*9 for i in range(9)]
	x = 0
	y = 0
	n = 0
	while True:
		n = d[x][y]
		r = list({1,2,3,4,5,6,7,8,9}-set(n))
		random.shuffle(r)
		for i in r:
			n.append(i)
			if i in a[x] or i in b[y] or i in c[int(x/3)+int(y/3)*3]:
				continue
			else:
				a[x][y] = i
				b[y][x] = i
				c[int(x/3)+int(y/3)*3][x%3+(y%3)*3] = i
				d[x][y] = n
				break
		
		if x == 8 and y == 8:
			return a

		if a[x][y] == 0:
			d[x][y] = []
			if x == 0:
				x = 8
				y -= 1
			else:
				x -= 1
			a[x][y] = 0
			b[y][x] = 0
			c[int(x/3)+int(y/3)*3][x%3+(y%3)*3] = 0
		else:
			if x == 8:
				x = 0
				y += 1
			else:
				x += 1

def zuo_jie_shudu():
	# a = sheng_shudu()
	a = shudu1()
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
				c[int(x/3)+int(y/3)*3][x%3+(y%3)*3] = i
				if x == 8 and y == 8:
					return a
				t = shudu(x,y,a,b,c)
				if t:
					return t
		a[x][y] = 0
		b[y][x] = 0
		c[int(x/3)+int(y/3)*3][x%3+(y%3)*3] = 0
		return False

	a = [[0]*9 for i in range(9)]
	b = [[0]*9 for i in range(9)]
	c = [[0]*9 for i in range(9)]
	for i in range(8):
		for i1 in range(8):
			a[i][i1] = jie[i][i1]
			b[i1][i] = jie[i][i1]
			c[int(i/3)+int(i1/3)*3][i%3+(i1%3)*3] = jie[i][i1]


	r = shudu(-1,0,a,b,c)	
	return r

def jie_shudu1(timu):
	global YY
	a = [[0]*9 for i in range(9)]
	b = [[0]*9 for i in range(9)]
	c = [[0]*9 for i in range(9)]
	d = [[[]]*9 for i in range(9)]
	for i in range(8):
		for i1 in range(8):
			a[i][i1] = timu[i][i1]
			b[i1][i] = timu[i][i1]
			c[int(i/3)+int(i1/3)*3][i%3+(i1%3)*3] = timu[i][i1]
	x = 0
	y = 0
	n = 0
	while True:
		YY += 1
		if a[x][y] == 0:
			pass
		else:
			if x == 8:
				x = 0
				y += 1
			else:
				x += 1
			continue
		n = d[x][y]
		r = list({1,2,3,4,5,6,7,8,9}-set(n))
		for i in r:
			n.append(i)
			if i in a[x] or i in b[y] or i in c[int(x/3)+int(y/3)*3]:
				continue
			else:
				a[x][y] = i
				b[y][x] = i
				c[int(x/3)+int(y/3)*3][x%3+(y%3)*3] = i
				d[x][y] = n
				break
		
		if x == 8 and y == 8:
			print('D:')
			for i in d:
				print(i)
			print()
			return a

		if a[x][y] == 0:
			d[x][y] = []
			if x == 0:
				x = 8
				y -= 1
			else:
				x -= 1
			while timu[x][y] != 0:
				if x == 0:
					x = 8
					y -= 1
				else:
					x -= 1
			a[x][y] = 0
			b[y][x] = 0
			c[int(x/3)+int(y/3)*3][x%3+(y%3)*3] = 0
		else:
			if x == 8:
				x = 0
				y += 1
			else:
				x += 1


def ma():
	ti = zuo_jie_shudu()
	jie = jie_shudu1(ti)
	for i in ti:
		print(i)
	print()
	for i in jie:
		print(i)
	print(YY)

if __name__ == '__main__':
	ma()

	# ans = shudu1()
	# for i in ans:
		# for i1 in i:
			# print(i1)
		# print()