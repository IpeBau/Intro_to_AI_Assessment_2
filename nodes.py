import time

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
nodeL = {'openpath':[],'name':'nodeL','targetdir':[],'distance':0,'passed':False,'latlong':[-13.2418087093092,6.0417003321605]}
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
nodepathAB = {'name':'AB', 'traffic':0, 'path_distance':0, 'startnode':nodeA, 'endnode':nodeB}
nodepathlist.append(nodepathAB)

nodeB.update({'openmove':[nodeA, nodeC]})
nodepathBA = {'name':'BA', 'traffic':0, 'path_distance':0, 'startnode':nodeB, 'endnode':nodeA}
nodepathBC = {'name':'BC', 'traffic':0, 'path_distance':0, 'startnode':nodeB, 'endnode':nodeC}
nodepathlist.append(nodepathBA)
nodepathlist.append(nodepathBC)

nodeC.update({'openmove':[nodeB, nodeD, nodeV]})
nodepathCB = {'name':'CB', 'traffic':0, 'path_distance':0, 'startnode':nodeC, 'endnode':nodeB}
nodepathCD = {'name':'CD', 'traffic':0, 'path_distance':0, 'startnode':nodeC, 'endnode':nodeD}
nodepathCV = {'name':'CV', 'traffic':0, 'path_distance':0, 'startnode':nodeC, 'endnode':nodeV}
nodepathlist.append(nodepathCB)
nodepathlist.append(nodepathCD)
nodepathlist.append(nodepathCV)

nodeD.update({'openmove':[nodeC, nodeE, nodeP]})
nodepathDC = {'name':'DC', 'traffic':0, 'path_distance':0, 'startnode':nodeD, 'endnode':nodeC}
nodepathDE = {'name':'DE', 'traffic':0, 'path_distance':0, 'startnode':nodeD, 'endnode':nodeE}
nodepathDP = {'name':'DP', 'traffic':0, 'path_distance':0, 'startnode':nodeD, 'endnode':nodeP}
nodepathlist.append(nodepathDC)
nodepathlist.append(nodepathDE)
nodepathlist.append(nodepathDP)

nodeE.update({'openmove':[nodeD, nodeF, nodeP]})
nodepathED = {'name':'ED', 'traffic':0, 'path_distance':0, 'startnode':nodeE, 'endnode':nodeD}
nodepathEF = {'name':'EF', 'traffic':0, 'path_distance':0, 'startnode':nodeE, 'endnode':nodeF}
nodepathEP = {'name':'EP', 'traffic':0, 'path_distance':0, 'startnode':nodeE, 'endnode':nodeP}
nodepathlist.append(nodepathED)
nodepathlist.append(nodepathEF)
nodepathlist.append(nodepathEP)

nodeF.update({'openmove':[nodeE, nodeS]})
nodepathFE = {'name':'FE', 'traffic':0, 'path_distance':0, 'startnode':nodeF, 'endnode':nodeE}
nodepathFS = {'name':'FS', 'traffic':0, 'path_distance':0, 'startnode':nodeF, 'endnode':nodeS}
nodepathlist.append(nodepathFE)
nodepathlist.append(nodepathFS)

nodeG.update({'openmove':[nodeH, nodeS, nodeB1]})
nodepathGH = {'name':'GH', 'traffic':0, 'path_distance':0, 'startnode':nodeG, 'endnode':nodeH}
nodepathGS = {'name':'GS', 'traffic':0, 'path_distance':0, 'startnode':nodeG, 'endnode':nodeS}
nodepathGB1 = {'name':'GB1', 'traffic':0, 'path_distance':0, 'startnode':nodeG, 'endnode':nodeB1}
nodepathlist.append(nodepathGH)
nodepathlist.append(nodepathGS)
nodepathlist.append(nodepathGB1)

