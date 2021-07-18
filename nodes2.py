import time
speed = 0

nodeA = {'openpath':[],'name':'nodeA','targetdir':[],'distance':0,'passed':False,'latlong':[9.8149154202846,4.5021985657435]}
nodeB = {'openpath':[],'name':'nodeB','targetdir':[],'distance':0,'passed':False,'latlong':[8.9556586204239,4.5021985657435]}
nodeC = {'openpath':[],'name':'nodeC','targetdir':[],'distance':0,'passed':False,'latlong':[8.0964018205633,4.5021985657435]}
nodeD = {'openpath':[],'name':'nodeD','targetdir':[],'distance':0,'passed':False,'latlong':[4.1581414878687,3.7861512325263]}
nodeE = {'openpath':[],'name':'nodeE','targetdir':[],'distance':0,'passed':False,'latlong':[3.2988846880081,3.4281275659177]}
nodeF = {'openpath':[],'name':'nodeF','targetdir':[],'distance':0,'passed':False,'latlong':[2.1890113215214,-0.8681564333855]}
nodeG = {'openpath':[],'name':'nodeG','targetdir':[],'distance':0,'passed':False,'latlong':[-2.7875176443381,0.1701121997794]}
nodeH = {'openpath':[],'name':'nodeH','targetdir':[],'distance':0,'passed':False,'latlong':[-6.2961495771024,-1.2261800999941]}
nodeI = {'openpath':[],'name':'nodeI','targetdir':[],'distance':0,'passed':False,'latlong':[-12.9553897760223,-5.4866617326364]}
nodeJ = {'openpath':[],'name':'nodeJ','targetdir':[],'distance':0,'passed':False,'latlong':[-14.9961246756913,-7.8496179322532]}
nodeK = {'openpath':[],'name':'nodeK','targetdir':[],'distance':0,'passed':False,'latlong':[-13.7788442092221,-9.2101078653659]}
nodeL = {'openpath':[],'name':'nodeL','targetdir':[],'distance':0,'passed':False,'latlong':[-3.8615886441639,6.0417003321605]}
nodeM = {'openpath':[],'name':'nodeM','targetdir':[],'distance':0,'passed':False,'latlong':[-13.2418087093092,1.3873926662487]}
nodeN = {'openpath':[],'name':'nodeN','targetdir':[],'distance':0,'passed':False,'latlong':[4.3729556878339,9.5861346315856]}
nodeO = {'openpath':[],'name':'nodeO','targetdir':[],'distance':0,'passed':False,'latlong':[-3.6109720775379,7.7602139318817]}
nodeP = {'openpath':[],'name':'nodeP','targetdir':[],'distance':0,'passed':False,'latlong':[3.4420941546515,4.5021985657435]}
nodeQ = {'openpath':[],'name':'nodeQ','targetdir':[],'distance':0,'passed':False,'latlong':[2.2248136881823,4.8602222323521]}
nodeR = {'openpath':[],'name':'nodeR','targetdir':[],'distance':0,'passed':False,'latlong':[0.8285213884087,5.8268861321953]}
nodeS = {'openpath':[],'name':'nodeS','targetdir':[],'distance':0,'passed':False,'latlong':[-0.3887590780605,0.3133216664229]}
nodeT = {'openpath':[],'name':'nodeT','targetdir':[],'distance':0,'passed':False,'latlong':[-11.5590974762488,-1.4051919332984]}
nodeU = {'openpath':[],'name':'nodeU','targetdir':[],'distance':0,'passed':False,'latlong':[-11.0220619763359,3.2133133659525]}
nodeV = {'openpath':[],'name':'nodeV','targetdir':[],'distance':0,'passed':False,'latlong':[8.2754136538676,5.2182458989607]}
nodeW = {'openpath':[],'name':'nodeW','targetdir':[],'distance':0,'passed':False,'latlong':[4.5161651544773,8.726877831725]}
nodeZ = {'openpath':[],'name':'nodeZ','targetdir':[],'distance':0,'passed':False,'latlong':[-0.3887590780605,9.4429251649422]}
nodeA1 = {'openpath':[],'name':'nodeA1','targetdir':[],'distance':0,'passed':False,'latlong':[-9.2319436432929,-3.1595078996805]}
nodeB1 = {'openpath':[],'name':'nodeB1','targetdir':[],'distance':0,'passed':False,'latlong':[-4.0406004774682,1.566404499553]}
nodeC1 = {'openpath':[],'name':'nodeC1','targetdir':[],'distance':0,'passed':False,'latlong':[-7.2270111102847,4.2873843657783]}
nodelist = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH, nodeI, nodeJ, nodeK, nodeL, nodeM, nodeN, nodeO, nodeP, nodeQ, nodeR, nodeS, nodeT, nodeU, nodeV, nodeW, nodeZ, nodeA1, nodeB1, nodeC1]

