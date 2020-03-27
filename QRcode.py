
from PIL import Image,ImageDraw
import time
import math
t0 = time.time()

file = 'QRcode1.jpeg'

im = Image.open(file).rotate(180)
li = []

def change_to_bw(im):
	data = im.getdata()
	size = im.size
	weight = size[0]
	height = size[1]

	for i in range(len(data)):
		py = int(i/weight)
		px = i-(weight*py)

		r,g,b = data[i]

		if (r+g+b) > 500:
			im.putpixel((px,py),(255,255,255))
		else:
			im.putpixel((px,py),(0,0,0))

def move_x(data,width,i,num=1):
	black = (0,0,0)
	if num > 0:
		move = 1
	else:
		move = -1
	r = 0
	while True:
		if data[i] == black:
			r += 1
		else:
			return r
		i += 1
		if i % width == 0:
			return r


def move_y(data,width,i,num=1):
	black = (0,0,0)
	l = len(data)
	if num >= 0:
		move = 1
	else:
		move = -1
	r = 0
	# print(i)
	while True:
		
		if data[i] == black:
			r += 1
		else:
			return r
		
		i += width
		if i > l-1:
			return r

def checkpositon(data,width,i,movex,movey,draw):
	return True
	l = len(data)
	py = int(i/width)
	px = i-(width*py)
	xindex = i+movex-1
	yindex = i+width*(movey-1)
	k = 0
	while True:
		if data[i] == black:
			m = move_x(data,width,xindex)

			if movex > (m*0.8) and movex < (m*1.2):
				newx = move_x(data,weight,i+m)
				newy = move_y(data,weight,i+m)
				if movex > (newx*0.8) and movex < (newx*1.2) and movey > (newy*0.8) and movey < (newy*1.2):
					drawim.line([(newx,newy),(newx+100,newy+100)],(100,100,100))
					k += 1
					break

		xindex += 1
		if xindex % width == 0:
			break

	# while True:
	# 	if data[i] == black:
	# 		m = move_y(data,width,xindex)

	# 		if movey > (m*0.8) and movey < (m*1.2):
	# 			newy = move_y(data,weight,i+movex-1)
	# 			newx = move_x(data,weight,i+(movey-1)*weight)
	# 			if movex > (newx*0.8) and movex < (newx*1.2) and movey > (newy*0.8) and movey < (newy*1.2):
	# 				drawim.line([(newx,newy),(newx+100,newy+100)],(100,100,100))
	# 				k += 1
	# 				break

	# 	yindex += width
	# 	if yindex % width == 0:
	# 		break

	return k

def decode(li):
	def checkall(li,num,begin,end):
		for i in range(begin,end+1):
			if li[i] == num:
				pass
			else:
				return False
		return True
	def fang(num,k):
		r = 1
		for i in range(k):
			r *= num
		return r

	def get_yanma(y):
		pass


	a = len(li)
	data = []
	for i in li:
		data.append(i[:])
	k = 0
	if not checkall(data,1,0,7):
		pass
	elif not checkall(data,1,a-8,a-1):
		pass
	elif not checkall(data,1,a*(a-1),a*(a-1)+7):
		pass
	elif not checkall(data,1,a*a-8,a*a-1):
		pass

	lyanma = li[8][2:5]
	yanma = 0
	for i in range(3):
		yanma += fang(2,2-i)*lyanma[i]



change_to_bw(im)


black = (0,0,0)
white = (255,255,255)

size = im.size
weight = size[0]
height = size[1]

data = im.getdata()
i = 0
py = int(i/weight)
px = i-(weight*py)

lidata = list(data)

width = 0



