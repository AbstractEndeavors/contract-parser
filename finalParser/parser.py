import json
import os
import shutil
import shutil, errno
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def changeGlob(x,v):
    globals()[x] = v
def lsInString(ls,x):
    for i in range(0,len(ls)):
        if ls[i] in x:
            return ls[i]
    return False
def eatInner(x,ls):
    if len(x) == 0:
        return x
    z = x
    for i in range(0,len(x)):
        if x[i] not in ls:
            return x[i:]
        

    return z
def eatAll(x,ls):
    return eatOuter(eatInner(x,ls),ls)
def getlower(ls):
    lowest = [len(ls[0]),0]
    for i in range(1,len(ls)):
        if len(ls[i])<lowest[0]:
            lowest = [len(ls[i]),i]
    return lowest
def tabIt(ls,y,h):
    l = 0
    if h == '}':
        l = 1
    k = ls[0]-ls[1]
    n = ''
    for i in range(0,k-l):
        n = n + '\t'
    return y[0]+'\n'+n+y[1],True
def eatOuter(x,ls):
    if len(x) == 0:
        return x
    z = x
    k = len(x)
    for i in range(0,len(x)):
        if z[-1] not in ls:
            return z
        z = z[:k]
        k -=1
    return z
def findItRet(x,ls):
    for i in range(0,len(ls)):
        if ls[i] == x:
            return ls[i]
def delBetween(x):
    x = cleanSpaces(x.replace('\t','').replace('  ',' '))
    go,z = True,''
    j = 0
    lsCount = [[0,0,False],[0,0,False],[0,0,False]]
    ifWhile,lsMake = [],[]
    for h in range(0,len(x)):
        nex = ''
        if h!=len(x)-1:
            nex = x[h+1]
        if x[h] == '(':
            lsCount[0][0] +=1
            lsCount[0][-1] = True
            if z[-len('if'):] == 'if' or z[-len('while'):] == 'while':
                ifWhile.append([lsCount[0][0],lsCount[2][0]])
        if x[h] == ')':
            lsCount[0][1] +=1
            if len(ifWhile) >0:
                if ifWhile[-1][0] == lsCount[0][1] and nex != '{':
                    lsCount[2][-1] == True
                    y,line = tabIt(lsCount[2],['{',''],x[h])
            if lsCount[0][0] == lsCount[0][1]:
                lsCount[0] = [0,0,False]
        if x[h] == '[':
            lsCount[1][0] +=1
            lsCount[1][-1] = True
        if x[h] == ']':
            lsCount[1][1] +=1
            if lsCount[1][0] == lsCount[1][1]:
                lsCount[1] = [0,0,False]
        if x[h] == '{':
            lsCount[2][0] +=1
            lsCount[2][-1] == True
            y,line = tabIt(lsCount[2],['{',''],x[h+1])
        elif x[h] == '}':
            wh = ''
            lsCount[2][1] +=1
            if len(ifWhile)>0:
                if ifWhile[-1][1] == lsCount[2][0] - lsCount[2][1]:
                    ifWhile = ifWhile[:-1]
                if ifWhile[-1][1] < lsCount[2][0] - lsCount[2][1]:
                    wh,line = tabIt(lsCount[2],['}',''],'')
                    ifWhile = ifWhile[:-1]
            if lsCount[2][0] == lsCount[2][1]:
                lsCount[2] = [0,0,False]

            y,line = tabIt(lsCount[2],['}',''],nex)
            y = wh + y
        elif x[h] == ';' and lsCount[0][-1] == False:
            y,line = tabIt(lsCount[2],[';',''],nex)
        else:
            if nex == '}':
                y,line = tabIt(lsCount[2],[x[h],''],nex)
            else:
                y = x[h]
                line = False
        z = z + y
    lsMake.append(z)
    z = ''
    for i in range(0,len(lsMake)):
        z = z + lsMake[i]
    
    return z
def cleanSpaces(x):
    ls = [',','(',')','{','}','(',')','=','*','//',':',';','+','-','!']
    lsN = ['\t',' ']
    for i in range(0,len(ls)):
        while lsInString([lsN[0]+ls[i],lsN[1]+ls[i]],x) != False:
            rep = lsInString([lsN[0]+ls[i],lsN[1]+ls[i]],x)
            x = x.replace(rep,ls[i])
        while lsInString([ls[i]+lsN[0],ls[i]+lsN[1]],x) != False:
            rep = lsInString([ls[i]+lsN[0],ls[i]+lsN[1]],x)
            x = x.replace(rep,ls[i])
    return x