nodeH.update({'openmove':[nodeG, nodeA1]})
nodepathHG = {'name':'HG', 'traffic':0, 'path_distance':0, 'startnode':nodeH, 'endnode':nodeG}
nodepathHA1 = {'name':'HA1', 'traffic':0, 'path_distance':0, 'startnode':nodeH, 'endnode':nodeA1}
nodepathlist.append(nodepathHG)
nodepathlist.append(nodepathHA1)

nodeI.update({'openmove':[nodeT, nodeJ, nodeA1]})
nodepathIT = {'name':'IT', 'traffic':0, 'path_distance':0, 'startnode':nodeI, 'endnode':nodeT}
nodepathIJ = {'name':'IJ', 'traffic':0, 'path_distance':0, 'startnode':nodeI, 'endnode':nodeJ}
nodepathIA1 = {'name':'IA1', 'traffic':0, 'path_distance':0, 'startnode':nodeI, 'endnode':nodeA1}
nodepathlist.append(nodepathIT)
nodepathlist.append(nodepathIJ)
nodepathlist.append(nodepathIA1)

nodeJ.update({'openmove':[nodeI, nodeK]})
nodepathJI = {'name':'JI', 'traffic':0, 'path_distance':0, 'startnode':nodeJ, 'endnode':nodeI}
nodepathJK = {'name':'JK', 'traffic':0, 'path_distance':0, 'startnode':nodeJ, 'endnode':nodeK}
nodepathlist.append(nodepathJI)
nodepathlist.append(nodepathJK)

nodeK.update({'openmove':[nodeJ]})
nodepathKJ = {'name':'KJ', 'traffic':0, 'path_distance':0, 'startnode':nodeK, 'endnode':nodeJ}
nodepathlist.append(nodepathKJ)

nodeL.update({'openmove':[nodeO, nodeR, nodeB1, nodeC1]})
nodepathLO = {'name':'LO', 'traffic':0, 'path_distance':0, 'startnode':nodeL, 'endnode':nodeO}
nodepathLR = {'name':'LR', 'traffic':0, 'path_distance':0, 'startnode':nodeL, 'endnode':nodeR}
nodepathLB1 = {'name':'LB1', 'traffic':0, 'path_distance':0, 'startnode':nodeL, 'endnode':nodeB1}
nodepathLC1 = {'name':'LC1', 'traffic':0, 'path_distance':0, 'startnode':nodeL, 'endnode':nodeC1}
nodepathlist.append(nodepathLO)
nodepathlist.append(nodepathLR)
nodepathlist.append(nodepathLB1)
nodepathlist.append(nodepathLC1)

nodeM.update({'openmove':[nodeU, nodeT]})
nodepathMU = {'name':'MU', 'traffic':0, 'path_distance':0, 'startnode':nodeM, 'endnode':nodeU}
nodepathMT = {'name':'MT', 'traffic':0, 'path_distance':0, 'startnode':nodeM, 'endnode':nodeT}
nodepathlist.append(nodepathMU)
nodepathlist.append(nodepathMT)

nodeN.update({'openmove':[nodeW, nodeZ]})
nodepathNW = {'name':'NW', 'traffic':0, 'path_distance':0, 'startnode':nodeN, 'endnode':nodeW}
nodepathNZ = {'name':'NZ', 'traffic':0, 'path_distance':0, 'startnode':nodeN, 'endnode':nodeZ}
nodepathlist.append(nodepathNW)
nodepathlist.append(nodepathNZ)

nodeO.update({'openmove':[nodeZ, nodeL]})
nodepathOZ = {'name':'OZ', 'traffic':0, 'path_distance':0, 'startnode':nodeO, 'endnode':nodeZ}
nodepathOL = {'name':'OL', 'traffic':0, 'path_distance':0, 'startnode':nodeO, 'endnode':nodeL}
nodepathlist.append(nodepathOZ)
nodepathlist.append(nodepathOL)

