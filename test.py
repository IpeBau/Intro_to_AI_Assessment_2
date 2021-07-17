testdict = {'openpath':['test', 'test2']}
test2dict = {'node':testdict}

print(test2dict['node']['openpath'])
test2dict['node']['openpath'].append('test3')
print(test2dict['node']['openpath'])

for i in range(0,3,1):
    print(i)

nodeA = {'openpath':[],'name':'nodeA','targetdir':[],'distance':0,'passed':False,'latlong':[9.8149154202846,4.5021985657435]}
nodeB = {'openpath':[],'name':'nodeB','targetdir':[],'distance':0,'passed':False,'latlong':[8.9556586204239,4.5021985657435]}

nodepathlist = []

nodeA.update({'openmove':[nodeB]})
nodepathAB = {'name':'AB', 'traffic':0, 'path_distance':0, 'startnode':nodeA, 'endnode':nodeB}
nodepathlist.append(nodepathAB)

for i in nodepathlist:
    print(i['name'])

print(nodepathlist)