nodepathlist = []

nodeA.update({'openmove':[nodeB]})
nodepathAB = {'name':'Katipunan SB', 'traffic':0, 'path_distance':0, 'startnode':nodeA, 'endnode':nodeB, 'passed':False}
nodepathlist.append(nodepathAB)

nodeB.update({'openmove':[nodeA, nodeC]})
nodepathBA = {'name':'Katipunan NB', 'traffic':0, 'path_distance':0, 'startnode':nodeB, 'endnode':nodeA, 'passed':False}
nodepathBC = {'name':'Katipunan Flyover/Aurora SB', 'traffic':0, 'path_distance':0, 'startnode':nodeB, 'endnode':nodeC, 'passed':False}
nodepathlist.append(nodepathBA)
nodepathlist.append(nodepathBC)

nodeC.update({'openmove':[nodeB, nodeD, nodeV]})
nodepathCB = {'name':'Katipunan Flyover/Aurora NB', 'traffic':0, 'path_distance':0, 'startnode':nodeC, 'endnode':nodeB, 'passed':False}
nodepathCD = {'name':'Katipunan Flyover/Aurora to Katipunan Ext. SB', 'traffic':0, 'path_distance':0, 'startnode':nodeC, 'endnode':nodeD, 'passed':False}
nodepathCV = {'name':'Katipunan Flyover/Aurora to Marikina Highway - Barangka SB', 'traffic':0, 'path_distance':0, 'startnode':nodeC, 'endnode':nodeV, 'passed':False}
nodepathlist.append(nodepathCB)
nodepathlist.append(nodepathCD)
nodepathlist.append(nodepathCV)

nodeD.update({'openmove':[nodeC, nodeE]})
nodepathDC = {'name':'Katipunan Extension 1 to Katipunan Flyover/Aurora NB', 'traffic':0, 'path_distance':0, 'startnode':nodeD, 'endnode':nodeC, 'passed':False}
nodepathDE = {'name':'Katipunan Extension 1 to Katipunan Extension 2 SB', 'traffic':0, 'path_distance':0, 'startnode':nodeD, 'endnode':nodeE, 'passed':False}
nodepathlist.append(nodepathDC)
nodepathlist.append(nodepathDE)

nodeE.update({'openmove':[nodeD, nodeF, nodeP]})
nodepathED = {'name':'Katipunan Extension 2 to Katipunan Extension 1 NB', 'traffic':0, 'path_distance':0, 'startnode':nodeE, 'endnode':nodeD, 'passed':False}
nodepathEF = {'name':'Santolan SB', 'traffic':0, 'path_distance':0, 'startnode':nodeE, 'endnode':nodeF, 'passed':False}
nodepathEP = {'name':'Katipunan Tunnel to Libis', 'traffic':0, 'path_distance':0, 'startnode':nodeE, 'endnode':nodeP, 'passed':False}
nodepathlist.append(nodepathED)
nodepathlist.append(nodepathEF)
nodepathlist.append(nodepathEP)

nodeF.update({'openmove':[nodeE, nodeS]})
nodepathFE = {'name':'Santolan NB', 'traffic':0, 'path_distance':0, 'startnode':nodeF, 'endnode':nodeE, 'passed':False}
nodepathFS = {'name':'EDSA: Santolan to Connecticut SB', 'traffic':0, 'path_distance':0, 'startnode':nodeF, 'endnode':nodeS, 'passed':False}
nodepathlist.append(nodepathFE)
nodepathlist.append(nodepathFS)

