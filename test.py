import yaml

# params = {}
# params['a']={}
# params['a']['b']={}
# params['a']['b']['c'] = 3
# params['a']['b']['d'] = 4
# params['a']['e'] = 5

# # def printChildren(d):
# # 	print (type(d))
# # 	print (type(d)==dict)
# # 	if type(d) == dict:
# # 		for child in d:
# # 			printChildren(child)
# # 	else:
# # 		print (d)

def dictToList(d, dList):
	for key, value in d.items():
		if type(value)==dict:
			dictToList(value, dList)
		else:
			# print (value)	
			dList.append(value)
	return dList

def listToDict(d, dList):
	for key, value in d.items():
		if type(value)==dict:
			listToDict(value, dList)
		else:
			print ('here', dList, type(dList))	
			thing = dList.pop(0)
			d[key] = thing
	return d

# l = dictToList(params, [])

# print (l)
# for item in range(len(l)):
# 	l[item] += 1
# print (l)

# print (params)
# new = listToDict(params, l)
# print (new)


