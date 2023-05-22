
import re 

# reading in the text file
# removing all the new lines and spaces 
GAPtxt = open("/Users/cathaoir/Desktop/gap.txt","r")
FromGap = GAPtxt.read()
FromGap = FromGap.replace('\n','')
FromGap = FromGap.replace(" ","")

# list of colours
colours = [1,5,10]

# list of cycle lengths
list = []
CycleLengths = []

# function to replace commas with spaces
def replace(g):
    return g.group(0).replace(',',' ')

# splitting the cycles into a list
FromGap = re.sub(r'\(.*?\)', replace, FromGap)
Cycles = FromGap.split(',')

# finding the cycle lengths
for d in Cycles:
    
    m = re.findall(r'\(((?:\d+\s*)+)\)', d)
    
    for i in m:
        list.append(len(i.split()))

    CycleLengths.append(list)
    list = []

# place holder for the sum
sum = 0

# using PET to calculate number of distinct colourings
    # a = number of fixed points
    # t = number of colourings with r colours
    # x = number of cycles of length i
    # i = length of cycle
    # r = number of colours
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
    
    # output
    print(int(sum / len(CycleLengths)))




