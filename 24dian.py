
SCORE = 24

NOTHIS = -10000

def cal_24(a,b,c,d):

	def cal(num1,num2,fu):
		if fu == 1:
			return num1+num2
		elif fu == 2:
			return num1-num2
		elif fu == 3:
			return num1*num2
		elif fu == 4:
			if num2 != 0 and num1%num2 == 0:
				return num1/num2
		elif fu == 5:
			if num1 != 0 and num2%num1 == 0 and num1 != 1:
				return num2/num1
		return NOTHIS

	def printans(ans):
		# print('in')
		def getfu(fu):
			if fu == 1:
				return '+'
			elif fu == 2:
				return '-'
			elif fu == 3:
				return '*'
			elif fu == 4:
				return '/'
			else:
				return']'
		n = ans[0]
		f = ans[1]
		# print(n,f)

		if len(f) == 3:
			a = ['%s' % n[0], getfu(f[0]), '%s' % n[1], getfu(f[1]), '%s' % n[2], getfu(f[2]), '%s' % n[3]]
			# a = '%s' % n[0]
			# a += getfu(f[0])
			# a += '%s' % n[1]
			# a += getfu(f[1])
			# a += '%s' % n[2]
			# a += getfu(f[2])
			# a += '%s' % n[3]
			if f[0] == 1 or f[0] == 2:
				if f[1] == 3 or f[1] == 4 or f[1] == 5:
					a.insert(0,'(')
					a.insert(4,')')

			if f[1] == 1 or f[1] == 2:
				if f[2] == 3 or f[2] == 4 or f[2] == 5:
					a.insert(0,'(')
					a.insert(6,')')
			for i in a:
				if i == ']':
					l = a.index('(')
					r = a.index(')')
					a.reverse()
					# a = a[r+2:]+'/'+a[l:r+1]
					break

		else:
			a = ['(', '%s'%n[0], getfu(f[0]), '%s'%n[1], ')', getfu(ans[2]), '(', '%s'%n[2], getfu(f[1]), '%s'%n[3], ')']
			# a = '('
			# a += '%s' % n[0]
			# a += getfu(f[0])
			# a += '%s' % n[1]
			# a += ')'
			# a += getfu(ans[2])
			# a += '('
			# a += '%s' % n[2]
			# a += getfu(f[1])
			# a += '%s' % n[3]
			# a += ')'
		print(''.join(a))

	def printans2(ans):
		def getfu(fu):
			if fu == '1':
				return '+'
			elif fu == '2':
				return '-'
			elif fu == '3':
				return '*'
			elif fu == '4':
				return '/'
			else:
				return']'
		n = []
		f = []
		if len(ans) == 4:
			for i in ans:
				n.append(i[1:])
				f.append(i[:1])
			f.pop(0)
		else:
			for i in range(4):
				n.append(ans[i][1:])
				f.append(ans[i][:1])
			
			f.pop(2)
			f.pop(0)
			midf = ans[4]
		if len(f) == 3:
			a = [n[0], getfu(f[0]), n[1], getfu(f[1]), n[2], getfu(f[2]), n[3]]
			if f[0] == '1' or f[0] == '2':
				if f[1] == '3' or f[1] == '4' or f[1] == '5':
					a.insert(0,'(')
					a.insert(4,')')

			if f[1] == '1' or f[1] == '2':
				if f[2] == '3' or f[2] == '4' or f[2] == '5':
					a.insert(0,'(')
					a.insert(6,')')
			# for i in a:
			# 	if i == ']':
			# 		l = a.index('(')
			# 		r = a.index(')')
			# 		a.reverse()
			# 		break

		else:
			a = ['(', n[0], getfu(f[0]), n[1], ')', getfu(midf), '(', n[2], getfu(f[1]), n[3], ')']

		print(''.join(a))

	def switch(l,index1,index2):
		l.insert(index2+1,l[index1])
		l.insert(index1+1,l[index2])
		l.pop(index1)
		l.pop(index2)
		return l

	def kill_same(ans):
		flist = []
		for i in ans:
			if not i in flist:
				flist.append(i)
		# print(flist)
		key = []
		for i in flist:
			n = i[0][:]
			f = i[1][:]
			if len(f) == 3:
				f.insert(0,1)
				a = []
				for i1 in range(4):
					a.append(('%s'%f[i1]+'%s'%n[i1]))
				a.sort()
				if not a in key:
					key.append(i)
			elif len(f) == 2:
				a = []
				f.insert(2,1)
				f.insert(0,1)
				for i1 in range(4):
					a.append(('%s'%f[i1]+'%s'%n[i1]))
				a.append('%s'%i[2])
				a.sort()
				if not a in key:
					key.append(i)
		# print(key)
		print(flist)
		for i in key:
			flist.pop(flist.index(i))
		print(flist)
		return key

	ans = []
	nums = [[a, b, c, d], [a, b, d, c], [a, c, b, d], [a, c, d, b], [a, d, b, c], [a, d, c, b], [b, a, c, d], [b, a, d, c], [b, c, a, d], [b, c, d, a], [b, d, a, c], [b, d, c, a], [c, a, b, d], [c, a, d, b], [c, b, a, d], [c, b, d, a], [c, d, a, b], [c, d, b, a], [d, a, b, c], [d, a, c, b], [d, b, a, c], [d, b, c, a], [d, c, a, b], [d, c, b, a]]
	# fus = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 3, 1], [1, 3, 2], [1, 3, 3], [1, 3, 4], [1, 4, 1], [1, 4, 2], [1, 4, 3], [1, 4, 4], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 1, 4], [2, 2, 1], [2, 2, 2], [2, 2, 3], [2, 2, 4], [2, 3, 1], [2, 3, 2], [2, 3, 3], [2, 3, 4], [2, 4, 1], [2, 4, 2], [2, 4, 3], [2, 4, 4], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 1, 4], [3, 2, 1], [3, 2, 2], [3, 2, 3], [3, 2, 4], [3, 3, 1], [3, 3, 2], [3, 3, 3], [3, 3, 4], [3, 4, 1], [3, 4, 2], [3, 4, 3], [3, 4, 4], [4, 1, 1], [4, 1, 2], [4, 1, 3], [4, 1, 4], [4, 2, 1], [4, 2, 2], [4, 2, 3], [4, 2, 4], [4, 3, 1], [4, 3, 2], [4, 3, 3], [4, 3, 4], [4, 4, 1], [4, 4, 2], [4, 4, 3], [4, 4, 4]]
	fus = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 1, 5], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 1], [1, 3, 2], [1, 3, 3], [1, 3, 4], [1, 3, 5], [1, 4, 1], [1, 4, 2], [1, 4, 3], [1, 4, 4], [1, 4, 5], [1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 5], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 1, 4], [2, 1, 5], [2, 2, 1], [2, 2, 2], [2, 2, 3], [2, 2, 4], [2, 2, 5], [2, 3, 1], [2, 3, 2], [2, 3, 3], [2, 3, 4], [2, 3, 5], [2, 4, 1], [2, 4, 2], [2, 4, 3], [2, 4, 4], [2, 4, 5], [2, 5, 1], [2, 5, 2], [2, 5, 3], [2, 5, 4], [2, 5, 5], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 1, 4], [3, 1, 5], [3, 2, 1], [3, 2, 2], [3, 2, 3], [3, 2, 4], [3, 2, 5], [3, 3, 1], [3, 3, 2], [3, 3, 3], [3, 3, 4], [3, 3, 5], [3, 4, 1], [3, 4, 2], [3, 4, 3], [3, 4, 4], [3, 4, 5], [3, 5, 1], [3, 5, 2], [3, 5, 3], [3, 5, 4], [3, 5, 5], [4, 1, 1], [4, 1, 2], [4, 1, 3], [4, 1, 4], [4, 1, 5], [4, 2, 1], [4, 2, 2], [4, 2, 3], [4, 2, 4], [4, 2, 5], [4, 3, 1], [4, 3, 2], [4, 3, 3], [4, 3, 4], [4, 3, 5], [4, 4, 1], [4, 4, 2], [4, 4, 3], [4, 4, 4], [4, 4, 5], [4, 5, 1], [4, 5, 2], [4, 5, 3], [4, 5, 4], [4, 5, 5], [5, 1, 1], [5, 1, 2], [5, 1, 3], [5, 1, 4], [5, 1, 5], [5, 2, 1], [5, 2, 2], [5, 2, 3], [5, 2, 4], [5, 2, 5], [5, 3, 1], [5, 3, 2], [5, 3, 3], [5, 3, 4], [5, 3, 5], [5, 4, 1], [5, 4, 2], [5, 4, 3], [5, 4, 4], [5, 4, 5], [5, 5, 1], [5, 5, 2], [5, 5, 3], [5, 5, 4], [5, 5, 5]]
	for i in nums:
		for i1 in fus:
			a1 = cal(i[0],i[1],i1[0])
			if a1 == NOTHIS:
				continue
			a2 = cal(a1,i[2],i1[1])
			if a2 == NOTHIS:
				continue
			a3 = cal(a2,i[3],i1[2])
			if a3 == SCORE:
				ans.append([i,i1])
	
	fus1 = [[1, 1], [1, 2], [2, 1], [2, 2]]
	for i in nums:
		for ix in range(2):
			for i1 in fus1:
				a1 = cal(i[0],i[1],i1[0])
				if a1 == NOTHIS:
					continue
				a2 = cal(i[2],i[3],i1[1])
				if a2 == NOTHIS:
					continue
				a3 = cal(a1,a2,ix+2)
				if a3 == SCORE:
					ans.append([i,i1,ix+2])
	print(ans,'ans')
	ans = kill_same(ans)
	print(ans,'ans"')
	for i in ans:
		printans(i)
		# printans2(i)

	
if __name__ == '__main__':
	cal_24(1,1,1,72)
