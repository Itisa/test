
NOT_INIT = -1

v = [1,2,3,4,5,6]
e = []


dic = {}
dic['e1e2'] = 1
dic['e1e3'] = 4
dic['e2e3'] = 6
dic['e2e4'] = 7
dic['e2e5'] = 5
dic['e3e5'] = 1
dic['e4e5'] = 3
dic['e4e6'] = 2
dic['e5e6'] = 5

g = [v,dic]
start = 1
end = 6
now = start
s1 = [start]
s2 = v
s2.pop(s2.index(start))
nex = start
alllength = 0
slength = [0]

nex = start

while True:
	nnex = nex
	nownex = 'e%s'%nnex
	shortest = NOT_INIT
	nex = NOT_INIT	

	# find the nearest point
	# print(s1,s2)
	for i in s2:
		# print('asbv',i,)
		if i < nnex:
			key = 'e%s'%i + nownex
		else:
			key = nownex + 'e%s'%i
		# print(key)
		if key in dic:
			# print(dic[key],123)
			if shortest == NOT_INIT:
				shortest = dic[key]
				nex = i
				# print(shortest,nex)
			else:
				if shortest > dic[key]:
					shortest = dic[key]
					nex = i
	if nex == NOT_INIT:
		print('error')
	# print(nex,'nex')
	# check if the nearest
	nownex = 'e%s'%nex
	lastlength = slength[-1]
	newshort = NOT_INIT
	# print(nownex,'nownext')
	for i in range(len(s1)):
		if s1[i] < nex:
			key = 'e%s'%s1[i] + nownex
		else:
			key = nownex + 'e%s'%s1[i]
		# print(key,'key',i,s1)
		if key in dic:
			nowdis = shortest + lastlength - slength[i]
			dis = dic[key]
			# print(dis,i,'dis',shortest,key,nowdis,slength)
			if dis < nowdis:
				# a = 1/0
				# print(s1,'former')
				
				for i1 in range(i+1,len(s1)):
					s2.append(s1[i1])
				s1 = s1[:i+1]
				break

		else:
			continue

	
	s1.append(nex)
	s2.pop(s2.index(nex))
	# print(s1,s2,shortest,nex,'tonext')
	slength.append(shortest+slength[-1])
	# print('ind s',slength)

	if nex == end:
		break
alllength = 0
for i in range(len(s1)):
	if s1[i] == end:
		break
	if s1[i] < s1[i+1]:
		key = 'e%s'%s1[i]+'e%s'%s1[i+1]
	else:
		key = 'e%s'%s1[i+1]+'e%s'%s1[i]
	alllength += dic[key]
print(alllength,s1)
