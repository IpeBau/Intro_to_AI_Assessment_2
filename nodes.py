import time

nodeA = {'name':'nodeA','targetdir':[],'distance':0,'passed':False,'latlong':[9.8149154202846,4.5021985657435]}
nodeB = {'name':'nodeB','targetdir':[],'distance':0,'passed':False,'latlong':[8.9556586204239,4.5021985657435]}
nodeC = {'name':'nodeC','targetdir':[],'distance':0,'passed':False,'latlong':[8.0964018205633,4.5021985657435]}
nodeD = {'name':'nodeD','targetdir':[],'distance':0,'passed':False,'latlong':[4.1581414878687,3.7861512325263]}
nodeE = {'name':'nodeE','targetdir':[],'distance':0,'passed':False,'latlong':[3.2988846880081,3.4281275659177]}
nodeF = {'name':'nodeF','targetdir':[],'distance':0,'passed':False,'latlong':[2.1890113215214,-0.8681564333855]}
nodeG = {'name':'nodeG','targetdir':[],'distance':0,'passed':False,'latlong':[-2.7875176443381,0.1701121997794]}
nodeH = {'name':'nodeH','targetdir':[],'distance':0,'passed':False,'latlong':[-6.2961495771024,-1.2261800999941]}
nodeI = {'name':'nodeI','targetdir':[],'distance':0,'passed':False,'latlong':[-12.9553897760223,-5.4866617326364]}
nodeJ = {'name':'nodeJ','targetdir':[],'distance':0,'passed':False,'latlong':[-14.9961246756913,-7.8496179322532]}
nodeK = {'name':'nodeK','targetdir':[],'distance':0,'passed':False,'latlong':[-13.7788442092221,-9.2101078653659]}
nodeL = {'name':'nodeL','targetdir':[],'distance':0,'passed':False,'latlong':[-13.2418087093092,6.0417003321605]}
nodeM = {'name':'nodeM','targetdir':[],'distance':0,'passed':False,'latlong':[-13.2418087093092,1.3873926662487]}
nodeN = {'name':'nodeN','targetdir':[],'distance':0,'passed':False,'latlong':[4.3729556878339,9.5861346315856]}
nodeO = {'name':'nodeO','targetdir':[],'distance':0,'passed':False,'latlong':[-3.6109720775379,7.7602139318817]}
nodeP = {'name':'nodeP','targetdir':[],'distance':0,'passed':False,'latlong':[3.4420941546515,4.5021985657435]}
nodeQ = {'name':'nodeQ','targetdir':[],'distance':0,'passed':False,'latlong':[2.2248136881823,4.8602222323521]}
nodeR = {'name':'nodeR','targetdir':[],'distance':0,'passed':False,'latlong':[0.8285213884087,5.8268861321953]}
nodeS = {'name':'nodeS','targetdir':[],'distance':0,'passed':False,'latlong':[-0.3887590780605,0.3133216664229]}
nodeT = {'name':'nodeT','targetdir':[],'distance':0,'passed':False,'latlong':[-11.5590974762488,-1.4051919332984]}
nodeU = {'name':'nodeU','targetdir':[],'distance':0,'passed':False,'latlong':[-11.0220619763359,3.2133133659525]}
nodeV = {'name':'nodeV','targetdir':[],'distance':0,'passed':False,'latlong':[8.2754136538676,5.2182458989607]}
nodeW = {'name':'nodeW','targetdir':[],'distance':0,'passed':False,'latlong':[4.5161651544773,8.726877831725]}
nodeZ = {'name':'nodeZ','targetdir':[],'distance':0,'passed':False,'latlong':[-0.3887590780605,9.4429251649422]}
nodeA1 = {'name':'nodeA1','targetdir':[],'distance':0,'passed':False,'latlong':[-9.2319436432929,-3.1595078996805]}
nodeB1 = {'name':'nodeB1','targetdir':[],'distance':0,'passed':False,'latlong':[-4.0406004774682,1.566404499553]}
nodeC1 = {'name':'nodeC1','targetdir':[],'distance':0,'passed':False,'latlong':[-7.2270111102847,4.2873843657783]}


nodeA.update({'openmove':[nodeB]})
nodeB.update({'openmove':[nodeA, nodeC]})
nodeC.update({'openmove':[nodeB, nodeD, nodeV]})
nodeD.update({'openmove':[nodeC, nodeE, nodeP]})
nodeE.update({'openmove':[nodeD, nodeF, nodeP]})
nodeF.update({'openmove':[nodeE, nodeS]})
nodeG.update({'openmove':[nodeH, nodeS, nodeB1]})
nodeH.update({'openmove':[nodeG, nodeA1]})
nodeI.update({'openmove':[nodeT, nodeJ, nodeA1]})
nodeJ.update({'openmove':[nodeI, nodeK]})
nodeK.update({'openmove':[nodeJ]})
nodeL.update({'openmove':[nodeO, nodeR, nodeB1, nodeC1]})
nodeM.update({'openmove':[nodeU, nodeT]})
nodeN.update({'openmove':[nodeW, nodeZ]})
nodeO.update({'openmove':[nodeZ, nodeL]})
nodeP.update({'openmove':[nodeE, nodeQ]})
nodeQ.update({'openmove':[nodeP, nodeR]})
nodeR.update({'openmove':[nodeQ, nodeL]})
nodeS.update({'openmove':[nodeF, nodeG]})
nodeT.update({'openmove':[nodeI, nodeM]})
nodeU.update({'openmove':[nodeM, nodeC1]})
nodeV.update({'openmove':[nodeC,nodeW]})
nodeW.update({'openmove':[nodeV, nodeN]})
nodeZ.update({'openmove':[nodeN, nodeO]})
nodeA1.update({'openmove':[nodeH, nodeI]})
nodeB1.update({'openmove':[nodeG, nodeL]})
nodeC1.update({'openmove':[nodeL, nodeU]})

#y
playerlat = 9.8149154202846
#x 
playerlong = 4.5021985657435
#y
exitlat = -13.7788442092221
#x
exitlong = -9.2101078653659

nodelist = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH, nodeI, nodeJ, nodeK, nodeL, nodeM, nodeN, nodeO, nodeP, nodeQ, nodeR, nodeS, nodeT, nodeU, nodeV, nodeW, nodeZ, nodeA1, nodeB1, nodeC1]

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
