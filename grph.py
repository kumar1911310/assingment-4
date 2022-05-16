def function(rosID, string):
    k = 3
    counter = 0
    suffix = string[len(string) - k:]
    #print 'suffix = ' + suffix
    #print 'id = ' + rosID
    for key in seqDict:
        prefix = seqDict[key][:k]
        #print 'prefix ' + prefix
        if suffix == prefix and key != rosID:
            print (rosID + ' ' + key)
    return None
inFile = open('rosalind_grph.txt', 'r')
count = -1
seqDict = {}
for line in inFile:
    line = line.strip()
    if line[0] == '>':
        count += 1
        seqKey = line[1:]
        seqDict[seqKey] = ''
    else:
        if count > -1:
            seqDict[seqKey] += line

for rosID in seqDict:
    function(rosID, seqDict[rosID])