nodeG.update({'openmove':[nodeH, nodeS, nodeB1]})
nodepathGH = {'name':'EDSA: Ortigas to Shaw SB', 'traffic':0, 'path_distance':0, 'startnode':nodeG, 'endnode':nodeH, 'passed':False}
nodepathGS = {'name':'EDSA: Ortigas to Connecticut NB', 'traffic':0, 'path_distance':0, 'startnode':nodeG, 'endnode':nodeS, 'passed':False}
nodepathGB1 = {'name':'EDSA: Ortigas Avenue to Ortigas cor. San Miguel Ave.', 'traffic':0, 'path_distance':0, 'startnode':nodeG, 'endnode':nodeB1, 'passed':False}
nodepathlist.append(nodepathGH)
nodepathlist.append(nodepathGS)
nodepathlist.append(nodepathGB1)

nodeH.update({'openmove':[nodeG, nodeA1]})
nodepathHG = {'name':'EDSA: Shaw to Ortigas Ave. NB', 'traffic':0, 'path_distance':0, 'startnode':nodeH, 'endnode':nodeG, 'passed':False}
nodepathHA1 = {'name':'EDSA: Shaw to Pioneer', 'traffic':0, 'path_distance':0, 'startnode':nodeH, 'endnode':nodeA1, 'passed':False}
nodepathlist.append(nodepathHG)
nodepathlist.append(nodepathHA1)

nodeI.update({'openmove':[nodeT, nodeJ, nodeA1]})
nodepathIT = {'name':'EDSA: Estrella+ to Narra Ext.', 'traffic':0, 'path_distance':0, 'startnode':nodeI, 'endnode':nodeT, 'passed':False}
nodepathIJ = {'name':'EDSA: Estrella+ to Ayala Avenue', 'traffic':0, 'path_distance':0, 'startnode':nodeI, 'endnode':nodeJ, 'passed':False}
nodepathIA1 = {'name':'EDSA: Estrella+ to Pioneer', 'traffic':0, 'path_distance':0, 'startnode':nodeI, 'endnode':nodeA1, 'passed':False}
nodepathlist.append(nodepathIT)
nodepathlist.append(nodepathIJ)
nodepathlist.append(nodepathIA1)

nodeJ.update({'openmove':[nodeI, nodeK]})
nodepathJI = {'name':'EDSA: Ayala Avenue to Estrella+', 'traffic':0, 'path_distance':0, 'startnode':nodeJ, 'endnode':nodeI, 'passed':False}
nodepathJK = {'name':'EDSA: Ayala Avenue to Ayala Ave. cor. Makati Ave.', 'traffic':0, 'path_distance':0, 'startnode':nodeJ, 'endnode':nodeK, 'passed':False}
nodepathlist.append(nodepathJI)
nodepathlist.append(nodepathJK)

nodeK.update({'openmove':[nodeJ]})
nodepathKJ = {'name':'EDSA: Ayala Ave. cor. Makati Ave. to Ayala Avenue', 'traffic':0, 'path_distance':0, 'startnode':nodeK, 'endnode':nodeJ, 'passed':False}
nodepathlist.append(nodepathKJ)

nodeL.update({'openmove':[nodeO, nodeR, nodeB1, nodeC1]})
nodepathLO = {'name':'Ortigas Ave.: C5 to Amang Rodriguez', 'traffic':0, 'path_distance':0, 'startnode':nodeL, 'endnode':nodeO, 'passed':False}
nodepathLR = {'name':'C5: Ortigas to Eastwood', 'traffic':0, 'path_distance':0, 'startnode':nodeL, 'endnode':nodeR, 'passed':False}
nodepathLB1 = {'name':'Ortigas: C5 to San Miguel Ave.', 'traffic':0, 'path_distance':0, 'startnode':nodeL, 'endnode':nodeB1, 'passed':False}
nodepathLC1 = {'name':'C5: Ortigas to Lanuza', 'traffic':0, 'path_distance':0, 'startnode':nodeL, 'endnode':nodeC1, 'passed':False}
nodepathlist.append(nodepathLO)
nodepathlist.append(nodepathLR)
nodepathlist.append(nodepathLB1)
nodepathlist.append(nodepathLC1)

nodeM.update({'openmove':[nodeU, nodeT]})
nodepathMU = {'name':'C5: Kalayaan Avenue to Bagong Ilog', 'traffic':0, 'path_distance':0, 'startnode':nodeM, 'endnode':nodeU, 'passed':False}
nodepathMT = {'name':'Kalayaan Avenue: C5 to Narra Extension', 'traffic':0, 'path_distance':0, 'startnode':nodeM, 'endnode':nodeT, 'passed':False}
nodepathlist.append(nodepathMU)
nodepathlist.append(nodepathMT)