nodeP.update({'openmove':[nodeE, nodeQ]})
nodepathPE = {'name':'PE', 'traffic':0, 'path_distance':0, 'startnode':nodeP, 'endnode':nodeE}
nodepathPQ = {'name':'PQ', 'traffic':0, 'path_distance':0, 'startnode':nodeP, 'endnode':nodeQ}
nodepathlist.append(nodepathPE)
nodepathlist.append(nodepathPQ)

nodeQ.update({'openmove':[nodeP, nodeR]})
nodepathQP = {'name':'QP', 'traffic':0, 'path_distance':0, 'startnode':nodeQ, 'endnode':nodeP}
nodepathQR = {'name':'QR', 'traffic':0, 'path_distance':0, 'startnode':nodeQ, 'endnode':nodeR}
nodepathlist.append(nodepathQP)
nodepathlist.append(nodepathQR)

nodeR.update({'openmove':[nodeQ, nodeL]})
nodepathRQ = {'name':'RQ', 'traffic':0, 'path_distance':0, 'startnode':nodeR, 'endnode':nodeQ}
nodepathRL = {'name':'RL', 'traffic':0, 'path_distance':0, 'startnode':nodeR, 'endnode':nodeL}
nodepathlist.append(nodepathRQ)
nodepathlist.append(nodepathRL)

nodeS.update({'openmove':[nodeF, nodeG]})
nodepathSF = {'name':'SF', 'traffic':0, 'path_distance':0, 'startnode':nodeS, 'endnode':nodeF}
nodepathSG = {'name':'SG', 'traffic':0, 'path_distance':0, 'startnode':nodeS, 'endnode':nodeG}
nodepathlist.append(nodepathSF)
nodepathlist.append(nodepathSG)

nodeT.update({'openmove':[nodeI, nodeM]})
nodepathTI = {'name':'TI', 'traffic':0, 'path_distance':0, 'startnode':nodeT, 'endnode':nodeI}
nodepathTM = {'name':'TM', 'traffic':0, 'path_distance':0, 'startnode':nodeT, 'endnode':nodeM}
nodepathlist.append(nodepathTI)
nodepathlist.append(nodepathTM)

nodeU.update({'openmove':[nodeM, nodeC1]})
nodepathUM = {'name':'UM', 'traffic':0, 'path_distance':0, 'startnode':nodeU, 'endnode':nodeC1}
nodepathUC1 = {'name':'UC1', 'traffic':0, 'path_distance':0, 'startnode':nodeU, 'endnode':nodeC1}
nodepathlist.append(nodepathUM)
nodepathlist.append(nodepathUC1)

nodeV.update({'openmove':[nodeC,nodeW]})
nodepathVC = {'name':'VC', 'traffic':0, 'path_distance':0, 'startnode':nodeV, 'endnode':nodeC}
nodepathVW = {'name':'VW', 'traffic':0, 'path_distance':0, 'startnode':nodeV, 'endnode':nodeW}
nodepathlist.append(nodepathVC)
nodepathlist.append(nodepathVW)

nodeW.update({'openmove':[nodeV, nodeN]})
nodepathWV = {'name':'WV', 'traffic':0, 'path_distance':0, 'startnode':nodeW, 'endnode':nodeV}
nodepathWN = {'name':'WN', 'traffic':0, 'path_distance':0, 'startnode':nodeW, 'endnode':nodeN}
nodepathlist.append(nodepathWV)
nodepathlist.append(nodepathWN)

nodeZ.update({'openmove':[nodeN, nodeO]})
nodepathZN = {'name':'ZN', 'traffic':0, 'path_distance':0, 'startnode':nodeZ, 'endnode':nodeN}
nodepathZO = {'name':'ZO', 'traffic':0, 'path_distance':0, 'startnode':nodeZ, 'endnode':nodeO}
nodepathlist.append(nodepathZN)
nodepathlist.append(nodepathZO)