def commUncomm(ogRead):
   
    beg = 0
    lsA = []
    ogNew = ogRead
    lastLen = len(ogNew)
    length = 0
    while len(ogNew) >0 and lastLen != length:
        length,i = getlower([ogNew.split(ls[0][0])[0],ogNew.split(ls[1][0])[0],ogNew.split(ls[2][0])[0]])
        lsA.append(ogNew[:length])
        ogNew = ogNew[length+len(ls[i][0]):]
        j,z = 0,''
        while ls[i][1] not in z and ls[i][1] in ogNew:
            z = ogNew[:j]
            ogNow = ogNew[j:]
            j+=1
        lsA.append(ls[i][0]+z)
        ogNew = ogNow
        lastLen = len(ogNew)
    u = ''
    for i in range(0,len(lsA)):
        if float(i%2) == float(0):
            u = u + lsA[i]
    changeGlob('lines',delBetween(u).split('\n'))
    n = ''
    for i in range(0,len(lsA)):
            n = n + lsA[i]
    changeGlob('linesCommented',delBetween(n).split('\n'))
def parseIt(x):
    lines = cleanSpaces(reader(x)).replace('(',' ( ').replace(')',' ) ').replace('{',' { ').replace('}',' } ').replace(';',' ; ').replace(',',' , ').replace('.',' . ').replace('[]','[^*^*^*]').replace('[',' [').replace(']',' ] ').split('\n')
    allSides = []
    for i in range(0,len(lines)):
        x = [eatInner(lines[i],[' ','\n','\t',''])]
        
    
        jsVa =  {"type":"",'name':"","internalType":'"nonpayable','inputs':[],'stateMutability':'public','outputs':[]}
        jsI = {}
        jsO = {}
        js = [jsI,jsO]
        m = ''
        mm = ''
        mmm = ''
        headers = ['pragma ','SPDX','contract','library','interface','abstract','constructor',"emit","import","function","modify"]
        types = ['uint','address','bytes','string','bool']
        stateImmutability = ["pure","view","payable","constant","immutable","anonymous","indexed","virtual","override","public","private","external","internal"]
        newSide = []
        for l in range(0,len(x)):
            side = x[l].split(' ')
            cou = 0
            for i in range(0,len(side)):
                if side[i] in ['(']:
                    if cou == 0:
                        new = ''
                    new = new + side[i]
                    cou +=1
                elif side[i] in [')']:
                    new = new + side[i]+' '
                    cou -=1
                    if cou == 0:
                        newSide.append(cleanSpaces(new))
                elif cou != 0:
                    new = new + ' '+side[i]
                elif side[i] != '':
                    newSide.append(side[i])
            side = newSide
            newSide = []
            for i in range(0,len(side)):
                if side[i] in ['[']:
                    if cou == 0:
                        new = ''
                    new = new + side[i]
                    cou +=1
                elif side[i] in [']']:
                    new = new + side[i]+' '
                    cou -=1
                    if cou == 0:
                        newSide.append(cleanSpaces(new))
                if cou != 0:
                    new = new + ' '+side[i]
                if side[i] != '':
                    newSide.append(side[i])
            side = newSide
            newSide = []
            for i in range(0,len(side)):
                if side[i] in ['"']:
                    if cou == 0:
                        new = ''
                    new = new + side[i]
                    cou +=1
                elif side[i] in ['"']:
                    new = new + side[i]
                    cou -=1
                    if cou == 0:
                        newSide.append(cleanSpaces(new))
                elif cou != 0:
                    new = new + ' '+side[i]
                elif side[i] != '':
                    newSide.append(side[i])
            side = newSide
            newSide = []
            wholeSide = []
            for i in range(0,len(side)):
                if '=' in side[i] and '==' not in side[i] and side[i][0] != '(':
                    spl = side[i].split('=')
                    newSide.append(spl[0])
                    wholeSide.append(newSide)
                    wholeSide.append(['='])
                    newSide = [spl[1]]
                
                else:
                    newSide.append(side[i])
            if len(newSide) != 0: 
                wholeSide.append(newSide)
                
        allSides.append(wholeSide)
    return allSides
def isLs(ls):
    if type(ls) is list:
        return True
    return False
def whileNotLs(ls):
    ogLs = ls
    for i in range(0,len(ls)):
        n = lsToStr(ls[i])
        while isLs(n):
           n = lsToStr(n)
    return ogLs
def lsToStr(ls):
    n = ''
    for i in range(0,len(ls)):
        n = n + ' '+ls[i]
    return n