nodeN.update({'openmove':[nodeW, nodeZ]})
nodepathNW = {'name':'Amang Rodriguez to Marikina Infanta Highway Curve', 'traffic':0, 'path_distance':0, 'startnode':nodeN, 'endnode':nodeW, 'passed':False}
nodepathNZ = {'name':'Amang Rodriguez: Marikina Infanta to Manggahan', 'traffic':0, 'path_distance':0, 'startnode':nodeN, 'endnode':nodeZ, 'passed':False}
nodepathlist.append(nodepathNW)
nodepathlist.append(nodepathNZ)

nodeO.update({'openmove':[nodeZ, nodeL]})
nodepathOZ = {'name':'Amang Rodriguez: Ortigas to Manggahan', 'traffic':0, 'path_distance':0, 'startnode':nodeO, 'endnode':nodeZ, 'passed':False}
nodepathOL = {'name':'Ortigas: Amang Rodriquez to C5', 'traffic':0, 'path_distance':0, 'startnode':nodeO, 'endnode':nodeL, 'passed':False}
nodepathlist.append(nodepathOZ)
nodepathlist.append(nodepathOL)

nodeP.update({'openmove':[nodeE, nodeQ]})
nodepathPE = {'name':'Libis to Katipunan Tunnel', 'traffic':0, 'path_distance':0, 'startnode':nodeP, 'endnode':nodeE, 'passed':False}
nodepathPQ = {'name':'Katipunan-Libis Tunnel to Mercury Ave', 'traffic':0, 'path_distance':0, 'startnode':nodeP, 'endnode':nodeQ, 'passed':False}
nodepathlist.append(nodepathPE)
nodepathlist.append(nodepathPQ)

nodeQ.update({'openmove':[nodeP, nodeR]})
nodepathQP = {'name':'Mercury Ave. to Katipunan-Libis Tunnel', 'traffic':0, 'path_distance':0, 'startnode':nodeQ, 'endnode':nodeP, 'passed':False}
nodepathQR = {'name':'Mercury Ave. to Eastwood', 'traffic':0, 'path_distance':0, 'startnode':nodeQ, 'endnode':nodeR, 'passed':False}
nodepathlist.append(nodepathQP)
nodepathlist.append(nodepathQR)

nodeR.update({'openmove':[nodeQ, nodeL]})
nodepathRQ = {'name':'Eastwood to Mercury Ave.', 'traffic':0, 'path_distance':0, 'startnode':nodeR, 'endnode':nodeQ, 'passed':False}
nodepathRL = {'name':'C5: Eastwood to Ortigas Ave. ', 'traffic':0, 'path_distance':0, 'startnode':nodeR, 'endnode':nodeL, 'passed':False}
nodepathlist.append(nodepathRQ)
nodepathlist.append(nodepathRL)

nodeS.update({'openmove':[nodeF, nodeG]})
nodepathSF = {'name':'EDSA: Connecticut to Santolan', 'traffic':0, 'path_distance':0, 'startnode':nodeS, 'endnode':nodeF, 'passed':False}
nodepathSG = {'name':'EDSA: Connecticut to Ortigas Ave.', 'traffic':0, 'path_distance':0, 'startnode':nodeS, 'endnode':nodeG, 'passed':False}
nodepathlist.append(nodepathSF)
nodepathlist.append(nodepathSG)

nodeT.update({'openmove':[nodeI, nodeM]})
nodepathTI = {'name':'Narra Ext. to Estrella+', 'traffic':0, 'path_distance':0, 'startnode':nodeT, 'endnode':nodeI, 'passed':False}
nodepathTM = {'name':'Kalayaan Ave.: Narra Ext. to C5', 'traffic':0, 'path_distance':0, 'startnode':nodeT, 'endnode':nodeM, 'passed':False}
nodepathlist.append(nodepathTI)
nodepathlist.append(nodepathTM)

nodeU.update({'openmove':[nodeM, nodeC1]})
nodepathUM = {'name':'C5: Bagong Ilog to Kalayaan', 'traffic':0, 'path_distance':0, 'startnode':nodeU, 'endnode':nodeM, 'passed':False}
nodepathUC1 = {'name':'C5: Bagong Ilog to Lanuza', 'traffic':0, 'path_distance':0, 'startnode':nodeU, 'endnode':nodeC1, 'passed':False}
nodepathlist.append(nodepathUM)
nodepathlist.append(nodepathUC1)