for i in range(len(data)):

	if data[i] == black:
		movex = move_x(data,weight,i)
		# midmove = int(movex/2)
		# midy = move_y(data,weight,i+midmove-1)
		if not movex > 35:
			continue
		# print(midy)
		movey = move_y(data,weight,i)


		if movex > (movey*0.8) and movex < (movey*1.2):
			newi = i+movex
			newx = move_x(data,weight,i+(movey-1)*weight)
			newy = move_y(data,weight,i+movex-1)
			if movex > (newx*0.8) and movex < (newx*1.2) and movey > (newy*0.8) and movey < (newy*1.2):
				pass
			else:
				# print(movex,movey,newy,i)
				continue


			print('hi',movex,movey)
		
			drawim = ImageDraw.Draw(im)
			
			py = int(i/weight)
			px = i-(weight*py)
			# xie = math.sqrt(px*px+py*py)

			drawim.line([(px,py),(px+movex,py+movey)],(100,100,100))
			px += movex
			# drawim.line([(px,py),(px,py)],(100,100,100))
			px -= movex

			newpy = py+newy
			newpx = px+newx
			
			# drawim.line([(newpx,newpy),(newpx+100,newpy+100)],(255,100,100),5)
			
			print(newpx,newpy,px,py,i)
			# px += movex
			# drawim.line([(px,py),(px+100,py+100)],(100,100,100))

			if checkpositon(data,weight,i,movex,movey,drawim):
				li.append([px,py,newpx,newpy])

if len(li) == 3:
	pass
else:
	li.pop(-1)
# print(li)

disx = []
disy = []

# for i in li:
# 	disx.append(i[2]-i[0])
# 	disy.append(i[3]-i[1])

# lastnum = disx[0]
# k = 0
# group = [li[0]]
# for i in range(1,len(disx)):
# 	if abs(disx[0]-lastnum) < 5:
# 		k += 1
# 		group.append(li[i])
# 	else:
# 		k = 0
group = li[:]
print(group)
print(disx,disy)



# ppery = (group[0][3]-group[0][1])/7


allx = []
ally = []
for i in group:
	allx.append(i[0])
	allx.append(i[2])
	ally.append(i[1])
	ally.append(i[3])
minx = min(allx)
maxx = max(allx)
miny = min(ally)
maxy = max(ally)

aQRcode = int((maxx-minx)*7/(group[0][2]-group[0][0]))
#####correct a
v = round((aQRcode-21)/4)
aQRcode = v*4+21

pperx = (maxx-minx)/aQRcode
ppery = (maxy-miny)/aQRcode
print(maxx-minx,maxy-miny,pperx,ppery,aQRcode)

QRwidth = maxx-minx
QRheight = maxy-miny
# for i in range(QRwidth * QRheight):
QRlist = [[]]

i = minx+miny*weight
k = 0
hk = 0
heightk = 0
addyl = []


l = len(data)
while True:

	# if (i%weight) > maxx:
	if len(QRlist[-1]) >= 25:
		# if int(i/weight) >= maxy:
		if len(QRlist) >= 25:
			# QRlist.pop(-1)
			# QRlist.pop(-1)
			break
		
		# QRlist[-1].pop(-1)
		QRlist.append([])

		addy = int(int(heightk*ppery)-int((heightk-1)*(ppery)))
		heightk += 1
		
		addyl.append(addy)
		i = (int(i/weight)+addy)*weight+minx
		# print(' ')
		

		
		# print('\n')
		k = 0
		# break
		# print(QRlist)

	b = 0
	w = 0
	nowpx = int(int(k*pperx)-int((k-1)*(pperx)))
	nowpy = int(int(k*ppery)-int((k-1)*(ppery)))

	py = int(i/weight)
	px = i-(weight*py)
	
	# print(nowpy)

	if heightk%2 == 1:
		color = (255,100,100)
	else:
		color = (100,100,255)

	drawim.line([(px,py),(px+nowpx,py+nowpy)],color,3)

	# print(nowpx,nowpy,k)
	for ix in range(nowpx):
		for iy in range(nowpy):
			index = i+ix+iy*weight
			if index >= l:
				w += 1
				print(index,l)
			else:	
				if data[index] == black:
					b += 1
				else:
					w += 1
	if b >= w:
		QRlist[-1].append(1)
	else:
		QRlist[-1].append(0)
	k += 1
	i += nowpy
	# print(i,int(i/weight),maxy)
	# break


ans = decode(QRlist)


for x in QRlist:
	print(x)
print(len(QRlist))
print(len(QRlist[0]))
print('has got list')
# print(addyl)
# print(QRlist)

# im.show()
im.save('caogao.png')

# print(ans)

t1 = time.time()
print(t1-t0)
