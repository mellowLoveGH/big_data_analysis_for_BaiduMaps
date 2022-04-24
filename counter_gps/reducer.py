import sys

# get the results for UV and accuracy rate

fre = 0
lastKey = False
for data in sys.stdin:
    data = data.strip()
    try:
        record = data.split('\t')
        curKey = record[0]
        value = int(record[1])
        if lastKey and curKey !=lastKey:
            #fre = fre + value
            sys.stdout.write("%s\t%s\n"%(lastKey,fre))
            lastKey = curKey
            fre = value
        else:
            lastKey = curKey
            fre = fre + value
    except:
        sys.stdout.write("%s\t%s\n"%("00",1))
if lastKey:
    sys.stdout.write("%s\t%s\n"%(lastKey,fre))