nodeV.update({'openmove':[nodeC,nodeW]})
nodepathVC = {'name':'Marikina Highway: Barangka to Katipunan Flyover/Aurora', 'traffic':0, 'path_distance':0, 'startnode':nodeV, 'endnode':nodeC, 'passed':False}
nodepathVW = {'name':'Marikina Highway: Barangka to Amang Rodriguez', 'traffic':0, 'path_distance':0, 'startnode':nodeV, 'endnode':nodeW, 'passed':False}
nodepathlist.append(nodepathVC)
nodepathlist.append(nodepathVW)

nodeW.update({'openmove':[nodeV, nodeN]})
nodepathWV = {'name':'Marikina Highway: Amang Rodriguez to Barangka', 'traffic':0, 'path_distance':0, 'startnode':nodeW, 'endnode':nodeV, 'passed':False}
nodepathWN = {'name':'Marikina Highway: Amang Rodriguez', 'traffic':0, 'path_distance':0, 'startnode':nodeW, 'endnode':nodeN, 'passed':False}
nodepathlist.append(nodepathWV)
nodepathlist.append(nodepathWN)

nodeZ.update({'openmove':[nodeN, nodeO]})
nodepathZN = {'name':'Amang Rodriguez: Manggahan to Marikina Highway', 'traffic':0, 'path_distance':0, 'startnode':nodeZ, 'endnode':nodeN, 'passed':False}
nodepathZO = {'name':'Amang Rodriguez: Manggahan to Ortigas', 'traffic':0, 'path_distance':0, 'startnode':nodeZ, 'endnode':nodeO, 'passed':False}
nodepathlist.append(nodepathZN)
nodepathlist.append(nodepathZO)

nodeA1.update({'openmove':[nodeH, nodeI]})
nodepathA1H = {'name':'EDSA: Pioneer to Shaw', 'traffic':0, 'path_distance':0, 'startnode':nodeA1, 'endnode':nodeH, 'passed':False}
nodepathA1I = {'name':'EDSA: Pioneer to Estrella+', 'traffic':0, 'path_distance':0, 'startnode':nodeA1, 'endnode':nodeI, 'passed':False}
nodepathlist.append(nodepathA1H)
nodepathlist.append(nodepathA1I)

nodeB1.update({'openmove':[nodeG, nodeL]})
nodepathB1G = {'name':'EDSA: Ortigas cor. San Miguel Ave. to Ortigas Avenue', 'traffic':0, 'path_distance':0, 'startnode':nodeB1, 'endnode':nodeG, 'passed':False}
nodepathB1L = {'name':'Ortigas: San Miguel Ave. to C5', 'traffic':0, 'path_distance':0, 'startnode':nodeB1, 'endnode':nodeL, 'passed':False}
nodepathlist.append(nodepathB1G)
nodepathlist.append(nodepathB1L)

nodeC1.update({'openmove':[nodeL, nodeU]})
nodepathC1L = {'name':'C5: Lanuza to Ortigas Ave.', 'traffic':0, 'path_distance':0, 'startnode':nodeC1, 'endnode':nodeL, 'passed':False}
nodepathC1U = {'name':'C5: Lanuza to Bagong Ilog', 'traffic':0, 'path_distance':0, 'startnode':nodeC1, 'endnode':nodeU, 'passed':False}
nodepathlist.append(nodepathC1L)
nodepathlist.append(nodepathC1U)

for i in nodepathlist:
    if len(i['startnode']['openpath'])==0:
        i['startnode'].update({'openpath':[i]})
    elif len(i['startnode']['openpath'])>0:
        templist = i['startnode']['openpath']
        templist.append(i)
        i['startnode'].update({'openpath':templist})

for i in nodelist:
    namelist = []
    for x in i['openpath']:
        namelist.append(x['name'])
    print(f"{i['name']}: {namelist}")

#y
playerlat = 9.8149154202846
#x 
playerlong = 4.5021985657435
#y
exitlat = -13.7788442092221
#x
exitlong = -9.2101078653659



#def targetdir(x,y):
#    # x = node targetdir attribte
#    targetdirlist = x['targetdir']
#    targetdirlist.append(y)
#    x.update({'targetdir':targetdirlist})


