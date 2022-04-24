import sys

fre = 0
val = ""
lastKey = False
error_counter = 0

for data in sys.stdin:
    data = data.strip()
    try:
        record = data.split('\t')
        curKey = record[0]
        value = record[1]
        if lastKey and curKey !=lastKey:
            ch = lastKey[0]
            if ch=="S":
                sys.stdout.write("%s\t%s\n"%(lastKey,val)) 
            #
            lastKey = curKey
            ch = lastKey[0]
            if ch=="S":
                val = value
        else: 
            lastKey = curKey
            ch = curKey[0]
            if ch=="S":
                val = value
    except:
        error_counter += 1
#
if lastKey:
    ch = lastKey[0]
    if ch=="S":
        sys.stdout.write("%s\t%s\n"%(lastKey,val))


