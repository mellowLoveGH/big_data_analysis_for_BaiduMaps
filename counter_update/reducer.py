
import sys

# for PV, success rate, finish calculation
# for UV, remove the redundancy
# for accuracy, sampling by every hour and every grid

fre = 0
val = ""
lastKey = False

for data in sys.stdin:
    data = data.strip()
    #sys.stdout.write("%s\n"%(data))
    try:
        record = data.split('\t')
        curKey = record[0]
        value = record[1]
        if lastKey and curKey !=lastKey:
            #sys.stdout.write("%s\t%s\n"%(lastKey,fre))
            ch = lastKey[0]
            if ch=="S":
                sys.stdout.write("%s\t%s#C\n"%(lastKey,val)) 
            elif ch=="U":
                sys.stdout.write("%s\t%s#B\n"%(lastKey,fre))
            else:
                sys.stdout.write("%s\t%s#A\n"%(lastKey,fre))  
            #
            lastKey = curKey
            ch = lastKey[0]
            if ch=="S":
                val = value
            else:
                fre = int(value)
        else: 
            lastKey = curKey
            ch = curKey[0]
            if ch=="S":
                val = value
            else:
                fre = fre + int(value)
    except:
        sys.stdout.write("%00\t1#A\n")
if lastKey:
    ch = lastKey[0]
    if ch=="S":
        sys.stdout.write("%s\t%s#C\n"%(lastKey,val))
    elif ch=="U":
        sys.stdout.write("%s\t%s#B\n"%(lastKey,fre))
    else:
        sys.stdout.write("%s\t%s#A\n"%(lastKey,fre))