for i in nodelist:
    nodelat = i['latlong'][0]
    nodelong = i['latlong'][1]
    nodelatlong = i['latlong']
    openmove = i['openmove']

    if 'north' not in openmove:
        i.update({'northpenalty':5})
    else:
        i.update({'northpenalty':0})
    
    if 'south' not in openmove:
        i.update({'southpenalty':5})
    else:
        i.update({'southpenalty':0})

    if 'east' not in openmove:
        i.update({'eastpenalty':5})
    else:
        i.update({'eastpenalty':0})
    
    if 'west' not in openmove:
        i.update({'westpenalty':5})
    else:
        i.update({'westpenalty':0})
    
    #adjacent distance
    #if 'north' in openmove:
    #    i.update({'northdistance':10})
    #else:
    #    i.update({'northpenalty':0})
    #
    #if 'south' not in openmove:
    #    i.update({'southpenalty':10})
    #else:
    #    i.update({'southpenalty':0})

    #if 'east' not in openmove:
    #    i.update({'eastpenalty':10})
    #else:
    #    i.update({'eastpenalty':0})
    #
    #if 'west' not in openmove:
    #    i.update({'westpenalty':10})
    #else:
    #    i.update({'westpenalty':0})

    northpenalty = 0#i['northpenalty']
    southpenalty = 0#i['southpenalty']
    eastpenalty = 0#i['eastpenalty']
    westpenalty = 0#i['westpenalty']

    latdif = abs(nodelat-exitlat)
    longdif = abs(nodelong-exitlong)

#    if exitlat > nodelat:
#        targetdir(i,'north')
#    elif exitlat < nodelat:
#        targetdir(i,'south')
#    
#    if exitlong > nodelong:
#        targetdir(i,'east')
#    if exitlong < nodelong:
#        targetdir(i,'west')


    if exitlat > nodelat and exitlong > nodelong:
        i.update({'targetdir':'southwest'})
        i.update({'distance': sum([latdif+southpenalty,longdif+eastpenalty])/len(nodelatlong)})
    elif exitlat > nodelat and exitlong < nodelong:
        i.update({'targetdir':'southwest'})
        i.update({'distance': sum([latdif+southpenalty,longdif+westpenalty])/len(nodelatlong)})
    elif exitlat < nodelat and exitlong > nodelong:
        i.update({'targetdir':'northeast'})
        i.update({'distance': sum([latdif+northpenalty,longdif+eastpenalty])/len(nodelatlong)})
    elif exitlat < nodelat and exitlong < nodelong:
        i.update({'targetdir':'northwest'})
        i.update({'distance': sum([latdif+northpenalty,longdif+westpenalty])/len(nodelatlong)})
    elif exitlat == nodelat and exitlong > nodelong:
        i.update({'targetdir':'east'})
        i.update({'distance': sum([longdif+eastpenalty])})
    elif exitlat == nodelat and exitlong < nodelong:
        i.update({'targetdir':'west'})
        i.update({'distance': sum([longdif+westpenalty])})
    elif exitlat > nodelat and exitlong == nodelong:
        i.update({'targetdir':'south'})
        i.update({'distance': sum([latdif+southpenalty])})
    elif exitlat < nodelat and exitlong == nodelong:
        i.update({'targetdir':'north'})
        i.update({'distance': sum([latdif+northpenalty])})
    elif exitlat == nodelat and exitlong == nodelong:
        i.update({'targetdir':'target'})
        i.update({'distance': sum([latdif,longdif])})

for i in nodelist:
    print(f"{i['name']}: {i['distance']}")

for i in nodepathlist:
    path = i['endnode']['distance'] + i['traffic']*20
    i.update({'path_distance':path})
    print(f"{i['name']}: {i['path_distance']}")

#def playerposcheck(playerlat, playerlong):
#    for i in nodepathlist:
#        if i['startnode']['latlong'][0]==playerlat and i['startnode']['latlong'][1]==playerlong:
#            return i['startnode']

def playerposcheck(playerlat, playerlong,z):
    if z == 'node':
        for i in nodelist:
            if i['latlong'][0]==playerlat and i['latlong'][1]==playerlong:
                return i
    if z == 'paht':
        for i in nodepathlist:
            if i['startnode']['latlong'][0]==playerlat and i['startnode']['latlong'][1]==playerlong:
                return i['startnode']