nodeA1.update({'openmove':[nodeH, nodeI]})
nodepathA1H = {'name':'A1H', 'traffic':0, 'path_distance':0, 'startnode':nodeA1, 'endnode':nodeH}
nodepathA1I = {'name':'A1I', 'traffic':0, 'path_distance':0, 'startnode':nodeA1, 'endnode':nodeI}
nodepathlist.append(nodepathA1H)
nodepathlist.append(nodepathA1I)

nodeB1.update({'openmove':[nodeG, nodeL]})
nodepathB1G = {'name':'B1G', 'traffic':0, 'path_distance':0, 'startnode':nodeB1, 'endnode':nodeG}
nodepathB1L = {'name':'B1L', 'traffic':0, 'path_distance':0, 'startnode':nodeB1, 'endnode':nodeL}
nodepathlist.append(nodepathB1G)
nodepathlist.append(nodepathB1L)

nodeC1.update({'openmove':[nodeL, nodeU]})
nodepathC1L = {'name':'C1L', 'traffic':0, 'path_distance':0, 'startnode':nodeC1, 'endnode':nodeL}
nodepathC1U = {'name':'C1U', 'traffic':0, 'path_distance':0, 'startnode':nodeC1, 'endnode':nodeU}
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
    nameprint = i['name']
    pathprint = i['openpath']
    print(f"{nameprint}: {pathprint}")

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
        i.update({'targetdir':['south','east']})
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

def playerposcheck(playerlat, playerlong):
    for i in nodelist:
        if i['latlong'][0]==playerlat and i['latlong'][1]==playerlong:
            return i

def availabledirections(node):
    distanceslist = []
    availabledirectionslist = []
    #p2pdistancestlist = []
    while True:
        #openmove = node['openmove']
        directionslist = node['openmove']
        availabledirectionsprompt = 'AVAILABLE NODES:\n'
        for i in directionslist:
            newlat = i['latlong'][0]
            newlong = i['latlong'][1]

            availabledirectionsprompt += f"{i['name']}\n"
            availabledirectionslist.append(i)

            newnode = playerposcheck(newlat,newlong)
            #if newnode['passed']==True:
            #    continue
            #else:       
            distanceslist.append(newnode['distance'])

            #p2pdistancestlist.append()
        break
    print(availabledirectionsprompt)
    print(f'\n{distanceslist}')
    time.sleep(2)

    chosenpath = availabledirectionslist[distanceslist.index(min(distanceslist))]
    chosenpathname = chosenpath['name']
    print(f"Selected direction: {chosenpathname}")
    return chosenpath

def passedcompute(x):
    if x['passed']==True:
        prevdistance = x['distance']
        newdistance = prevdistance + 30
        x.update({'distance':newdistance})

pathlist = []
stepcount = 0
while True:
    currentnode = playerposcheck(playerlat,playerlong)
    print(f"\nCurrent Node: {currentnode['name']}")
    print(f"\nCurrent Node: {currentnode['distance']}")
    if currentnode['passed']==True:
        try:
            pathlist.remove(currentnode['name'])
            passedcompute(currentnode)
            stepcount-=1
        except:
            passedcompute(currentnode)
            stepcount-=1
    currentnode.update({'passed':True})
    passedcompute(currentnode)
    pathlist.append(currentnode['name'])
    stepcount+=1
    
    if playerlat != exitlat or playerlong != exitlong: 
        
        previousnode = currentnode
        move = availabledirections(currentnode)
        playerlong = move['latlong'][1]
        playerlat = move['latlong'][0]
                
        #currentnode = playerposcheck(playerlat,playerlong)
        if move['passed']==True:
            pathlist.remove(previousnode['name'])
            passedcompute(previousnode)
            stepcount-=1

        time.sleep(2)

    elif playerlat == exitlat and playerlong == exitlong:
        print("\nPizza delivered!\nEnjoy!\n")
        print(f'Optimum path:{pathlist}')
        print(f'Number of steps: {stepcount-1}')
        break

for i in nodelist:
    print(f"{i['name']}: {i['distance']}")
