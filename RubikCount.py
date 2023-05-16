
import re 

GAPtxt = open("/Users/cathaoir/Desktop/gap.txt","r")
FromGap = GAPtxt.read()
FromGap = FromGap.replace('\n','')
FromGap = FromGap.replace(" ","")

colours = [2,3,4,5,6,7,8,9,10]

list = []
CycleLengths = []

def replace(g):
    return g.group(0).replace(',',' ')

FromGap = re.sub(r'\(.*?\)', replace, FromGap)
Cycles = FromGap.split(',')


for d in Cycles:

    m = re.findall(r'\(((?:\d+\s*)+)\)', d)
    
    for i in m:
        list.append(len(i.split()))

    CycleLengths.append(list)
    list = []


sum = 0

for r in colours:

    for item in CycleLengths:
    
        a = 24
        t = 1

        for i in range(2,25):
            x = item.count(i)
            a = a - (i*x)
            t = (r**x) * t

        t = (r**a) * t
        sum += t 

    print(int(sum / len(CycleLengths)))