def availabledirections(node):
    distanceslist = []
    availabledirectionslist = []
    openpathslist = node['openpath']
    #p2pdistancestlist = []
    while True:
        #openmove = node['openmove']
        directionslist = node['openpath']
        availabledirectionsprompt = 'AVAILABLE PATHS:\n'
        for i in directionslist:
            newlat = i['endnode']['latlong'][0]
            newlong = i['endnode']['latlong'][1]

            availabledirectionsprompt += f"{i['name']}\n"
            availabledirectionslist.append(i)

            #newnode = playerposcheck(newlat,newlong)
            #if newnode['passed']==True:
            #    continue
            #else:       
            distanceslist.append(i['path_distance'])

            #p2pdistancestlist.append()
        break
    print(availabledirectionsprompt)
    print(f'\n{distanceslist}')
    time.sleep(speed)

    chosendistance = min(distanceslist)
    chosenpath = availabledirectionslist[distanceslist.index(chosendistance)]
    chosenpathname = chosenpath['name']
    print(f"Selected direction: {chosenpathname}")
    return chosenpath

#def nchoose(x,trycount):
#    chosenlist = []
#    while len(chosenlist)<trycount:
#        try:
#            
#            chosenlist = []
#            current = 0
#            minimum = min(x)
#            maximum = maximum(x)
#            chosenlist.append(minimum)
#            count = 0
#            for i in x:
#                if count == 0:
#                    chosen = 

def passedcompute(x):
    if x['passed']==True:
        prevdistance = x['distance']
        newdistance = prevdistance + 20
        x.update({'distance':newdistance})

def pathpassedcompute(x):
    if x['passed']==True:
        prevdistance = x['path_distance']
        newdistance = prevdistance + 20
        x.update({'path_distance':newdistance})

nodepathlistpassed = []
pathlist = []
stepcount = 0
while True:
    currentnode = playerposcheck(playerlat,playerlong,'node')

    print(f"\nCurrent Node: {currentnode['name']}")
    #print(f"\nCurrent Node Distance: {currentnode['distance']}")
    #if currentnode['passed']==True:
    #    try:
    #        pathlist.remove(currentnode['name'])
    #        passedcompute(currentnode)
    #        stepcount-=1
    #    except:
    #        passedcompute(currentnode)
    #        stepcount-=1    
#
    #    try:
    #        nodepathlistpassed.remove(currentpath['name'])
    #        pathpassedcompute(currentpath)
    #    except:
    #        pathpassedcompute(currentpath)
    currentnode.update({'passed':True})
    passedcompute(currentnode)
    pathlist.append(currentnode['name'])

    #try:
    #    currentpath.update({'passed':True})
    #    pathpassedcompute(currentpath)
    #    nodepathlistpassed.append(currentpath['name'])
    #except:
    #    None
    #stepcount+=1
    
    if playerlat != exitlat or playerlong != exitlong: 
        
        
        try:
            previousnode = currentnode
            previouspath = currentpath
        except:
            previousnode = currentnode
        
        move = availabledirections(currentnode)
        playerlong = move['endnode']['latlong'][1]
        playerlat = move['endnode']['latlong'][0]
        currentpath = move
        currentnode = move['endnode']

        try:
            currentpath.update({'passed':True})
            pathpassedcompute(currentpath)
            nodepathlistpassed.append(currentpath['name'])
        except:
            currentpath.update({'passed':True})
            pathpassedcompute(currentpath)
        stepcount+=1
                
        #currentnode = playerposcheck(playerlat,playerlong)
        try:
            if currentnode['passed']==True:
                try:
                    pathlist.remove(previousnode['name'])
                    nodepathlistpassed.remove(previouspath['name'])
                except:
                    pathlist.remove(previousnode['name'])
                stepcount-=1
                try:
                    pathpassedcompute(previouspath)
                    passedcompute(previousnode)
                except:
                    passedcompute(previousnode)
        except:
            pathlist.remove(previousnode['name'])
            passedcompute(previousnode)

        for i in nodepathlist:
            path = i['endnode']['distance'] + i['traffic']*20
            i.update({'path_distance':path})
            print(f"{i['name']}: {i['path_distance']}")    
        

        time.sleep(speed)

    elif playerlat == exitlat and playerlong == exitlong:
        print("\nPizza delivered!\nEnjoy!\n")
        print(f'Optimum path nodes:{pathlist}')
        print(f'Optimum path:{nodepathlistpassed}')
        print(f'Number of steps: {stepcount-1}')
        break

for i in nodepathlist:
    print(f"{i['name']}: {i['path_distance']}")