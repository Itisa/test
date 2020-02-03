
SCORE = 24

NOTHIS = -10000

def cal_24main(a,b,c,d):

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

	def cal_24(nums,fus):
		a1 = cal(i[0],i[1],i1[0])
		if a1 == NOTHIS or i1[0]==5:
			return False
		a2 = cal(a1,i[2],i1[1])
		if a2 == NOTHIS:
			return False
		a3 = cal(a2,i[3],i1[2])
		if a3 == SCORE:
			return True

			
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

		if 5 in f:
			a = ['%s' % n[0], getfu(f[0]), '%s' % n[1], getfu(f[1]), '%s' % n[2], getfu(f[2]), '%s' % n[3]]
			nex = f.index(5)+1
			a.insert(0,'%s'%n[nex])
			a.pop(nex+2)
			a.pop(nex+2)
			a.insert(1,'(')
			a.insert(nex+3,')')
			a.insert(1,'/')



		elif f[2]>0:
			a = ['%s' % n[0], getfu(f[0]), '%s' % n[1], getfu(f[1]), '%s' % n[2], getfu(f[2]), '%s' % n[3]]

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
					break

		elif f[2]<0:
			a = ['(', '%s'%n[0], getfu(f[0]), '%s'%n[1], ')', getfu(f[2]+4), '(', '%s'%n[2], getfu(f[1]), '%s'%n[3], ')']
		else:
			print('f[2]error')
		return ''.join(a)
		# print(''.join(a))

	def switch(l,index1,index2):
		l.insert(index2+1,l[index1])
		l.insert(index1+1,l[index2])
		l.pop(index1)
		l.pop(index2)
		return l

	def combine(a,b):
		if len(a) != len(b):
			print('error')
		else:
			z = []
			for i in range(len(a)):
				z.append('%s'%a[i]+'%s'%b[i])
			return z

	def split(a):
		z = []
		for i in range(len(a[0])):
			z.append([])
		for i in a:
			for i1 in range(len(z)):
				z[i1].append(int(i[i1]))
		return z
	
	def kill_same(ans):
		flist1 = []
		flist2 = []
		for i in ans:
			if i in flist1 or i in flist2:
				pass
			else:
				if i[1][2]>0:
					flist1.append(i[:])
				else:
					flist2.append(i[:])
		# print(flist)
		key1 = []
		index1 = []
		for i in flist1:
			# print(i)

			n = i[0][:]
			f = i[1][:]
			f.insert(0,1)
			
			mykey = combine(n,f)
			for i1 in range(len(mykey)):
				if mykey[i1][0] == '1' and mykey[i1][1] == '4':
					mykey[i1] = '13'
			mykey.sort()
			
			if mykey in key1:
				continue
			else:
				key1.append(mykey)
				index1.append(flist1.index(i))
			# s = split(mykey)
			# print(s)


		f1 = []
		for i in index1:
			f1.append(flist1[i])
		pindex1=[]
		pf = []
		for i in range(len(f1)):
			for i1 in range(len(f1)):
				if f1[i1][1] == f1[i][1] and i1!=i:
					if not f1[i1][1] in pf:
						pf.append(f1[i1][1][:])
						# print(i,i1)
						pindex1.append(i)
						continue
		pindex1.reverse()
		# print(pindex1)
		# print(f1)
		for i in pindex1:
			f1.pop(i)
		
		######################################################
		key2 = []
		index2 = []
		for i in flist2:
			# print(i)

			n = i[0][:]
			f = i[1][:]
			# print(n,f)
			f.insert(1,1)
			f.insert(0,1)
			f.pop(-1)
			for i1 in flist2:
				if i[1] == i1[1]:
					continue
			
			mykey = combine(n,f)
			for i1 in range(len(mykey)):
				if mykey[i1][0] == '1' and mykey[i1][1] == '4':
					mykey[i1] = '13'
			# print(mykey)
			mykey.sort()
			
			if mykey in key2:
				continue
			else:
				key2.append(mykey)
				index2.append(flist2.index(i))
		f2 = []
		for i in index2:
			f2.append(flist2[i])
		# print(f1)
		# print(f2)


		flist = f1[:]
		for i in f2:
			flist.append(i)


		return flist




	ans = []
	nums = [[a, b, c, d], [a, b, d, c], [a, c, b, d], [a, c, d, b], [a, d, b, c], [a, d, c, b], [b, a, c, d], [b, a, d, c], [b, c, a, d], [b, c, d, a], [b, d, a, c], [b, d, c, a], [c, a, b, d], [c, a, d, b], [c, b, a, d], [c, b, d, a], [c, d, a, b], [c, d, b, a], [d, a, b, c], [d, a, c, b], [d, b, a, c], [d, b, c, a], [d, c, a, b], [d, c, b, a]]
	# fus = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 3, 1], [1, 3, 2], [1, 3, 3], [1, 3, 4], [1, 4, 1], [1, 4, 2], [1, 4, 3], [1, 4, 4], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 1, 4], [2, 2, 1], [2, 2, 2], [2, 2, 3], [2, 2, 4], [2, 3, 1], [2, 3, 2], [2, 3, 3], [2, 3, 4], [2, 4, 1], [2, 4, 2], [2, 4, 3], [2, 4, 4], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 1, 4], [3, 2, 1], [3, 2, 2], [3, 2, 3], [3, 2, 4], [3, 3, 1], [3, 3, 2], [3, 3, 3], [3, 3, 4], [3, 4, 1], [3, 4, 2], [3, 4, 3], [3, 4, 4], [4, 1, 1], [4, 1, 2], [4, 1, 3], [4, 1, 4], [4, 2, 1], [4, 2, 2], [4, 2, 3], [4, 2, 4], [4, 3, 1], [4, 3, 2], [4, 3, 3], [4, 3, 4], [4, 4, 1], [4, 4, 2], [4, 4, 3], [4, 4, 4]]
	fus = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 1, 5], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 1], [1, 3, 2], [1, 3, 3], [1, 3, 4], [1, 3, 5], [1, 4, 1], [1, 4, 2], [1, 4, 3], [1, 4, 4], [1, 4, 5], [1, 5, 1], [1, 5, 2], [1, 5, 3], [1, 5, 4], [1, 5, 5], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 1, 4], [2, 1, 5], [2, 2, 1], [2, 2, 2], [2, 2, 3], [2, 2, 4], [2, 2, 5], [2, 3, 1], [2, 3, 2], [2, 3, 3], [2, 3, 4], [2, 3, 5], [2, 4, 1], [2, 4, 2], [2, 4, 3], [2, 4, 4], [2, 4, 5], [2, 5, 1], [2, 5, 2], [2, 5, 3], [2, 5, 4], [2, 5, 5], [3, 1, 1], [3, 1, 2], [3, 1, 3], [3, 1, 4], [3, 1, 5], [3, 2, 1], [3, 2, 2], [3, 2, 3], [3, 2, 4], [3, 2, 5], [3, 3, 1], [3, 3, 2], [3, 3, 3], [3, 3, 4], [3, 3, 5], [3, 4, 1], [3, 4, 2], [3, 4, 3], [3, 4, 4], [3, 4, 5], [3, 5, 1], [3, 5, 2], [3, 5, 3], [3, 5, 4], [3, 5, 5], [4, 1, 1], [4, 1, 2], [4, 1, 3], [4, 1, 4], [4, 1, 5], [4, 2, 1], [4, 2, 2], [4, 2, 3], [4, 2, 4], [4, 2, 5], [4, 3, 1], [4, 3, 2], [4, 3, 3], [4, 3, 4], [4, 3, 5], [4, 4, 1], [4, 4, 2], [4, 4, 3], [4, 4, 4], [4, 4, 5], [4, 5, 1], [4, 5, 2], [4, 5, 3], [4, 5, 4], [4, 5, 5], [5, 1, 1], [5, 1, 2], [5, 1, 3], [5, 1, 4], [5, 1, 5], [5, 2, 1], [5, 2, 2], [5, 2, 3], [5, 2, 4], [5, 2, 5], [5, 3, 1], [5, 3, 2], [5, 3, 3], [5, 3, 4], [5, 3, 5], [5, 4, 1], [5, 4, 2], [5, 4, 3], [5, 4, 4], [5, 4, 5], [5, 5, 1], [5, 5, 2], [5, 5, 3], [5, 5, 4], [5, 5, 5]]
	for i in nums:
		for i1 in fus:
			if cal_24(i,i1):
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
					i1.append(ix-2)
					if len(i1) >= 4:
						continue
					ans.append([i,i1[:]])
				#ix 0,1
				# -2*,-1/

	# print(ans,'ans')
	ans = kill_same(ans)
	print(len(ans))
	# print(ans,'ans"')
	pans = []
	for i in ans:
		p = printans(i)
		pans.append(p)
		print(p)
	return pans
	
if __name__ == '__main__':
	cal_24main(1,5,2,7)
